from services.conexao import conectar
import bcrypt
import getpass

def input_senha_mascarada():
    """
    Solicita uma senha ao usuário, mascarando a entrada.
    """
    try:
        senha = getpass.getpass("Digite sua senha: ")
        # Você pode adicionar lógica de validação aqui, se necessário.
        # Por exemplo, verificar comprimento mínimo, caracteres especiais, etc.
        print("\nSenha digitada (mascarada na entrada):", "*" * len(senha))
        return senha
    except Exception as e:
        print(f"Erro ao obter a senha: {e}")
        return None

# Exemplo de uso:
minha_senha = input_senha_mascarada()

if minha_senha:
    print(f"A senha que você digitou foi: '{minha_senha}'")
    # Em um aplicativo real, você não exibiria a senha dessa forma.
    # Em vez disso, a usaria para autenticação, hash, etc.

def criar_usuario(nome, email, senha):
    # Criptografa a senha para guardar segura no banco
    senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

    conn = conectar()
    cursor = conn.cursor()

    # Insere usuário no banco
    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
        (nome, email, senha_hash)
    )
    conn.commit()
    cursor.close()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    # Busca todos os usuários, sem mostrar senha
    cursor.execute("SELECT id, nome, email FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()
    return usuarios

def deletar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()

    # Deleta usuário pelo id
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
    conn.commit()

    cursor.close()
    conn.close()

def buscar_usuario_por_email(email):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)

    # Busca usuário pelo email para login
    cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    cursor.close()
    conn.close()
    return usuario

def validar_senha(senha_digitada, senha_hash):
    # Compara senha digitada com senha criptografada do banco
    return bcrypt.checkpw(senha_digitada.encode(), senha_hash.encode())
