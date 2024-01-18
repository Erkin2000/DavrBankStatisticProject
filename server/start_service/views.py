
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import HttpResponse, render

from .models import InformationOverdue, Example
from .serializers import ModelListSerialializer
from tablib import Dataset
from .resources import ExampleResource

class InformationOverdueListView(APIView):

    def get(self, request):
        overdue = InformationOverdue.objects.all()
        serializer = ModelListSerialializer(overdue, many=True)
        return Response(serializer.data)



# def GetExcel(request):
#     if request.method == 'POST':
#         info_resource = ExampleResource()
#         dataset = Dataset()
#         new_info = request.FILES['file']
#         imported_data = dataset.load(new_info.read(), format='xlsx')
#         for data in imported_data:
#             value = Example(
#                 data[0],
#                 data[1],
#                 data[2],
#                 data[3]
#             )
#             value.save()
#     return render(request, 'form.html')

def GetExcel(request):
    if request.method == 'POST':
        info_resource = ExampleResource()
        dataset = Dataset()
        new_info = request.FILES['file']
        imported_data = dataset.load(new_info.read(), format='xlsx')
        for data in imported_data:
            value = Example(
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[13],
                data[14],
            )
            value.save()
    return render(request, 'form.html')



