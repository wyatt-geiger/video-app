from django.shortcuts import render
from django.contrib import messages
from .forms import VideoForm

# Create your views here.

def home(request):
    app_name = 'Podcasts'
    return render(request, 'video_collection/home.html')

def add(request):
    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(request, 'New video saved')
    # if the request method is POST and the new video form is valid, it will be saved to the database
    # otherwise, the page will reload
        else:
            messages.warning(request, 'Please check the data entered.')
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
    
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})