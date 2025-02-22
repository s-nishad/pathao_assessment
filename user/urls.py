from django.urls import path
# from .views import CreateUserView, RetrieveUserView, AddUserTagsView, GetUsersByTagsView, UserOperation
from .views import RetrieveUserView, AddUserTagsView, UserOperation

urlpatterns = [
    path('users', UserOperation.as_view(), name='create-user'),
    path('users/<int:id>', RetrieveUserView.as_view(), name='get-user'),
    path('users/<int:id>/tags', AddUserTagsView.as_view(), name='add-user-tags'),
    # path('users/', GetUsersByTagsView.as_view(), name='get-users-by-tags'),
]
