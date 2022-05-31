from django.shortcuts import render, get_object_or_404
from picturesque.models import Picturesque, Genre
from picturesque.serializers  import PicturesqueSerializer, GenreSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response

import datetime

# Create your views here.
def index(request):
    context ={
        "data":"cool and all",
        "list":[i for i in range(1,10,2)]
    }

    return render(request, "django.html", context)
    #template = loader.get_template('django.html')
    #return HttpResponse(template.render(context, request))

class PicturesqueViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Picturesque.objects.all()
        serializer = PicturesqueSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = PicturesqueSerializer(data=request.data)
        if serializer.is_valid():
            picturesque = Picturesque()
            picturesque.name = serializer.validated_data["name"]
            print(serializer.validated_data)
            genre=serializer.validated_data["genre"]
            picturesque.genre = Genre.objects.filter(name=genre["name"])
            picturesque.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        queryset = Picturesque.objects.all()
        
        picturesque = None
        try:
            picturesque = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = PicturesqueSerializer(picturesque)
        return Response(serializer.data)
    
class GenreViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        
        if serializer.is_valid():
            genre = Genre()
            genre.name = serializer.validated_data["name"]
            genre.save()
            return Response({"status": "OK"})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        queryset = Genre.objects.all()
        
        genre = None
        try:
            genre = get_object_or_404(queryset, pk=pk)
        except:
            pass
        serializer = GenreSerializer(genre)
        return Response(serializer.data)