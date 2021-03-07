from django.shortcuts import redirect,render
import requests
from django.conf import settings
from isodate import parse_duration,parse_datetime,parse_time
from.forms import CreateUserForm
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required
from.decorators import*

from django.contrib.auth.models import Group
from.models import*
# Create your views here.
@login_required(login_url='login')
def home(request):
  Searched_Url = "https://www.googleapis.com/youtube/v3/search" 
  comment_url = "https://www.googleapis.com/youtube/v3/commentThreads"
  post = request.POST.get('search')
  print(post)
  if post is not None: 
    user = request.user.customer
    search = Search.objects.create(user=user,Text_searched=post)
  
  #https://youtu.be/
  #C-gEQdGVXbk
  
  
  params = {
    'part':'snippet',
    'q':post,
    'key': settings.YOUTUBE_DATA_API_KEY,
    'maxResults':20,
    'type':'video'
  }
  r = requests.get(Searched_Url,params=params)
  
  result = r.json()["items"]
  videos = []
  
  # loop
  for results in result:
    videos_data = {
      'title':results['snippet']['title'],
      'id':results['id'],
      #'duration' : parse_duration(results['contenDetails']['duration'].total_second()//60),
      'thumbnail':results['snippet']['thumbnails']['high']['url'],
      'ChannelTitle':results['snippet']['channelTitle'],
      'publishedAt':results['snippet']['publishedAt'],
      'channelId': results['snippet']['channelId'],
      'description':results['snippet']['description'],
      #'viewerRating':results['snippet']['viewerRating'],
      #'likeCount':results['snippet']['lilikeCount'],
    }
    videos.append(videos_data)
    #print(results['snippet']['channelTitle'])
  #print(videos)

  BaseUrl ="https://www.youtube.com/embed/{}"
  videose = results['id']['videoId']
  

  resultpage = BaseUrl.format(videose)
  resultingpage = videos[0]
  print(resultingpage)
  parsing_datetime = resultingpage['publishedAt']
  print(resultpage)
  params2 = {
    'part':['id','snippet','replies'],
    'videoId':videose,
    'key':settings.YOUTUBE_DATA_API_KEY,
    'maxResults':80,
    
    
  }
  r2 = requests.get(comment_url,params=params2)
  comments = r2.json()["items"]
  #print(r.text)
  print(r2.text)
  comments_video = []
  
  for comment in comments:
    comment_data = {
      'textDisplay':comment['snippet']['topLevelComment']['snippet']['textDisplay'],
      
      'textOriginal':comment['snippet']['topLevelComment']['snippet']['textOriginal'],
      
      'authorProfileImageUrl':comment['snippet']['topLevelComment']['snippet']['authorProfileImageUrl'],
      
      'authorDisplayName':comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
      
      'authorChannelUrl':comment['snippet']['topLevelComment']['snippet']['authorChannelUrl'],
      
      'authorChannelId':comment['snippet']['topLevelComment']['snippet']['authorChannelId'],
      
      'likeCount':comment['snippet']['topLevelComment']['snippet']['likeCount'],
      
      'publishedAt':comment['snippet']['topLevelComment']['snippet']['publishedAt'],
      
      'updatedAt':comment['snippet']['topLevelComment']['snippet']['updatedAt'],
      
      'totalReplyCount':comment['snippet']['totalReplyCount'],
      
      
    }
    
    comments_video.append(comment_data)
  
  print(comment_data)
  
  
  #print(videose)
  context ={
    'videos':videos,
    'resultpage':resultpage,
    'resultingpage':resultingpage,
    'comments_video':comments_video
  }
  return render(request,'Api/home.html',context)
  
  
def homeDetail(request,id):
  context = {
    
  }
  return render(request,'Api/home.html',context)
@unauthenticated_user
def registerPage(request):
  forms = CreateUserForm()
  
  #
  if request.method == "POST":
    forms = CreateUserForm(request.POST)
    if forms.is_valid():
      forms.save()
      return redirect('login')
  
  context = {
    'forms':forms
  }
  return render(request,'Api/register.html',context)
    
@unauthenticated_user  
def loginPage(request):
  username = request.POST.get('username')
  password = request.POST.get('password')
  user = authenticate(username=username,password=password)
  if user is not None:
    if user.is_active:
      login(request,user)
      return redirect('/')
      #messages.success(request,'login')
    else:
      messages.error(request,'username OR password incorrect')
  messages.error(request,'invalid login')
  context = {
    'messages':messages,
  }
  return render(request,'Api/Login.html',context)
  
  
def logoutPage(request):
  logout(request)
  return redirect('login')
  
  
  
def setting(request,id):
  customers = customer.objects.filter(id=id)
  print(customers)
  
  context = {
    'customer':customers
  }
  return render(request,'Api/setting.html',context)
  
def history(request):
  user_his =request.user.customer
  #print(user_his)
  searchs = Search.objects.filter(user=user_his).order_by('-date')
  #print(searchs)
  context = {
    'user_his':user_his,
    'searchs':searchs
  }
  return render(request,'Api/history.html',context)
  
  
  