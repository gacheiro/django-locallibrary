# Django Local Library Tutorial

Tutorial de django da Mozilla Developer Network. É um app para gerenciar uma biblioteca. Ao longo do tutorial, fiz algumas mudanças como
adicionar fixtures, por exemplo. O tutorial pode ser encontrado (aqui)[https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django].

## Instalando

O ideal é criar um ambiente virtual antes de instalar as dependências. Depois:

```
# instala as dependências
pip install -r requirements.txt

# procura por alterações nos modelos e cria o banco de dados
python manage.py makemigrations
python manage.py migrate

# popula o banco de dados com as fixtures
python manage.py loaddata authors.yaml genres.yaml books.yaml bookinstances.yaml

# cria um superusuário para acessar /admin
python manage.py createsuperuser

# agora é só rodar o app
python manage.py runserver
```
