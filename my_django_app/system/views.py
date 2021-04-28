from rest_framework import viewsets
from system.models import Client, Purchase
from system.serializer import ClientSerializer, PurchaseSerializer

class ClientsViewSet(viewsets.ModelViewSet):
    """Showing all the clients"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class PurchasesViewSet(viewsets.ModelViewSet):
    """Showing all the purchases"""
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


