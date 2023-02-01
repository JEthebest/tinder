from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from .models import Questionnaire, Like, Photo
from .serializers import QuestionnaireSerializer, LikeSerializer, PhotoSerializers

# Create your views here.

class QuestionnaireViewSet(ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    

class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializers
