from django.urls import path
from .views import CreateUserView, RetrieveUserView, AddUserTagsView, GetUsersByTagsView

urlpatterns = [
    path('users/', CreateUserView.as_view(), name='create-user'),
    path('users/<int:id>', RetrieveUserView.as_view(), name='get-user'),
    path('users/<int:id>/tags', AddUserTagsView.as_view(), name='add-user-tags'),
    path('user/', GetUsersByTagsView.as_view(), name='get-users-by-tags'),
]
