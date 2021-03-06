from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    
    path('post/<str:pk>/',views.post,name="post"),

    path('create-post/',views.createBlog,name="create-post"),
    path('update-post/<str:pk>/',views.updateBlog,name="update-post"),
    path('delete-post/<str:pk>/',views.deleteBlog,name="delete-post"),
]