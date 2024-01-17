from rest_framework.response import Response
from rest_framework.views import APIView

from .models import InformationOverdue
from .serializers import ModelListSerialializer


class InformationOverdueListView(APIView):

    def get(self, request):
        overdue = InformationOverdue.objects.all()
        serializer = ModelListSerialializer(overdue, many=True)
        return Response(serializer.data)