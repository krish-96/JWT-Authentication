from django.shortcuts import redirect

from .models import TeleVision, Mobile
from .viewsets_serializers import TelevisionSerializer, MobileSerializer, CompanyMobileSerializer

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

class NormalViewsetTeleVisionViewSet(viewsets.ViewSet):
    """
    This viewset is similar to APIVIew but the only difference is that is
    APIView will provide methods such as GET, POST, PUT, PATCH and DELETE
    ViewSets will provide methods such as LIST, RETRIEVE, CREATE, UPDATE, DELETE
    """
    queryset = TeleVision.objects.all()

    def list(self, request):
        serializer = TelevisionSerializer(self.queryset, many=True)
        return Response(serializer.data, template_name='rest_framework/api.html', status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        print(f"PK {pk} returned")
        try:
            queryset = self.queryset.get(id=pk)
        except Exception as E:
            return Response({"Error": "No record found with the given ID."}, status=status.HTTP_200_OK)
        print("queryset : ", queryset)
        serializer = TelevisionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        print("Data : {}".format(data))
        serializer = TelevisionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("Valid Serializer")
            serializer.save()
            return Response(serializer.data, template_name='rest_framework/api.html', status=status.HTTP_200_OK)
        return Response(serializer.data, template_name='rest_framework/api.html', status=status.HTTP_200_OK)

    def update(self, request, pk):
        print(pk)
        try:
            queryset = self.queryset.get(id=pk)
        except Exception as E:
            print(f"Error : {E}")
            return Response({"Message": "Error in saving the data."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TelevisionSerializer(queryset, request.data)
        if serializer.is_valid(raise_exception=True):
            print("Serializer is valid!")
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            queryset = self.queryset.get(id=pk)
        except Exception as E:
            print(f"Error : {E}")
            return Response({"Message": "Error in deleting the data."}, status=status.HTTP_400_BAD_REQUEST)
        print("Deleting the Resord")
        company_name = queryset.company
        queryset.delete()
        print("Deleted the Resord")
        return Response({"Success": f"Deletion completed successfully! - {company_name}"}, status=status.HTTP_200_OK)


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 200

class ModelMobileViewSet(viewsets.ModelViewSet):
    """
    Modelviewset is similar to Viewset but the only difference is that is
    In Viewset we need to write the below functions manually
        GET, POST, PUT, PATCH and DELETE
    But in ModelViewSets Everythin gwill be written we need to use the following
        queryset and serializer_class
    Rest of the things will be taken care by ModelViewset
    """
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    pagination_class = LargeResultsSetPagination
    permission_classes = [IsAuthenticated]
    # template_name = 'rest_framework/api.html'


    @action(detail=False, methods=['GET', "POST"])
    def no_of_mobile(self, request):
        if request.method=="POST":
            r_data = request.POST
            print("data : ", r_data)
            super().create(self, request)
        return Response({"Total No of mobiles ": Mobile.objects.all().count()}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET', 'POST'])
    def get_company(self, request, pk):
        try:
            if request.method == "POST":
                serializer_data = self.serializer_class(data=request.POST)
                if serializer_data.is_valid(raise_exception=True):
                    serializer_data.save()
                    return redirect('login')
                return Response(serializer_data.data, status=status.HTTP_200_OK)
        except Exception as E:
            print("Error creating : ", E)
            return Response({"Error Msg": "Error in creating."}, status=status.HTTP_200_OK)
        # if request.method=="POST":
        #     self.create(self, request)
        #     return Response({"Total No of mobiles ": Mobile.objects.all().count()}, status=status.HTTP_200_OK)
        try:
            mobile = Mobile.objects.select_related('brand').get(id=pk)
            # print(mobile.brand)
        except Mobile.DoesNotExist:
            return Response({"Error": "Mobile does not exist with the given id."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MobileSerializer(mobile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GenericTeleVisionViewSet(viewsets.GenericViewSet):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer


class MixinTeleVisionViewSet(viewsets.ViewSetMixin):
    pass


class ReadOnlyModelTeleVisionViewSet(viewsets.ReadOnlyModelViewSet):
    # queryset = Mobile.objects.all()
    # serializer_class = MobileSerializer
    pass

class CompanyMobileViewSet(viewsets.ModelViewSet):
    queryset = Mobile.objects.all()
    serializer_class = CompanyMobileSerializer