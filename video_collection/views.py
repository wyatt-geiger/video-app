from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.functions import Lower
from .forms import VideoForm, SearchForm
from .models import Video


# Create your views here.

def home(request):
    app_name = 'Podcasts'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            
            try:
                new_video_form.save()
                return redirect('video_list')
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'That video has already been added')
    # if the request method is POST and the new video form is valid, it will be saved to the database
    # otherwise, the page will reload
        
        messages.warning(request, 'Please check the data entered.')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
    
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

def video_list(request):

    search_form = SearchForm(request.GET) # build form from data user has sent to app

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']
        videos = Video.objects.filter(name__icontains=search_term).order_by(Lower('name'))
        # searches for a video that contains the search term, orders it alphabetically and ignores case
    else: # form not valid, not filled in, user has not had chance to enter anything
        search_form = SearchForm()
        videos = Video.objects.order_by('name')

    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos, 'search_form': search_form})