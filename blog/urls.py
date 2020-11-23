from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns=[
    path('',BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_detail'),
]
# here if in url post/1/ i.e "/1 is pk of the data in db which is held by
# 'object' a context object returned by DetailView see DetailView"
# comes it will redirect to BlogDetailView for the further process.