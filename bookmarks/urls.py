from django.urls import path
from .views import BookmarkListCreateView, BookmarkDetailView

urlpatterns = [
    path('bookmarks/', BookmarkListCreateView.as_view(), name='bookmark-list-create'),
    path('bookmarks/<int:pk>/', BookmarkDetailView.as_view(), name='bookmark-detail'),
]
