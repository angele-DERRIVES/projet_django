from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label="Username",
                               max_length=100)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())

    class Meta:
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")

    def clean_first_name(self):
        if self.cleaned_data['first_name'] == '':
            self.add_error('first_name', "First name can't be empty !")
        return self.cleaned_data['first_name']
