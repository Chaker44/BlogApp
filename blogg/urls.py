from django.urls import path
from .views import (
    BlogListView,
    BlogView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit', BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>', BlogView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),

]
