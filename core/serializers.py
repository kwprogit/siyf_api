from rest_framework import serializers
from .models import (
    HeaderNews, 
    News, 
    Feedback,
    Employee,
    Sponsor
)


class AdminSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class HeaderNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderNews
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class FeedbackSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    email = serializers.EmailField()
    phone = serializers.CharField(required=False)
    feedback = serializers.CharField()
