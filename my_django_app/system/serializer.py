from django.db.models import fields
from rest_framework import serializers
from system.models import Client, Purchase

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        exclude = []