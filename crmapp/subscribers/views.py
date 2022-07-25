from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Subscriber
from .forms import SubscriberForm
from django.forms.forms import NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.conf import settings
import stripe

sub = Subscriber()

def subscriber_new(request, template='subscribers/subscriber_new.html'):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Unpack form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Create the User record
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            # Create Subscriber Record
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            sub = Subscriber(address_one=address_one, address_two=address_two,
                             city=city, state=state, user_rec=user)
            sub.save()
            # Process payment (via Stripe)
            # stripe error handler and credit card debit processor
            try:
                sub.charge(request, email, fee)
            except stripe.error.StripeError as e:
                #handle errors
                form._errors[NON_FIELD_ERRORS] = form.error_class([e.args[0]])
                return render(request, template, {'form': form,
                     'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY})
            # Auto login the user
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                if authenticated_user.is_active:
                    login(request, authenticated_user)
                    return HttpResponseRedirect(reverse('account_list'))
                return HttpResponseRedirect(reverse(django.contrib.auth.views.login))
            return HttpResponseRedirect(reverse('signup'))
    else:
        form = SubscriberForm()

    return render(request, template, {'form':form,
                 'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY})
