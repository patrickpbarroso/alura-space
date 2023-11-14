from django import forms

class LoginForms(forms.Form):
    # Formulário com dados de login de usuário
    nome_login=forms.CharField(
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Ana Santos"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):
    # Formulário com dados de cadastro de usuário
    nome_cadastro=forms.CharField(
        label="Nome de cadastro",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Ana Santos"
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: ana.santos@email.com"
            }
        )
    )
    senha_1=forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    senha_2=forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )