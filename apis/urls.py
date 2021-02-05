# basic URL Configurations 
from django.urls import include, path 

# import routers 
from rest_framework import routers 

# importing everything from views
from apis.views import *

#defining the router
router = routers.DefaultRouter()

# define the router path and viewset to be used 
router.register(r'sales', SalesViewSet)
router.register(r'purchase',PurchaseViewSet) 
  
# specify URL Path for rest_framework 
urlpatterns = [ 
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')), 
] 