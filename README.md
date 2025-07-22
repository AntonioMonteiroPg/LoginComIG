# 🔐 Sistema de Login com Interface Gráfica (Tkinter + MySQL)

Bem-vindo ao **LoginApp**, um sistema completo de autenticação de usuários com interface gráfica feita em **Tkinter**, banco de dados em **MySQL**, e segurança de senhas com **bcrypt**. Um projeto simples, funcional e educativo para entender como construir uma aplicação real com separação entre camadas (MVC).

---

## 🚀 Funcionalidades

✅ Interface gráfica intuitiva com Tkinter  
✅ Cadastro de novos usuários  
✅ Autenticação segura com senhas criptografadas (bcrypt)  
✅ Listagem de usuários cadastrados (sem exibir senhas!)  
✅ Exclusão de usuários  
✅ Gerenciamento de sessão  
✅ Atalhos de teclado (Enter para login e salvar usuário)  
✅ Protegido contra acesso direto pelo terminal

---

## 🧱 Estrutura do Projeto

projeto/
│
├── controller/
│ └── login_controller.py
│
├── model/
│ └── usuario_model.py
│
├── services/
│ └── conexao.py
│
├── main.py ← Arquivo principal (interface Tkinter)
└── README.md

yaml
Copiar
Editar

- **controller**: Lógica de controle de login e sessão  
- **model**: Acesso ao banco de dados e lógica de usuário  
- **services**: Conexão com o banco (MySQL)  
- **main.py**: Interface gráfica e execução principal  

---

## 🛠️ Tecnologias Usadas

- **Python 3.x**
- **Tkinter** – Interface gráfica nativa
- **MySQL** – Banco de dados relacional
- **bcrypt** – Criptografia segura de senhas
- **VS Code** – Ambiente de desenvolvimento

---

## 🔒 Segurança

Senhas dos usuários são armazenadas usando **bcrypt**, um dos algoritmos mais seguros para armazenamento de senhas. Comparações de login são feitas via hash, protegendo seus dados mesmo em caso de acesso ao banco.

---

## ⚡ Atalhos de Teclado

- **Enter na tela de login** = Fazer login
- **Enter na tela de criar usuário** = Salvar usuário

---

## 🧪 Como rodar o projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/login-tkinter-app.git
   cd login-tkinter-app
Instale os requisitos (se necessário):

bash
Copiar
Editar
pip install bcrypt mysql-connector-python
Configure a conexão com seu MySQL no arquivo:

bash
Copiar
Editar
services/conexao.py
Execute o sistema:

bash
Copiar
Editar
python main.py
💡 Para esconder o terminal no Windows, use pythonw main.py ou salve como .pyw.

📷 Capturas de Tela
(Adicione aqui screenshots do sistema rodando se quiser melhorar a apresentação!)

🧠 Aprendizados
Este projeto demonstra na prática:

Separação entre interface, controle e modelo

Como proteger senhas de forma segura

Uso profissional do Tkinter

Integração Python + MySQL

Boas práticas de UX com atalhos e centralização de janelas

🧑‍💻 Autor
Desenvolvido com 💻 por [Seu Nome]
📧 contato: [seuemail@exemplo.com]
🌐 GitHub: https://github.com/seu-usuario

📜 Licença
Este projeto está licenciado sob a MIT License. Sinta-se livre para usar, estudar e modificar.

"Segurança e usabilidade podem andar de mãos dadas — e com Tkinter, até com estilo!"

yaml
Copiar
Editar

---

Se quiser, posso gerar versões com badges, emojis de seção ou adaptá-lo para um portfólio mais formal 