from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response


class RequestVerificationViewSet(viewsets.ViewSet):
    """
    """

    # its better to use the ViewSet instead of views.API: https://www.stackoverflow.com/questions/30389248

    def list(self, request, format=None):
        """
        List view doesnt make 100% sense because we only have 1 object, but its convenient
        """
        user = self.request.user
        return Response(
            {}
        )

