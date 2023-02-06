from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse

from Registration.Forms.register import RegisterForm


class RegisterFormView(generic.FormView):
    template_name = 'User/register_form.html'
    form_class = RegisterForm

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        password2 = form.cleaned_data['password2']

        try:
            User.objects.create_user(
                username=username, email=email, password=password
            )

        except Exception as e:
            form.add_error(None, "Unexpected error")
            messages.error(self.request, f"Your form doesn\'t seem valid")
            return super().form_invalid(form)

        messages.success(self.request, f"Your account have been created !")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
