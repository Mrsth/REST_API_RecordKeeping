from django.urls import include, path

from rest_framework import routers
from apis1.views import SalesTableViewSet, PurchaseTableViewSet, ListTableViewSet

router = routers.DefaultRouter()
router.register('sale',SalesTableViewSet,basename='sale')
router.register('pur',PurchaseTableViewSet,basename='pur')
router.register('content',ListTableViewSet,basename='content')

# specify URL Path for rest_framework 
urlpatterns = [ 
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')), 
] 
