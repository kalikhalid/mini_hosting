from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Video
from django.urls import reverse_lazy

class VideoCreateView(CreateView):
    model = Video
    fields = ['title', 'video_file', 'description',]
    template_name = 'hosting/upload.html'
    success_url = reverse_lazy('hosting:index') # TODO доделать
    def form_valid(self, form):
        form.instance.user = self.request.user
        resource = super().form_valid(form)
        return resource

class VideoListView(ListView):
    model = Video
    template_name = "hosting/vidoes-list.html"

    def get_queryset(self):
        return Video.objects.all()