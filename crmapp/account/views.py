from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Account
from django.views.generic import ListView, CreateView, DetailView, UpdateView
# Create your views here.

class AccountList(ListView):
    template_name = 'account/account_list.html'
    model = Account
    paginate_by = 2
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account')
        except KeyError:
            a = None
        if a:
            accounts_list = Account.objects.filter(name__icontains= a,
                            owner=self.request.user)
        else:
            accounts_list = Account.objects.filter(owner=self.request.user)
        return accounts_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)


class AccountDetail(DetailView):
    model = Account


class AccountCreate(CreateView):
    model = Account

class AccountEdit(UpdateView):
    model = Account
    fields = ('name', 'desc')
