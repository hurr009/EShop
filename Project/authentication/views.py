from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View, generic
from django.urls import reverse
from django.contrib.auth import mixins, logout, login, authenticate


from .forms import UserRegistrationForm, UserLoginForm


class IndexView(generic.TemplateView):
    template_name = 'authentication/index.html'


class SignUpView(View):
    form_class = UserRegistrationForm
    template_name = 'authentication/signup.html'

    def get(self, request):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        
        context = {'form': self.form_class}
        return render(request, self.template_name, context)

class LoginView(View):
    returnUrl = None
    form_class = UserLoginForm

    def get(self, request):
        LoginView.returnUrl = request.GET.get('return_url')
        context = {'form': self.form_class}
        return render(request, 'authentication/login.html', context)

    def post(self, request):
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if LoginView.returnUrl is not None:
                return HttpResponseRedirect(LoginView.returnUrl)
            else:
                return redirect('index')
        else:
            return redirect(reverse('login'))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))