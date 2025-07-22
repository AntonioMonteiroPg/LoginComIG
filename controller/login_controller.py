from model.usuario_model import buscar_usuario_por_email, validar_senha

sessao = {}  # Dicionário que vai guardar os dados da sessão do usuário logado

def login(email, senha):
    usuario = buscar_usuario_por_email(email)
    if not usuario:
        return False, "Usuário não encontrado."

    if not validar_senha(senha, usuario['senha']):
        return False, "Senha incorreta."

    # Guarda no dicionário sessao os dados do usuário logado
    sessao['usuario'] = {'id': usuario['id'], 'nome': usuario['nome']}
    return True, f"Bem-vindo, {usuario['nome']}!"
