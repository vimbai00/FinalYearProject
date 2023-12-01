
from django.contrib import admin
from django.urls import path
from Discussion_forum.views import *

urlpatterns = [
    
    path('',forumhome,name='forumhome'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]
