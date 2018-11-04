from .views import RequestVerificationViewSet, ConfirmVerificationViewSet, VerificationStatusViewSet, ImageHashesViewSet

# Rest Framework
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'request-verification', RequestVerificationViewSet, base_name='request_verification')
router.register(r'confirm-verification', ConfirmVerificationViewSet, base_name='confirm_verification')
router.register(r'verificaton-status', VerificationStatusViewSet, base_name='verification_status')
router.register(r'get-verifications-for-address', ImageHashesViewSet, base_name='get_verifications')

