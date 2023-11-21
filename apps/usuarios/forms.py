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
                "placeholder": "Ex.: ana.santos"
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
        label="Nome de usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: ana.santos"
            }
        )
    )
    primeiro_nome=forms.CharField(
        label="Primeiro nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Ana"
            }
        )
    )

    sobrenome=forms.CharField(
        label="Sobrenome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"Ex.: Santos"
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

    def clean_nome_cadastro(self):
        # Método para validar que o nome de usuário não tem espaços
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("O nome de usuário não pode conter espaços")
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("As senhas devem ser iguais")
            else:
                return senha_2