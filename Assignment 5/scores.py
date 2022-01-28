import pandas as pd

def main():
  scores = pd.read_csv('P5_scores.csv')
  raw_grades = []
  for row in scores.itertuples():
    print(row)
    score_weight = sum(row[2:5]) * .2
    proj_weight = row[5] * .4
    raw_grade = round(score_weight + proj_weight, 2)
    #print(f'Student: {row[1]}, Grade: {raw_grade}')
    raw_grades.append(raw_grade)
  
  letter_grades = []
  for grade in raw_grades:
    if grade >= 90:
      letter_grades.append('A')
    elif grade >= 80:
      letter_grades.append('B')
    else:
      letter_grades.append('C')
  
  scores['Grade'] = letter_grades
  # Remove trailing white spaces from headers
  # Not necessary, but saves headache for database queries
  scores = scores.rename(columns=lambda column : column.strip())  
  scores.to_csv('grades.csv', index=False)

if __name__ == '__main__':
  main()