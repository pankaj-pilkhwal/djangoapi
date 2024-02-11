from django.http import HttpResponse, JsonResponse
import json


def home_page(request):
    print("Home page is requested")
    response_data = {"friends":["Pankaj", "Ankit", "Ravi", "Uttam"]}
    return JsonResponse(response_data)