from django.urls import path
from .views import HomePageView, BlogsPageView

urlpatterns = [
  path('', HomePageView.as_view(), name = 'home'),
  path('Blog/<int:pk>', BlogsPageView.as_view(), name = 'blog')
]