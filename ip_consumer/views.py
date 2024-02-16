from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import IPAddressSerializer


class IPAddressListView(APIView):
    serializer_class = IPAddressSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
