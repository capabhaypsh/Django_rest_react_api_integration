from rest_framework import serializers
from img_upload_api.models import Profile

class ProfileSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = ['id','name','email','dob','state','gender','loaction','pimage','rdoc']
        fields = '__all__'

