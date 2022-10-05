from django.urls import path

from music_app.core.views import show_index, add_album, show_album, edit_album, delete_album, show_profile, \
    delete_profile

urlpatterns = [
    path('', show_index, name='show index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', show_album, name='show album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/details/', show_profile, name='show profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
