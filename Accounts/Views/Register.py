from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login
from Accounts.Forms.login import UserRegistrationForm


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')

        else:
            for error in list(form.error.values()):
                print(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="../Templates/Register.html",
        context={"form": form}
    )
