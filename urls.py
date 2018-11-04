from django.contrib import admin
from django.conf.urls import url, include

def testing_500_error(request):
    """
    Testing view to generate a 500 server error
    :param request:
    :return:
    """
    raise ValueError('This is a test exception raised on purpose, for testing exception handling.')



urlpatterns = [
    url('api/', include('api.urls')),
    url(r'^testing-500-error$', testing_500_error, name='testing_500_error'),
]
