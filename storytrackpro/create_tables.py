import os
import django
import mysql.connector
from mysql.connector import connect, Error
from django.conf import settings

# Load Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storytrackpro.settings")
django.setup()

# Get database settings from Django's DATABASES configuration
db_settings = settings.DATABASES["default"]

# SQL statements to create tables
CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS MEDIA_ORGANIZATION (
        OrgID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        City VARCHAR(255) NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS REPORTER (
        ReporterID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        UserID INT NOT NULL,  -- Foreign key to auth_user
        OrgID INT,
        FOREIGN KEY (UserID) REFERENCES auth_user(id) ON DELETE CASCADE,
        FOREIGN KEY (OrgID) REFERENCES MEDIA_ORGANIZATION(OrgID) ON DELETE SET NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS EDITOR (
        EditorID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        UserID INT NOT NULL,  -- Foreign key to auth_user
        OrgID INT,
        FOREIGN KEY (UserID) REFERENCES auth_user(id) ON DELETE CASCADE,
        FOREIGN KEY (OrgID) REFERENCES MEDIA_ORGANIZATION(OrgID) ON DELETE SET NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS STORY (
        StoryID INT AUTO_INCREMENT PRIMARY KEY,
        ReporterID INT,
        EditorID INT,
        OrgID INT,
        Headline VARCHAR(255) NOT NULL,
        Status VARCHAR(50) NOT NULL,
        Priority VARCHAR(50) NOT NULL,
        AssignedDate DATE NOT NULL,
        DueDate DATE NOT NULL,
        Category VARCHAR(255),
        StoryBody TEXT,
        Feedback TEXT,
        FOREIGN KEY (ReporterID) REFERENCES REPORTER(ReporterID) ON DELETE SET NULL,
        FOREIGN KEY (EditorID) REFERENCES EDITOR(EditorID) ON DELETE SET NULL,
        FOREIGN KEY (OrgID) REFERENCES MEDIA_ORGANIZATION(OrgID) ON DELETE SET NULL
    );
    """,
]


# Function to execute SQL commands
def create_tables():
    try:
        # Connect to the MySQL database using Django's settings
        connection = connect(
            host=db_settings["HOST"],
            user=db_settings["USER"],
            password=db_settings["PASSWORD"],
            database=db_settings["NAME"],
            port=db_settings["PORT"],
        )
        if connection.is_connected():
            print("Connected to the database")
            cursor = connection.cursor()

            # Execute each SQL command
            for sql in CREATE_TABLES:
                cursor.execute(sql)
                print("Executed: ", sql)

            print("All tables created successfully!")

    except Error as e:
        print(f"Error Creating Tables: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
