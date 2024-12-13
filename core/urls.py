from django.urls import path


from geo.urls import urlpatterns
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]