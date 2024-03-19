import pandas as pd  
# Load the dataset  
survey = pd.read_csv('survey.csv')
# Create a function to categorize company size
def categorize_company_size(employee_count):
    if 1 <= employee_count <= 50:
        return "Small"
    elif 50 < employee_count <= 250:
        return "Medium"
    else:
        return "Large"
survey['no_employees'] = survey['no_employees'].apply(categorize_company_size)

survey.to_csv('cleaned_csv_file.csv', index=False)