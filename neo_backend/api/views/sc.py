from ...helpers import get_verification_request_status, get_image_hashes, create_verification_request, confirm_verification_request
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from ..serializers import VerificationConfirmationSerializer, VerificationRequestSerializer
from rest_framework import viewsets, permissions, mixins, status


class RequestVerificationViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    create_verification_request(sender_address, sender_address_wif, source_address):
    """

    renderer_classes = [
        # the only order in which csv headers work and the browsable api returns pretty json
        JSONRenderer,
        BrowsableAPIRenderer,
    ]

    authentication_classes = []

    # DRY Permissions dont apply here as this is not a Model View Set, but a custom one.
    permission_classes = (
        permissions.AllowAny,
    )

    serializer_class = VerificationRequestSerializer

    # its better to use the ViewSet instead of views.API: https://www.stackoverflow.com/questions/30389248

    def create(self, request, *args, **kwargs):
        """

        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sender_address = serializer.data.get('sender_address')
        sender_address_wif = serializer.data.get('sender_address_wif')
        source_address = serializer.data.get('source_address')

        try:
            create_verification_request(sender_address, sender_address_wif, source_address)
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': str(e),
                }
            )

        return Response(
            {
                'status': 'success',
            }
        )


class ConfirmVerificationViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    """
    confirm_verification_request(sender_address, sender_address_wif, target_address, image_hash):
    """

    # its better to use the ViewSet instead of views.API: https://www.stackoverflow.com/questions/30389248

    renderer_classes = [
        # the only order in which csv headers work and the browsable api returns pretty json
        JSONRenderer,
        BrowsableAPIRenderer,
    ]

    authentication_classes = []

    # DRY Permissions dont apply here as this is not a Model View Set, but a custom one.
    permission_classes = (
        permissions.AllowAny,
    )

    serializer_class = VerificationConfirmationSerializer

    def create(self, request, *args, **kwargs):
        """

        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sender_address = serializer.data.get('sender_address')
        sender_address_wif = serializer.data.get('sender_address_wif')
        target_address = serializer.data.get('target_address')
        image_hash = serializer.data.get('image_hash')

        try:
            confirm_verification_request(sender_address, sender_address_wif, target_address, image_hash)
        except Exception as e:
            return Response(
                {
                    'status': 'error',
                    'message': str(e),
                }
            )

        return Response(
            {
                'status': 'success',
            }
        )
