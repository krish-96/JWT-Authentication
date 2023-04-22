from rest_framework.views import APIView
from .models import TeleVision
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class TeleVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeleVision
        fields = ['company', 'model', 'price']


class TVListView(APIView):
    renderer_classes = [JSONRenderer]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    def get(self, *args, **kwargs):
        return Response({"detail": TeleVisionSerializer(TeleVision.objects.all().values_list('company'), many=True).data},
                        status=status.HTTP_200_OK)
