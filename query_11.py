import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

student_name = 'Anna Matthews'
teacher_name = 'Teacher 1'

query = f'''
    SELECT t.teacher_name, st.student_name, AVG(g.grade) AS average_grade
    FROM teachers t
    JOIN subjects s ON t.teacher_id = s.teacher_id
    JOIN grades g ON s.subject_id = g.subject_id
    JOIN students st ON g.student_id = st.student_id
    WHERE st.student_name = '{student_name}' AND t.teacher_name = '{teacher_name}'
    GROUP BY t.teacher_name, st.student_name;
'''

cursor.execute(query)
result = cursor.fetchone()

if result:
    teacher_name, student_name, average_grade = result
    print(f"Average grade given by {teacher_name} to {student_name}: {average_grade:.2f}")
else:
    print(f"No data found for {teacher_name} and {student_name}")

conn.close()
