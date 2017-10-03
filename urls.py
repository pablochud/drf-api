from rest_framework.routers import DefaultRouter
from retail.views import ChainViewSet, StoreViewSet, EmployeeViewSet, login
from django.conf.urls import patterns, url, include
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(prefix='chains', viewset=ChainViewSet)
router.register(prefix='stores', viewset=StoreViewSet)
router.register(prefix='employees', viewset=EmployeeViewSet)

#urlpatterns = router.urls

urlpatterns = [
      url(r'^', include(router.urls)),
      url(r'^jwt-auth/', obtain_jwt_token),
      url(r'^login/', login),
]
