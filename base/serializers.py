from rest_framework import serializers
from .models import Product, ProductType, Purchase, Sell, Department, Vendor

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'