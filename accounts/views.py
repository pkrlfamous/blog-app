from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# here UserCreationForm is the form class which
# django provides us to create new user

# subclassing generic class-based view CreateView
# in our SignUPView class.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# success_url redirect user to the login page upon
# successful registration.

# we r using reverse_lazy fn instead of reverse
# cause for all generic class_based views the urls are not loaded when 
# the file is imported, so we have to use the lazy form of reverse to 
# load them later when they're available. 