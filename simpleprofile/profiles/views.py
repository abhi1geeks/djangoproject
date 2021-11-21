
from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProfileSerializer
from .models import SimpleProfiles

@api_view(['GET'])
def profileList(request):
    profiles=SimpleProfiles.objects.all()
    serializer=ProfileSerializer(profiles,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profileDetails(request,pk):
    profile=SimpleProfiles.objects.get(id=pk)
    serializer=ProfileSerializer(profile,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def profileCreate(request):
    serializer=ProfileSerializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            _status='success'
        return Response(serializer.data)
    except Exception as e:
        msg_err=e.args
        ser_err= serializer.errors
        return Response('Profile can not created because of %s \n and %s'%(msg_err,ser_err),status=400)


@api_view(['POST'])
def profileUpdate(request,pk):
    try:
        profile=SimpleProfiles.objects.get(id=pk)
        serializer=ProfileSerializer(instance=profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except profile.DoesNotExist:
        return HttpResponse(status=404)
    except Exception as e:
        msg_err=e.args
        return Response('Profile %s can not update because of %s'%(pk,msg_err))


@api_view(['DELETE'])
def profileDelete(request,pk):
    try:
        profile=SimpleProfiles.objects.get(id=pk)
        profile.delete()
        return Response('id:%s Profile Deleted'%pk)
    except Exception as e:
        err_msg=e.args
        return Response('Profile id:%s does not exists.getting errors : %s'%(pk,err_msg))
    
