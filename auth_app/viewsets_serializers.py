from rest_framework import serializers
from .models import TeleVision, Mobile, Company


class TelevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeleVision
        fields = ['company', 'model', 'price']


class MobileSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Company.objects.all()
    )

    class Meta:
        model = Mobile
        fields = ['brand', 'ram', 'rom']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyMobileSerializer(serializers.ModelSerializer):
    brand = CompanySerializer()

    class Meta:
        model = Mobile
        fields = "__all__"
