import pandas as pd
import matplotlib.pyplot as plt
 
data = pd.read_csv("survey.csv")

def reports_by_gender():
# Filter data for each supervisor reports 
#'Yes' to 1, 'Some of them' to 2, 'No' to 3 
    supervisor_1 = data[data['supervisor'] == 1]
    supervisor_2 = data[data['supervisor'] == 2]
    supervisor_3 = data[data['supervisor'] == 3]

    yes_gender_counts = supervisor_1['Gender'].value_counts().sort_index()
    some_gender_counts = supervisor_2['Gender'].value_counts().sort_index()
    no_gender_counts = supervisor_3['Gender'].value_counts().sort_index()

# Create the figure and the axes
    fig, ax = plt.subplots()
# Since the genders read female, male and other the same across all three categories
    genders = no_gender_counts.index
# Generate the bars for each category
    bar1 = ax.bar([i - 0.2 for i in range(len(yes_gender_counts))], yes_gender_counts.values, width=0.2, color=['purple'],label='Yes')
    bar2 = ax.bar([i for i in range(len(some_gender_counts))], some_gender_counts.values, width=0.2, color=['teal'],label='Some of them')
    bar3 = ax.bar([i + 0.2 for i in range(len(no_gender_counts))], no_gender_counts.values, width=0.2, color=['turquoise'], label='No')
# Add values on top of the bars
    for bar in bar1 + bar2 + bar3:
        height = bar.get_height()
        ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
        textcoords="offset points", ha='center', va='bottom')
# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Gender', fontsize=15)
    ax.set_ylabel('Supervisor Reports Count', fontsize=15)
    ax.set_title('Supervisor Reports Count by gender', fontsize=18)
    ax.set_xticks(range(len(genders)))
    ax.set_xticklabels(genders)
    ax.legend()
# Show the plot
    plt.show()


def treatment_by_tech_gender():
    # Filter data for tech company employees receiving treatment
    tech_treatment_data = data[(data['tech_company'] == 'Yes') & (data['treatment'] == 'Yes')]

    # Group filtered tech_treatment_data by gender and count the number of individuals
    gender_counts = tech_treatment_data['Gender'].value_counts().sort_index()
    # Custom colors for female, male, and other
    colors = ['#800080', '#4169E1', '#228B22'] 
    # Create a horizontal bar chart 
    plt.figure(figsize=(10, 6))
    plt.barh(gender_counts.index, gender_counts.values, color=colors)
    # Add values at the top of each bar
    for index, value in enumerate(gender_counts.values):
        plt.text(value, index, str(value), ha='left', va='center')

    plt.xlabel('Tech Employees Recieving Treatment', fontsize=15)
    plt.ylabel('Gender', fontsize=15, )
    plt.title('Treatment by Gender in Tech Companies', fontsize=18)
    plt.tight_layout()
    # Show the plot
    plt.show()




