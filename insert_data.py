import sqlite3
import random
import faker
from datetime import datetime, timedelta

# Create a connection to the database (or connect to an existing one)
conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

# Insert data into the 'groups' table
groups_data = [
    ('Group A',),
    ('Group B',),
    ('Group C',)
]

cursor.executemany('INSERT INTO groups (group_name) VALUES (?)', groups_data)

# Insert data into the 'teachers' table
teachers_data = [
    ('Teacher 1',),
    ('Teacher 2',),
    ('Teacher 3',),
    ('Teacher 4',),
    ('Teacher 5',)
]

cursor.executemany('INSERT INTO teachers (teacher_name) VALUES (?)', teachers_data)

# Insert data into the 'subjects' table
subjects_data = [
    ('Mathematics', 1),
    ('Physics', 2),
    ('Chemistry', 3),
    ('Biology', 4),
    ('History', 5)
]

cursor.executemany('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', subjects_data)

# Insert data into the 'students' table using Faker library for generating names
fake = faker.Faker()

students_data = [
    (fake.first_name() + ' ' + fake.last_name(), random.randint(1, 3))
    for _ in range(50)
]

cursor.executemany('INSERT INTO students (student_name, group_id) VALUES (?, ?)', students_data)

# Insert data into the 'grades' table
grades_data = [
    (random.randint(1, 50), random.randint(1, 5), random.randint(1, 100),
     (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d'))
    for _ in range(1000)
]

cursor.executemany('INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)', grades_data)

# Commit changes and close the connection
conn.commit()
conn.close()
