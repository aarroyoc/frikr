from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View, ListView
from django.db.models import Q

from photos.models import Photo, PUBLIC
from photos.forms import PhotoForm

class PhotosQuerySet():

    @staticmethod
    def get_photos_queryset(request):
        if not request.user.is_authenticated:
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser:
            photos = Photo.objects.all()
        else:
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos

class HomeView(View):
    def get(self, request):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            "photos_list": photos
        }
        return render(request, "photos/home.html", context)


def detail(request, pk):
    # try/except con Photo.objects.get
    photos = PhotosQuerySet.get_photos_queryset(request).filter(pk=pk).select_related("owner")
    photo = photos[0] if len(photos) == 1 else None
    if photo is not None:
        context = {
            "photo": photo
        }
        return render(request, "photos/detail.html", context)
    else:
        return HttpResponseNotFound()


@login_required()
def create(request):
    success_message = ""
    if request.method == "GET":
        form = PhotoForm()
    else:
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user
        form = PhotoForm(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save()
            form = PhotoForm()
            url = reverse("photo_detail", args=[new_photo.pk])
            success_message = "Guardado con éxito"
            success_message += f"<a href='{url}'>"
            success_message += "Ver foto"
            success_message += "</a>"

    context = {
        "form": form,
        "success_message": success_message
    }
    return render(request, 'photos/new_photo.html', context)


class PhotoListView(View):
    def get(self, request):


        context = {
            "photos": PhotosQuerySet.get_photos_queryset(request)
        }
        return render(request, "photos/photos_list.html", context)

class UserPhotosView(ListView):
    model = Photo
    template_name = "photos/user_photos.html"

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)