import os
import mysql.connector


DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", "Venky@123"),
    "database": os.getenv("MYSQL_DATABASE", "student_placement_db"),
}


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def create_tables():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            gender VARCHAR(20) NOT NULL,
            department VARCHAR(50) NOT NULL,
            cgpa DECIMAL(3,1) NOT NULL,
            graduation_year INT NOT NULL
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS skills (
            skill_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            skill_name VARCHAR(100) NOT NULL,
            FOREIGN KEY(student_id)
            REFERENCES students(student_id)
            ON DELETE CASCADE
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS interviews (
            interview_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            communication_score INT NOT NULL,
            technical_score INT NOT NULL,
            aptitude_score INT NOT NULL,
            FOREIGN KEY(student_id)
            REFERENCES students(student_id)
            ON DELETE CASCADE
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS placements (
            placement_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            company VARCHAR(100) NOT NULL,
            package_lpa DECIMAL(5,2) NOT NULL,
            placement_date DATE NOT NULL,
            FOREIGN KEY(student_id)
            REFERENCES students(student_id)
            ON DELETE CASCADE
        )
        """
    )

    connection.commit()

    cursor.close()

    connection.close()