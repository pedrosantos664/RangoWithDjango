from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-input',
            'placeholder': _('seu@email.com')
        })
    )
    password = forms.CharField(
        label=_("Senha"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'current-password',
            'class': 'form-input',
            'placeholder': _('Sua senha')
        })
    )

    error_messages = {
        'invalid_login': _(
            "Por favor, insira um email e senha corretos. Note que ambos "
            "os campos diferenciam maiúsculas e minúsculas."
        ),
        'inactive': _("Esta conta está inativa."),
    }


class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': _('seu@email.com')
        }),
        help_text=_("Obrigatório. Insira um endereço de email válido.")
    )
    
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': _('Seu nome')
        }),
        max_length=30,
        help_text=_("Obrigatório. Máximo de 30 caracteres.")
    )

    password1 = forms.CharField(
        label=_("Senha"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': _('Crie uma senha segura')
        }),
        help_text=_(
            "Sua senha deve conter pelo menos 8 caracteres, "
            "não pode ser muito comum e não pode ser inteiramente numérica."
        )
    )
    
    password2 = forms.CharField(
        label=_("Confirmação de senha"),
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': _('Repita a mesma senha')
        }),
        help_text=_("Digite a mesma senha novamente para verificação.")
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("Este email já está em uso."))
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Para compatibilidade
        if commit:
            user.save()
        return user