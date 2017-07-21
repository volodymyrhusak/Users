DELIMITER $$
USE Users$$

drop procedure if exists add_user$$
CREATE PROCEDURE add_user(
    IN userName VARCHAR(30),
    IN userEmail VARCHAR(30),
    IN userPhone VARCHAR(30),
    IN userMobilePhone VARCHAR(30),
    IN userStatus INT(1)
    )
BEGIN
    INSERT INTO Users.Users (Users.userName, Users.userEmail, Users.userPhone, Users.userMobilePhone, Users.userStatus)
    VALUES (userName, userEmail,userPhone,userMobilePhone,userStatus);
COMMIT;
END$$


drop procedure if exists delete_course$$
CREATE PROCEDURE delete_course(
    IN userID INT)
BEGIN
    DELETE FROM Users.CourseUsers WHERE Users.CourseUsers.usersID=userID;
COMMIT;
END$$

drop procedure if exists add_course$$
CREATE PROCEDURE add_course(
    IN userID INT,
    IN courseID INT)
BEGIN
    INSERT INTO Users.CourseUsers (CourseUsers.users,CourseUsers.course) VALUES (userID,courseID);
COMMIT;
END$$


drop procedure if exists update_user$$
CREATE PROCEDURE update_user(
    IN id INT,
    IN userEmail VARCHAR(30),
    IN userPhone VARCHAR(30),
    IN userMobilePhone VARCHAR(30),
    IN userStatus INT(1))
BEGIN
    UPDATE Users.Users SET
	Users.userEmail =  CASE WHEN Users.userEmail != userEmail THEN userEmail ELSE Users.userEmail END,
    Users.userPhone = CASE WHEN Users.userPhone != userPhone THEN userPhone ELSE Users.userPhone END,
    Users.userMobilePhone = CASE WHEN Users.userMobilePhone != userMobilePhone THEN userMobilePhone ELSE userMobilePhone END,
    Users.userStatus = CASE WHEN Users.userStatus!= userStatus THEN userStatus ELSE Users.userStatus END
    WHERE Users.Users.usersID=id;
    COMMIT;
END$$


drop procedure if exists delete_user$$
CREATE PROCEDURE delete_user(
    IN id INT)
BEGIN
    DELETE FROM Users.Users WHERE Users.Users.usersID=id;
    COMMIT;
END$$

drop procedure if exists select_user$$
CREATE PROCEDURE select_user(
    IN id VARCHAR(30))
BEGIN
    SELECT
         Users.usersID,
         Users.userName,
         Users.userEmail,
         Users.userPhone,
         Users.userMobilePhone,
         Users.userStatus,
         GROUP_CONCAT(Courses.courseName ORDER BY Courses.courseName SEPARATOR '***')


    FROM Users.Users
	LEFT JOIN Users.CourseUsers ON CourseUsers.users = Users.usersID
    LEFT JOIN Users.Courses ON Courses.courseID = CourseUsers.course
    WHERE Users.usersID = id
	GROUP BY Users.usersID, Users.userName,Users.userEmail, Users.userPhone, Users.userMobilePhone, Users.userStatus;
END$$

CREATE PROCEDURE create_tables ()
BEGIN
CREATE TABLE Users(
    usersID INT NOT NULL AUTO_INCREMENT,
    userName  VARCHAR(30) NOT NULL,
    userEmail  VARCHAR(30) NOT NULL,
    userPhone  VARCHAR(30),
    userMobilePhone VARCHAR(30),
    userStatus INT(1) NOT NULL,
    CONSTRAINT PRIMARY KEY (usersID)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
 COMMIT;

CREATE TABLE Courses(
    courseID INT NOT NULL AUTO_INCREMENT,
    courseName VARCHAR(30) NOT NULL,
    PRIMARY KEY (courseID)
) CHARACTER SET utf8 COLLATE utf8_general_ci;
 COMMIT;

CREATE TABLE CourseUsers (
    users INT NOT NULL,
    course INT NOT NULL,
    CONSTRAINT PRIMARY KEY (users, course),
    CONSTRAINT Constr_CourseUsers_Users_fk FOREIGN KEY(users)
        REFERENCES Users(usersID)
        ON DELETE CASCADE,
    CONSTRAINT Constr_CourseUsers_Course_fk
        FOREIGN KEY (course) REFERENCES Courses(courseID)
        ON DELETE CASCADE
) CHARACTER SET ascii COLLATE ascii_general_ci;
 COMMIT;
END$$


drop procedure if exists select_users$$
CREATE PROCEDURE select_users(
    IN data VARCHAR(30),
    IN start INT,
    IN stop INT)
BEGIN
    SELECT
         Users.usersID,
         Users.userName,
         Users.userEmail,
         Users.userPhone,
         Users.userMobilePhone,
         Users.userStatus,
         GROUP_CONCAT(Courses.courseName ORDER BY Courses.courseName SEPARATOR '***')


    FROM Users.Users
	LEFT JOIN Users.CourseUsers ON CourseUsers.users = Users.usersID
    LEFT JOIN Users.Courses ON Courses.courseID = CourseUsers.course
    WHERE Users.userName like data or Users.userEmail like data or Users.userMobilePhone like data or Users.userPhone like data
	GROUP BY Users.usersID, Users.userName,Users.userEmail, Users.userPhone, Users.userMobilePhone, Users.userStatus
    ORDER BY Users.userName
    LIMIT start, stop;
END$$

drop procedure if exists select_course$$
CREATE PROCEDURE select_course()
BEGIN
    SELECT
        Courses.courseID,
        Courses.courseName
    FROM Users.Courses;
END$$


DELIMITER;