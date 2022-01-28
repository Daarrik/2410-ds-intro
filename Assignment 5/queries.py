import sqlite3
import json
import pandas as pd

# PART 1
con = sqlite3.connect('database.db')

# Comment out lines 11-23 after tables in database.db
# have been created. Not necessary, but doesn't print 
# out warnings or exceptions if it is commented out.
try:
  grades_data = pd.read_csv('grades.csv')
  grades_data.to_sql(con=con, name='grades')
except ValueError:
  print('Grades database already created')

try:
  profile_json = open('profile.json')
  profile = json.load(profile_json)
  student_data = pd.DataFrame(profile)
  student_data.to_sql(con=con, name='students')
except ValueError:
  print('Students database already created')

# PART 2
cur = con.cursor()
cur.execute('select * from grades where Name="Darrik"')
print(f'Retrieved Darrik\'s data: {cur.fetchone()}')
cur.execute('select Grade from grades where Name="Darrik"')
print(f'Retrieved Darrik\'s grade: {cur.fetchone()}')

# PART 3
cur.execute('select Major from students where Name="Darrik"')
print(f'Darrik\'s current Major: {cur.fetchone()}')
cur.execute('update students set Major="CS" where Name="Darrik"')
cur.execute('select Major from students where Name="Darrik"')
print(f'Darrik\'s new Major: {cur.fetchone()}')
con.commit()

# PART 4
# grades and students tables do not have a shared column
# where each student has a unique identifier, nor are they
# of the same length. This means we cannot join the two 
# tables in a way that would avoid duplicate names like 
# "Ashley" or "Anthony". (Explanation below)
# I just run queries separately on the tables.
cur.execute('select Name from grades where Grade="A"')
print(f'Students with an A: {cur.fetchall()}')
cur.execute('select Name from students where GPA>3.5 and Major="CS"')
print(f'CS Majors with GPA > 3.5: {cur.fetchall()}')

# PART 5
cur.execute('select Name from grades where Project>90')
print(f'My own query: {cur.fetchall()}')

# Explaining the problem in part 4:
print('\nThe problem with the data:')
# To demonstrate the problem I described above, let's make a 
# query of all the students that appear more than once in 
# either grades AND students.
# Anthony (2) and Ashley (3) appear more than once in both 
# students and grades.

cur.execute('select * from students ' +
            'join grades on grades.Name=students.Name ' +
            'where students.Name="Anthony" ' +
            'or students.Name="Ashley"')
for student in cur.fetchall():
  print(student)

# Suddenly, there are 4 Anthonys and 9 Ashleys.
# What is happening:
# Without a unique identifier to match the Ashleys
# in students to the Ashleys in grades, it just
# matches them all to each other, creating new
# Ashleys. The same thing happens to Anthony.

# Something similar happens to Ana and Benjamin.
# Ana appears in students once, but grades twice.
# Benajmin appears in students twice, but grades once.
# In both cases, there will be 2 Anas and 2 Benjamins,
# but it does not make sense to combine them as we don't
# know which Ana goes to which Ana and which Benjamin goes
# to which Benjamin.
cur.execute('select * from students ' +
            'join grades on grades.Name=students.Name ' +
            'where students.Name="Ana" ' +
            'or students.Name="Benjamin"')
for student in cur.fetchall():
  print(student)