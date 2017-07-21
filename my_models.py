# -*- coding: utf-8 -*-
from schematics.models import Model
from schematics.types import StringType, EmailType, BooleanType, IntType, ListType, ModelType
from my_types import PhoneType


class Course(Model):
    id = IntType()
    courseName = StringType()


class User(Model):
    usersID = IntType()
    userName = StringType(required=True)
    userEmail = EmailType(required=True)
    userPhone = PhoneType(default=None)
    userMobilePhone = PhoneType(default=None)
    userStatus = BooleanType(default=False)
    courses = ListType(ModelType(Course))


class Phone(Model):
    p = PhoneType()


if __name__ == '__main__':
    phone = Phone()
    phone.p = '123'
    phone.p.validate()
