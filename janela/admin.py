# janela/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()

# Desregistra o admin padrão (se necessário)
admin.site.unregister(User)

# Registra com customização
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'is_staff')
    # Adicione outras customizações aqui