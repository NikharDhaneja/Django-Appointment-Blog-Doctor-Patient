from django.shortcuts import render, redirect
from .forms import RegistrationForm, AddressForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views import View
from .models import User
from .forms import LoginForm

class HomepageView(View):
    def get(self, request):
        return render (request=request, template_name="homepage.html")

class RegistrationView(View):

    def get(self, request):
        form1 = RegistrationForm()
        form2 = AddressForm()
        return render (request=request, template_name="registration.html", context={"registration_form":form1, "address_form":form2})

    def post(self, request):
        form1 = RegistrationForm(request.POST, request.FILES)
        form2 = AddressForm(request.POST)

        if all((form1.is_valid(), form2.is_valid())):
            user = form1.save(commit = False)
            if form1.cleaned_data['role'] == 'doctor':
                print(user.is_doctor)
                user.is_doctor = True
            elif form1.cleaned_data['role'] == 'patient':
                user.is_patient = True

            address = form2.save(commit = False)
            address.user = user
            user.save()
            address.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("account:dashboard_view")

        messages.error(request, f'Unsuccessful registration.')
        return render (request=request, template_name="registration.html", context={"registration_form":form1, "address_form":form2})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request=request, template_name="login.html", context={"login_form":form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                messages.success(request, "Login successful." )
                return redirect("blog:blog_list_view")
        else:
            messages.error(request,"Invalid username or password.")
            return render(request=request, template_name="login.html", context={"login_form":form})


class DashboardView(View):

    def get(self, request):
        info = User.objects.get(username = request.user.username)
        return render (request=request, template_name="dashboard.html", context={"user_info":info})
