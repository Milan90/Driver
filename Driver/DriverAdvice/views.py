from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import *
from .serializers import *


class AdviceList(APIView):
    def get(self, request, format=None):
        advices = Advice.objects.all()
        serializer = AdviceSerializer(advices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


