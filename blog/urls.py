from django.urls import path
from .views import (
    BlogDetailView,
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
    )

urlpatterns=[
    path('post/<int:pk>/delete',BlogDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/new/',BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
    path('',BlogListView.as_view(), name = 'home'),
]
# here if in url post/1/ i.e "/1 is pk of the data in db which is held by
# 'object' a context object returned by DetailView see DetailView"
# comes it will redirect to BlogDetailView for the further process.