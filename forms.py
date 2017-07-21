# -*- coding: utf-8 -*-
from manager import UserManager
from my_models import User, Course
from schematics.exceptions import ValidationError, DataError


class ChangeUserForm():
    def __init__(self, form, usersID):
        self.user = User()
        self.user.userID = usersID
        self.user.userName = form.get('userName', 'name')
        self.user.userEmail = form['userEmail']
        self.user.userPhone = form['userPhone']
        self.user.userMobilePhone = form['userMobilePhone']
        self.user.userStatus = form['userStatus']
        # self.user.courses = form['courses']

    def validate(self):
        try:
            self.user.validate()
            return 'save'
        except (ValidationError, DataError) as err:
            return err

    def save(self):
        userManager = UserManager()
        userManager.updUsers(self.user)


class CreateUserForm():
    def __init__(self, form):
        self.user = User()
        self.user.userName = form['userName']
        self.user.userEmail = form['userEmail']
        self.user.userPhone = form['userPhone']
        self.user.userMobilePhone = form['userMobilePhone']
        self.user.userStatus = form['userStatus']

    def validate(self):
        try:
            self.user.validate()
            return 'save'
        except (ValidationError, DataError) as err:
            return err

    def save(self):
        userManager = UserManager()
        userManager.addUser(self.user)
