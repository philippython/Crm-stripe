from django.conf.urls import url, include
from .views import AccoutList

urlpatterns = [
        url(r'^list/$', AccountList.as_view(), name='account_list')
]
