from rest_framework import serializers
from django.utils.translation import gettext as _
from api.serializers import CustomSerializer


from rest_framework import serializers


class VerificationRequestSerializer(serializers.Serializer):
    """
    create_verification_request(sender_address, sender_address_wif, source_address):
    """
    sender_address = serializers.CharField()
    sender_address_wif = serializers.CharField()
    source_address = serializers.CharField()


class VerificationConfirmationSerializer(serializers.Serializer):
    """
    confirm_verification_request(sender_address, sender_address_wif, target_address):
    """
    sender_address = serializers.CharField()
    sender_address_wif = serializers.CharField()
    target_address = serializers.CharField()
    image_hash = serializers.CharField()


class VerificationStatusSerializer(serializers.Serializer):
    """
    get_verification_request_status(source_address, target_address):
    """
    source_address = serializers.CharField()
    target_address = serializers.CharField()


class TargetAddressSerializer(serializers.Serializer):
    """
    get_image_hashes(target_address)
    """
    target_address = serializers.CharField()

