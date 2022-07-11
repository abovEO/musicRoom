from django.shortcuts import render
from .models import room
from .serializer import RoomSerializer
from rest_framework import generics

class roomView(generics.CreateAPIView):
    queryset = room.objects.all()
    serializer_class = RoomSerializer

# Create your views here.
# def main(request):
#     return HttpResponse("Hello")