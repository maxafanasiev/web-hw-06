import sqlite3

conn = sqlite3.connect('school_database.db')
cursor = conn.cursor()

group_name = 'Group B'
subject_name = 'Physics'

query = f'''
    SELECT st.student_id, st.student_name, g.grade, g.date
    FROM students st
    JOIN grades g ON st.student_id = g.student_id
    JOIN subjects subj ON g.subject_id = subj.subject_id
    JOIN groups gr ON st.group_id = gr.group_id
    WHERE gr.group_name = '{group_name}' AND subj.subject_name = '{subject_name}'
    ORDER BY g.date DESC
    LIMIT 10;
'''

cursor.execute(query)
result = cursor.fetchone()

if result:
    student_id, student_name, grade, date = result
    print(f"Last grade of students in {subject_name}, {group_name}:")
    print("Student ID |  Student Name        | Grade | Date")
    print("----------------------------------------------")
    print(f"{student_id:10} | {student_name:20} | {grade:5} | {date}")
else:
    print(f"No data found for {subject_name} in {group_name}")

conn.close()
