from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Account
from django.views.generic import ListView, CreateView
# Create your views here.

class AccountList(ListView):
    template_name = 'account/account_list.html'
    model = Account
    paginate_by = 10
    context_object_name = 'accounts'

    def get_queryset(self):
        accounts_list = Account.objects.filter(owner=self.request.user)
        return accounts_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)
