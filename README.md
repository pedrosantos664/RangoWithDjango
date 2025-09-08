# 📚 RangoWithDjango

Aplicação web desenvolvida com **Django** durante estudos práticos de desenvolvimento web.  
O projeto segue o padrão **Model-View-Template (MVT)** do Django e implementa funcionalidades de cadastro, autenticação e gerenciamento de conteúdos.

---

## 🚀 Funcionalidades

- Cadastro e login de usuários.
- Criação e gerenciamento de categorias.
- Cadastro de páginas associadas a cada categoria.
- Interface amigável utilizando templates com herança.
- Painel administrativo do Django para gerenciar os dados.
- Autenticação e controle de acesso a funcionalidades restritas.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.x, Django
- **Banco de Dados:** SQLite (desenvolvimento local)
- **Frontend:** HTML5, CSS3, Bootstrap (templates)
- **Outros:** Django Admin, autenticação de usuários

---

## 📂 Estrutura do Projeto

RangoWithDjango/
│
├── rango/ # Aplicação principal
│ ├── models.py # Definição das entidades (Category, Page, etc.)
│ ├── views.py # Lógica das views
│ ├── urls.py # Rotas da aplicação
│ ├── templates/ # Templates com herança (base.html, index.html, etc.)
│ └── forms.py # Formulários Django (ModelForm)
│
├── RangoWithDjango/ # Configurações do projeto (settings, urls, wsgi)
├── manage.py # Comando principal para executar o projeto
└── requirements.txt # Dependências do projeto


---

## ⚡ Como Executar Localmente

1. **Clonar o repositório**
   ```bash
   git clone https://github.com/pedrosantos664/RangoWithDjango.git
   cd RangoWithDjango


2. **Criar e ativar ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows


3. **Instalar dependências**
   ```bash
   pip install -r requirements.txt


4. **Aplicar migrações**
   ```bash
   python manage.py migrate


5. **Criar superusuário (para acessar o admin)**
   ```bash
   python manage.py createsuperuser


6. **Executar o servidor**
   ```bash
   python manage.py runserver


7. **Acessar no navegador**
   ```bash
   Aplicação: 127.0.0.1:8000/janela/
   
   Admin:127.0.0.1:8000/admin
'

## 📖 Aprendizados com o Projeto
     
      Estrutura e funcionamento do framework Django.
       
      Criação de models, views, templates e formulários.
      
      Autenticação e autorização de usuários.
      
      Integração de templates com Bootstrap.
      
      Boas práticas de organização de projetos em Python.

## ✨ Autor

   Pedro Batista





