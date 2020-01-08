from rest_framework.views import APIView
from rest_framework.response import Response
from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


#class PhotoListAPI(APIView):
#    def get(self, request):
#        photos = Photo.objects.all()
#        serializer = PhotoSerializer(photos, many=True)
#        return Response(serializer.data)

class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)