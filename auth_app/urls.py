from django.urls import path
from . import (views, drf_views, viewsets_views)

from rest_framework.routers import DefaultRouter, SimpleRouter

routers = DefaultRouter()
routers.register('custom-television', viewsets_views.NormalViewsetTeleVisionViewSet),
routers.register('model-mobiles', viewsets_views.ModelMobileViewSet),
# routers.register('readonly-mobile', viewsets_views.ReadOnlyModelTeleVisionViewSet)
# routers.register('generic-mobile', viewsets_views.GenericTeleVisionViewSet),
# routers.register('company-mobile', viewsets_views.CompanyMobileViewSet),

urlpatterns = routers.urls

urlpatterns += [
	path('login/', views.login, name ='login'),
	path('create_person/', views.create_person, name ='create_person'),
	# path('hello/', views.hello, name ='hello'),



	path("tv-list/", drf_views.TVListView.as_view(), name ="tv_list")






]
