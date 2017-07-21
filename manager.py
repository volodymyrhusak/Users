# -*- coding: utf-8 -*-
from mysql.connector import MySQLConnection, Error, errorcode
from my_models import User, Course


class UserManager():
    def __init__(self):
        try:
            self.conn = MySQLConnection(user='root',
                                        password='1',
                                        host='127.0.0.1',
                                        database='Users')
            self.cursor = self.conn.cursor()
            # print(self.cursor._connection)

        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.cursor.close()
            self.conn.close()

    def addUser(self, data):
        user = User()
        user.userName = data['userName']
        user.userEmail = data['userEmail']
        user.userPhone = data['userPhone']
        user.userMobilePhone = data['userMobilePhone']
        args = [user.userID, user.userName, user.userEmail,
                user.userPhone, user.userMobilePhone]
        self.cursor.callproc('add_user', args)
        self.closeDB()

    def getUsers(self, search, page, limit):
        result = []
        start = limit * (page - 1)
        stop = limit * page
        print([search, start, stop])
        args = [search, start, stop]
        self.cursor.callproc('select_users', args)
        for data in self.cursor.stored_results():
            for u in data.fetchall():
                user = User()
                user.usersID = u[0]
                user.userName = u[1]
                user.userEmail = u[2]
                user.userPhone = u[3]
                user.userMobilePhone = u[4]
                user.userStatus = u[5]
                user.courses = []
                if u[6]:
                    for c in u[6].split('***'):
                        course = Course()
                        course.courseName = c
                        user.courses.append(course)
                result.append(user)

        self.closeDB()
        return result

    def getUser(self, id):
        args = [id]
        self.cursor.callproc('select_user', args)
        for data in self.cursor.stored_results():
            # print(data.fetchall())
            u = data.fetchone()
            user = User()
            user.usersID = u[0]
            user.userName = u[1]
            user.userEmail = u[2]
            user.userPhone = u[3]
            user.userMobilePhone = u[4]
            user.userStatus = u[5]
            user.courses = []
            if u[6]:
                for c in u[6].split('***'):
                    course = Course()
                    course.courseName = c
                    user.courses.append(course)
        self.closeDB()
        return user

    def deleteUser(self, id):
        args = [id]
        self.cursor.callproc('delete_user', args)
        self.closeDB()

    def updUsers(self, user):
        args = [user.usersID, user.userEmail, user.userPhone, user.userMobilePhone, user.userStatus]
        self.cursor.callproc('update_user', args)
        self.cursor.callproc('delete_course', [user.userID])
        if len(user.courses) <= 5:
            map(self.addCourse, user.courses)
        self.closeDB()

    def addCourse(self, course):
        self.cursor.callproc('add_course', [course.coursesID])
        self.closeDB()

    def closeDB(self):
        self.cursor.close()
        self.conn.close()


class CourseManager():
    def __init__(self):
        try:
            self.conn = MySQLConnection(user='root',
                                        password='1',
                                        host='127.0.0.1',
                                        database='Users')
            self.cursor = self.conn.cursor()
            # print(self.cursor._connection)

        except Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            self.cursor.close()
            self.conn.close()

    def closeDB(self):
        self.cursor.close()
        self.conn.close()

    def getCourse(self):
        result = []
        self.cursor.callproc('select_course')
        for data in self.cursor.stored_results():
            for c in data.fetchall():
                course = Course()
                course.id = c[0]
                course.courseName = c[1]
                result.append(course)

        self.closeDB()
        return result
