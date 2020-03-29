from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

class RegisterView(View):

    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    # if the request is a GET request
    def get(self, request):
        # create a blank form
        registration_form = self.form_class()
        return render(request, self.template_name, {'form': registration_form, 'title': 'Register'})

    # if the request is a POST request
    def post(self, request):
        registration_form = self.form_class(request.POST)
        # check if the form is valid
        if registration_form.is_valid():
            registration_form.save()
            return redirect('accounts:login')
        else:
            return render(request,'accounts/register.html', {'form': registration_form, 'title': 'Register'})

#class IndexView(View):
#
#    template_name = 'accounts/index.html'
#
#    def get(self, request):
#        return render(request, self.template_name, {'title': request.user.username})
