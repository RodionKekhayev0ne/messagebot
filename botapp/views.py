from django.http import JsonResponse
from django.shortcuts import render
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from botapp.models import Application
from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'  # Вы можете указать конкретные поля вместо '__all__'


# Create your views here.
@api_view(['GET'])
def get_applications(request):
    apps = Application.objects.all().values()
    serializer = ApplicationSerializer(apps, many=True)

    return Response(serializer.data)
