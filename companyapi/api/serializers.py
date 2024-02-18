from rest_framework import serializers
from api.models import Company, Employee


# Create Serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Company
        # fields = '__all__'
        fields = ["id", 'name', 'location', 'about', 'type', 'added_date', 'active']
        # id = serializers.ReadOnlyField()


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField

    class Meta:
        model = Employee
        fields = "__all__"
        