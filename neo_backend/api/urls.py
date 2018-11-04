from .views import RequestVerificationViewSet, ConfirmVerificationViewSet

# Rest Framework
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'request-verification', RequestVerificationViewSet, base_name='request_verification')
router.register(r'confirm-verification', ConfirmVerificationViewSet, base_name='confirm_verification')

