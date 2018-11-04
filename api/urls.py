
from django.conf.urls import url, include
from api import routers
from neo_backend.api.urls import router as neo_backend_router


# Rest Framework
router = routers.DefaultRouter()
router.extend(neo_backend_router)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
