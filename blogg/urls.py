from django.urls import path
from .views import BlogListView, BlogView
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogView.as_view(), name='post_detail')
]
