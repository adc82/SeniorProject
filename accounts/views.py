from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View

from .forms import UserCreationForm
from .models import LinkAccountToEcho


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


class HomePageView(View):
    template_name = 'home.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class ItWorkedView(View):
    template_name = 'itworked.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class CreateAccountView(View):
    template_name = 'create_account.html'
    form = UserCreationForm

    def get(self, request):
        context = {}
        context['form'] = self.form
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:it_worked'))

        context = {}
        context['form'] = self.form
        return render(request, self.template_name, context)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:it_worked'))

        return render(request, self.template_name, {})


class LinkEchoToUserView(View):
    template_name = 'link_account.html'

    @method_decorator(login_required)
    def get(self, request):
        link = LinkAccountToEcho.objects.create(user=request.user)
        context = {}
        context['passcode'] = link.passcode
        return render(request, self.template_name, context)
