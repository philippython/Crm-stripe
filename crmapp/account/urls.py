from django.conf.urls import url, include
from .views import AccountList, AccountDetail, AccountCreate, AccountEdit

urlpatterns = [
        url(r'^list/$', AccountList.as_view(), name='account_list'),
        url(r'^create/$', AccountCreate.as_view(), name='account_create'),
        url(r'^detail/(?P<pk>[\w-]+)/', AccountDetail.as_view(), name='account_detail'),
        url(r'^edit/(?P<pk>[\w-]+)/', AccountEdit.as_view(), name='account_edit')
]
