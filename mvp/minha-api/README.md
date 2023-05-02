# MVP

Estre projeto se trata do primeiro MVP da Disciplina **Desenvolvimento full Stack Básico** PUC-rio EAD.

O projeto se trata de uma lista de materia escolar.

------

# Como executar
 
 Primeiro é necessário ativar o ambiente virtual, no terminal do Visual Studio Code  digite
 o que está a baixo para criar o ambiente virtual:
 
 ```
  python -m venv venv
 ```
  
 Após a criação do ambiente virtual digite o que está a baixo para ativá-lo:
  
 ```
  venv/Scripts/Activate
 ```
 
 Depois que estiver com o ambiente virtual atiado, baixe o arquivo requirements.txt com o seguinte comando:
 
  ```
  pip install -r requirements.txt
 ```
 
 Se não consegguir com o comando acima, baixe todas manualmente com o comando 
  
 ```
 pip install 'nome da lib abaixo'
 ```
 ```
aniso8601
attrs
click
Flask
Flask-Cors
flask-openapi3
flask-restx
Flask-SQLAlchemy
greenlet
gunicorn
importlib-metadata
itsdangerous
Jinja2
jsonschema
MarkupSafe
nose2
pydantic
pyrsistent
pytz
six
SQLAlchemy
SQLAlchemy-Utils
typing_extensions
Werkzeug
zipp
Flask
sqlalchemy
sqlalchemy.orm
flask-openapi3
flask-restful
flask-swagger-ui
flask-swagger-ui

```
Depois que fizer os passos acima, rode o app.py e acesse no browser:

````
http://127.0.0.1:5000
```
