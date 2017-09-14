from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import WebUrlShortnerSerializer, WebUrlExpanderSerializer


class UrlShortnerApi(APIView):
    def post(self, request):
        serializer = WebUrlShortnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrlExpanderApi(APIView):
    def post(self, request):
        serializer = WebUrlExpanderSerializer(instance=request.data.get("url"))
        return Response(serializer.data, status=status.HTTP_200_OK)
