from wtforms import Form
from wtforms import StringField, TextField
from wtforms import validators.lenght
from wtforms.fields.html5 import EmailField

class CommentForm(Form):
    username = StringField('username')
    email = EmailField('Correio Eletronico')
    comment = TextField('Comentario')
   
#class LoginForm(Form):
    
class CreateForm(Form):
    username = TextField('Username',
                [
                  validators.Required(message = 'O username é valido'),
                  validators.lenght(min=4, max=50, message= 'Digite um r.a. valido'),
                ])
    email = Email('Correio Eletronico',
                [ validators.Required(message = 'O email é valido' ),
                  validators.Email(message= 'Digite um email valido'),
                  validators.lenght(min=4, max=50, message= 'Digite um email valido'),
                ])
    password = PasswordField('Password', [validatros.Required(message = 'A senha é valida' )])                
    