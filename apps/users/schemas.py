# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Email, Str


class UserRegistrationSchema(Schema):
    full_name = Str(required=True, error_messages={'required': 'Campo obrigatório'})
    email = Email(required=True, error_messages={'required': 'Campo obrigatório'})
    password = Str(required=True, error_messages={'required': 'Campo obrigatório'})


class UserSchema(Schema):
    full_name = Str(required=True, error_messages={'required': 'Campo obrigatório'})
    email = Email(required=True, error_messages={'required': 'Campo obrigatório'})