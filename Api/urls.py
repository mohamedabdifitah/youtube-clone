from django.urls import path
#from django.contrib.auth import views as auth_views
from. import views


urlpatterns = [
    path('',views.home,name="home"),
    path('watch?/<str:id>',views.homeDetail,name="homeDetail"),
    
    #path('<str:name>',views.video,name="video"),
    path('register',views.registerPage,name="registration"),
    path('login',views.loginPage,name="login"),
    path('logout',views.logoutPage,name="logout"),
    path('setting/<int:id>',views.setting,name='setting'),
    path('history',views.history,name="history"),
]



'''path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
path('reset/<uidb64><token>/',auth_views.PasswordResetConfrimView.as_view(),name="password_reset_confirm"),
path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")'''