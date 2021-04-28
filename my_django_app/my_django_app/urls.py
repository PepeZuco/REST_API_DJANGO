from django.contrib import admin
from django.db.models import base
from django.urls import path, include
from system.views import ClientsViewSet, PurchasesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients', ClientsViewSet,basename='Clients')
router.register('purchase', PurchasesViewSet, basename='Purchases')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]

