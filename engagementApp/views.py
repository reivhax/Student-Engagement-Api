from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser+
# from django.http import Http404
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.decorators import APIView
# from rest_framework.response import Response
# from rest_framework import mixins
from rest_framework import generics
from .models import Articles
from .serializer import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
 #this is the one for getting all the articles. So idealy, we get the objects from the model class then serialize them and return as Json data 

class ArticleList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete an article instance.
    """
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly, )
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
