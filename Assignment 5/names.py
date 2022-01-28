import numpy as np
import pandas as pd

def main():
  majors = ['CS', 'Bio', 'Chem', 'Math']
  
  name_col = []
  names = open('P5_names.txt', 'r')
  for name in names:
    name_col.append(name.rstrip())

  gpa_col = []
  major_col = []
  for _ in name_col:
    gpa = round(np.random.choice(np.arange(2.0, 4.0, .01)), 2)
    gpa_col.append(gpa)
    major_col.append(np.random.choice(majors))

  students = pd.DataFrame()
  students['Name'] = name_col
  students['GPA'] = gpa_col
  students['Major'] = major_col
  print(students)

  #students.to_json('profile.json', orient='records')
  students.to_csv('profile.csv', index=False)
if __name__ == '__main__':
  main()