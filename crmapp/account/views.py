from django.shortcuts import render
from django.views.generic import ListView, createView
# Create your views here.

class AccoutList(ListView):
    template_name = 'account/account_list.html'
