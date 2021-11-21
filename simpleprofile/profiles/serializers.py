from django.db.models import fields
from rest_framework import serializers,validators
from .models import SimpleProfiles


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleProfiles
        fields='__all__'
        print(model.firstName)
        # fields = ('id','firstName','lastName','dob','email','mobileNumber')



