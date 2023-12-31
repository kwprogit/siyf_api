from django.urls import path 
from rest_framework.response import Response
from rest_framework import status 
from .views import (
        HeaderNewsList, 
        NewsList, 
        EmployeeList, 
        SponsorList, 
        CreateFeedbackView, 
    )
from .accounting_controllers import AdminViewSet
urlpatterns = [
    path('manage_users/', AdminViewSet.as_view() ), 
    # path('headernews/create/', HeaderNewsList.as_view()), 
    path('<str:lang>/header/news/list/', HeaderNewsList.as_view()),
    path('<str:lang>/news/list/',NewsList.as_view()), 
    path('<str:lang>/employee/list/' , EmployeeList.as_view()), 
    path('sponsor/list/', SponsorList.as_view()), 
    path('feedback/create/', CreateFeedbackView.as_view())
]

def handler404(*args, **kwargs):
    return Response({
        "message" : "Permission denied to this URL. Suchara", 
    }, 
    status= status.HTTP_403_FORBIDDEN)
