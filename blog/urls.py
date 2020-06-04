from django.urls import path
 
from . import views#

app_name='blog'
urlpatterns = [
    
    path('',views.all_blogs,name='all_blogs'),#here name is specified so that we can specify url or path to use it in other part like html file 
    path('<int:blog_id>',views.detail,name='detail'), 
]