from .views import RequestVerificationViewSet

# Rest Framework
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'request-verification', RequestVerificationViewSet, base_name='request_verification')

