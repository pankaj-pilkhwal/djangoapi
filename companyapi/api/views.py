
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    # permission_classes = [permissions.IsAuthenticated]

    # for custom api's
    # 
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=10):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps, many=True, context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message': "Error: Company might not exists !!! "
            })
        

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# def home_page(request):
#     print("Home page is requested")
#     response_data = {"friends":["Pankaj", "Ankit", "Ravi", "Uttam"]}
#     return JsonResponse(response_data)
#     return HttpResponse("<h1>The requested page is not available</h1>")


def home_page(request):
    print("home_page is requested")
    return render(request, "index.html")