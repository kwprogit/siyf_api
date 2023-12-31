from django.shortcuts import render
from rest_framework.views import APIView
from .models import (
    HeaderNews, 
    News, 
    Feedback,
    Employee,
    Sponsor
)

from .serializers import (
    HeaderNewsSerializer, 
    NewsSerializer, 
    SponsorSerializer, 
    EmployeeSerializer,
    FeedbackSerializer
)
from rest_framework.response import Response
from rest_framework import status 


class HeaderNewsList(APIView):
    def get(self, request, lang):
        qset = HeaderNews.objects.filter(lang_code=lang)
        return  Response(
            HeaderNewsSerializer(qset, many=True).data, 
            status=status.HTTP_200_OK
        )
    
class NewsList(APIView):
    def get(self, request, lang):
        qset = News.objects.filter(lang_code=lang)
        return  Response(
            NewsSerializer(qset, many=True).data, 
            status=status.HTTP_200_OK
        )
    

class EmployeeList(APIView):
    def get(self, request, lang):
        qset = Employee.objects.filter(lang_code=lang)
        return  Response(
            EmployeeSerializer(qset, many=True).data, 
            status=status.HTTP_200_OK
        )
    

class SponsorList(APIView):
    def get(self, request):
        qset = Sponsor.objects.filter()
        return  Response(
            SponsorSerializer(qset, many=True).data, 
            status=status.HTTP_200_OK
        )
    

class CreateFeedbackView(APIView):
    def post(self, request, *args, **kwargs):
        ser = FeedbackSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            feedback = Feedback(**ser.validated_data)
            feedback.save()
            email = feedback.email 
            send_copy_to_feedbacker(email, feedback)
            return Response({
                "message" : "OK",
            }, status=status.HTTP_200_OK)
        

def send_copy_to_feedbacker(email , feedback):
    return None