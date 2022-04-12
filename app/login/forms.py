from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur', widget=forms.TextInput(
        attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-grey-darker'}
    ))
    password = forms.CharField(max_length=63, label='Mot de passe', widget=forms.PasswordInput(
        attrs={'class': 'shadow appearance-none border border-red rounded w-full py-2 px-3 text-grey-darker mb-3'}
    ))