from django.urls import path

from .views import *
app_name='blog'

urlpatterns=[
    path('', home_page, name='home_page'),
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),


    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail_page, name='post_detail'),


]