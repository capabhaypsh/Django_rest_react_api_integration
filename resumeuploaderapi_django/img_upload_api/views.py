from rest_framework.response import Response

# Create your views here.
from img_upload_api.models import Profile
from img_upload_api.serializers import ProfileSerialzer
from rest_framework.views import APIView
from rest_framework import status

class ProfileView(APIView):
    def post(self,request,format=None):
        serializer = ProfileSerialzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume Upload Succesfully','status':'success','candidate':serializer.data},
            status=status.HTTP_201_CREATED)
        return Response(self,request,format=None)

    def get(self,request,formate=None):
        candidates = Profile.objects.all()
        serializer = ProfileSerialzer(candidates,many=True)
        return Response({'status':'success','candidates':serializer.data},
            status=status.HTTP_200_OK)






