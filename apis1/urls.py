from django.urls import include, path

from rest_framework import routers
from apis1.views import (SalesTableViewSet, 
                         PurchaseTableViewSet, 
                         ListTableViewSet,
                         PurchaseRequisitionTableViewSet,
                         Accept_Reject_Table_ViewSet,
                         )

router = routers.DefaultRouter()
router.register('sale',SalesTableViewSet,basename='sale')
router.register('pur',PurchaseTableViewSet,basename='pur')
router.register('content',ListTableViewSet,basename='content')
router.register('pr',PurchaseRequisitionTableViewSet, basename='pr')
router.register('n', Accept_Reject_Table_ViewSet, basename='n')


# specify URL Path for rest_framework 
urlpatterns = [ 
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')), 
] 
