import pandas as pd

survey = pd.read_csv('cleaned_gender_csv_file.csv')

survey = survey[(survey['Age'] >= 18) & (survey['Age'] <= 70)]

survey.to_csv('cleaned_age_csv_file.csv', index=False)