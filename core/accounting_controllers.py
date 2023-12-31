from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status   
from .permissions import IsSuper, IsAuth
from .serializers import AdminSerializer
from .models import Admin
from config import settings as config_settings
from rest_framework.authtoken.models import Token

class AdminViewSet(APIView):
    permission_classes = [IsAuth, IsSuper]
    def post(self , request):
        ser = AdminSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            valdata = ser.validated_data
            username = valdata['username']
            password = valdata['password']
            try:
                Admin.objects.get(username=username)
                return Response({
                    "message" : f"User with username {username} already exists"
                }, status=status.HTTP_400_BAD_REQUEST)
            except: pass 
            new_admin = Admin(username=username)
            # new_admin = Admin(username=username, raw_password=password)
            new_admin.set_password(password)
            new_admin.save() 
            return Response({
                "message" : "Success"
            }, status=status.HTTP_200_OK)

    def patch(self, request):
        ser = AdminSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            valdata = ser.validated_data
            username = valdata['username']
            password = valdata['password']
            try:
                admin_user  = Admin.objects.get(username=username)
                # admin_user.raw_password = password
                admin_user.set_password(password)
            except:
                return Response({
                    "message" : f"User {username} not found"
                }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        ser = AdminSerializer(data=request.data)    
        if ser.is_valid(raise_exception=True):
            valdata = ser.validated_data
            username = valdata['username']
            try:
                admin_user = Admin.objects.get(username=username)
            except:
                return Response({
                    "message" : f'User {username} not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
class GetRootToken(APIView):
    def get(self, request, *args, **kwargs):
        if config_settings.DEBUG:
            user = Admin.objects.get(username='root')
            token, created = Token.objects.get_or_create(user=user)
            return Response(token.token, 200)
        else:
            return Response({
                "message" : "Cant run in prod mode", 
                }, 
                status=status.HTTP_403_FORBIDDEN
            )
