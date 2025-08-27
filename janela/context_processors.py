
def auth_status(request):  # ← Mude o nome para auth_status
    """
    Context processor para verificar autenticação
    """
    return {
        'usuario_autenticado': request.user.is_authenticated,
        'usuario_nome': request.user.first_name if request.user.is_authenticated else None,
    }