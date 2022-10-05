from django import forms
from django.forms import ModelForm

from music_app.core.models import Profile, Album


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.TextInput(attrs={'placeholder': 'Description'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),

        }


class DeleteProfileForm(ModelForm):
    def save(self, commit=True):
        albums = Album.objects.all()
        albums.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = []


class DeleteAlbumForm(ModelForm):
    def save(self, commit=True):
        self.instance.delete()

    class Meta:
        model = Album
        fields = '__all__'
