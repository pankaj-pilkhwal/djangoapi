from django.contrib import admin
from django.urls import include, path
from api.views import CompanyViewSet, EmployeeViewSet, home_page
from rest_framework import routers, exceptions


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)

router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('home', home_page),
]


# companies/{companyID}/employees