from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListAPIView
from rest_framework.response import Response
from .serializers import ProfileSerializer
from .models import SimpleProfiles

class ProfileListApi(ListAPIView):
    queryset = SimpleProfiles.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailsApi(RetrieveAPIView):
    queryset = SimpleProfiles.objects.all()
    serializer_class = ProfileSerializer

class ProfileCreateApi(CreateAPIView):
    queryset = SimpleProfiles.objects.all()
    serializer_class = ProfileSerializer

class ProfileUpdateApi(UpdateAPIView):
    queryset = SimpleProfiles.objects.all()
    serializer_class = ProfileSerializer
   

class ProfileDeleteApi(DestroyAPIView):
    queryset = SimpleProfiles.objects.all()
    serializer_class = ProfileSerializer