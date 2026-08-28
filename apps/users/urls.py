from django.urls import path
from .views import (
    AuthorListCreateView, 
    UserProfileViewSet
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    
    path('user-profiles/', UserProfileViewSet.as_view({
        'get': 'list', 
        'post': 'create'
    }), name='user-profile-list'),
    
    path('user-profiles/<int:pk>/', UserProfileViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'patch': 'partial_update', 
        'delete': 'destroy'
    }), name='user-profile-detail'),
]