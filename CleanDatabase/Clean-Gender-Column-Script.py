import pandas as pd

survey = pd.read_csv('survey.csv')

def categorize_gender(gender):
    if gender.lower() in {'m', 'male', 'man', 'guy', 'cis male'}:
        return 'male'
    elif gender.lower() in {'f', 'female', 'woman', 'w', 'cis female'}:
        return 'female'
    else:
        return 'other'
    
survey['Gender'] = survey['Gender'].apply(categorize_gender)

survey.to_csv('cleaned_csv_file.csv', index=False)