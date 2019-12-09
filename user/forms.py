from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanici Adi")
    password=forms.CharField(label="Parola",widget=forms.PasswordInput)
    

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanici Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm= forms.CharField(max_length=20, label="Parolayi dogrula", widget=forms.PasswordInput)
    def clean(self): #password ve confirm alanimiz eyni olarsa formumuz submit edilecek
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        values={
            "username": username,
            "password": password,
            "confirm": confirm
        }
        return values

    