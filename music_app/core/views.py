from django.shortcuts import render, redirect

from music_app.core.forms import ProfileForm, AlbumForm, DeleteProfileForm, DeleteAlbumForm
from music_app.core.models import Profile, Album


# Create your views here.


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    else:
        return None


def show_index(request):
    if get_profile():
        albums = Album.objects.all()
        context = {'albums': albums}
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                to = ''
                return redirect('show index')
        else:
            form = ProfileForm()

        context = {'form': form}

        return render(request, 'home-no-profile.html', context)


def add_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('show index')
    else:
        album_form = AlbumForm()

    context = {
        'album_form':album_form
    }
    return render(request, 'add-album.html', context)


def show_album(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST, request.FILES, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('show index')
    else:
        album_form = AlbumForm(instance=album)
    context = {
        'album_form': album_form,
        'pk':pk
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)

    context={
        'form':form,
        'pk':pk
    }
    return render(request, 'delete-album.html', context)


def show_profile(request):
    profile = get_profile()
    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': len(albums)
    }
    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == "POST":
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)


def add_context_to_base(request):
    context = {
        'profiles': Profile.objects.all()
    }
    return render(request, 'base.html', context)

