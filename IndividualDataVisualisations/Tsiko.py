import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv("survey.csv")

catName = ['Yes', 'No','Don\'t Know/No']
results = {
        'Switzerland': [2,1,2], #each of these values was determined by the .shape(0), code below and the results were printed onto the console, before they were added here
        'Canada': [24,19,20],
        'Netherlands': [3, 10, 6],
        'United Kingdom': [17, 67, 56],
        'France': [1,3,0],
        'Belgium': [2,1,1],
        'Sweden': [2,1,2],
        'Austria': [1,0,0],
        'Denmark': [0,2,0],
        'Australia': [4,12,4],
        'Finland': [0,2,0],
        'Norway': [0,0,0],
        'United States': [338, 98, 167],
        'Japan': [0,1,0],
        'Italy': [0,3,3],
        'Singapore': [0,1,3],
        'New Zealand': [1,6,1],
        'South Africa': [0,4,1],
        'Czech Republic': [0,1,0],
        'Portugal': [0,1,0],
        'Hungary': [0,1,0],
        'Poland': [0,5,2],
        'Slovakia': [0,0,0],
        'Slovenia': [0,0,1],
        'Croatia': [1,1,0],
        'Bulgaria': [0,2,1],
        'Bosnia and Herzegovina': [0,0,1],
        'Moldova': [0,1,0],
        'Georgia': [0,1,0],
        'Russia': [0,2,0],
        'India': [0,2,3],
        'Thailand': [0,1,0],
        'Philippines': [0,0,1],
        'China': [0,1,0],
        'Germany': [3,17,13],
        'Mexico': [0,2,1],
        }



def country_mental_Benefits(): #Tsiko, question 1b
    
    #Calculations to derive the points that the graph should be plotted to
    BenefitsSwi1 = data[(data['Country'] == 'Switzerland') & (data['benefits'] == 1)].shape[0] #Yes 2
    BenefitsSwi2 = data[(data['Country'] == 'Switzerland') & (data['benefits'] == 2)].shape[0] #No 1
    BenefitsSwi3 = data[(data['Country'] == 'Switzerland') & (data['benefits'] == 3)].shape[0] #Dont know/Not sure 2
    
    BenefitsCan1 = data[(data['Country']=='Canada') & (data['benefits'] == 1)].shape[0] #Yes 24
    BenefitsCan2 = data[(data['Country']=='Canada') & (data['benefits'] == 2)].shape[0] #No 19
    BenefitsCan3 = data[(data['Country']=='Canada') & (data['benefits'] == 3)].shape[0]#Dont know/Not sure 20
    
    BenefitsNet1 = data[(data['Country']=='Netherlands') & (data['benefits'] == 1)].shape[0]#Yes 3
    BenefitsNet2 = data[(data['Country']=='Netherlands') & (data['benefits'] == 2)].shape[0] #No 10
    BenefitsNet3 = data[(data['Country']=='Netherlands') & (data['benefits'] == 3)].shape[0]#Dont know/Not sure 6

    BenefitsUK1 = data[(data['Country']=='United Kingdom') & (data['benefits'] == 1)].shape[0]#Yes 17
    BenefitsUK2 = data[(data['Country']=='United Kingdom') & (data['benefits'] == 2)].shape[0]#No 67
    BenefitsUK3 = data[(data['Country']=='United Kingdom') & (data['benefits'] == 3)].shape[0]#Dont know/Not sure 56

    BenefitsFra1 = data[(data['Country']=='France') & (data['benefits'] == 1)].shape[0]
    BenefitsFra2 = data[(data['Country']=='France') & (data['benefits'] == 2)].shape[0]
    BenefitsFra3= data[(data['Country']=='France') & (data['benefits'] == 3)].shape[0]

    BenefitsBel1 = data[(data['Country']=='Belgium') & (data['benefits'] == 1)].shape[0]
    BenefitsBel2 = data[(data['Country']=='Belgium') & (data['benefits'] == 2)].shape[0]
    BenefitsBel3 = data[(data['Country']=='Belgium') & (data['benefits'] == 3)].shape[0]

    BenefitsSwe1 = data[(data['Country']=='Sweden') & (data['benefits'] == 1)].shape[0]
    BenefitsSwe2 = data[(data['Country']=='Sweden') & (data['benefits'] == 2)].shape[0]
    BenefitsSwe3 = data[(data['Country']=='Sweden') & (data['benefits'] == 3)].shape[0]

    BenefitsAustria1 = data[(data['Country']=='Austria') & (data['benefits'] == 1)].shape[0]
    BenefitsAustria2 = data[(data['Country']=='Austria') & (data['benefits'] == 2)].shape[0]
    BenefitsAustria3 = data[(data['Country']=='Austria') & (data['benefits'] == 3)].shape[0]

    BenefitsDen1 = data[(data['Country']=='Denmark') & (data['benefits'] == 1)].shape[0]
    BenefitsDen2 = data[(data['Country']=='Denmark') & (data['benefits'] == 2)].shape[0]
    BenefitsDen3 = data[(data['Country']=='Denmark') & (data['benefits'] == 3)].shape[0]

    BenefitsAus1 = data[(data['Country']=='Australia') & (data['benefits'] == 1)].shape[0]
    BenefitsAus2 = data[(data['Country']=='Australia') & (data['benefits'] == 2)].shape[0]
    BenefitsAus3 = data[(data['Country']=='Australia') & (data['benefits'] == 3)].shape[0]

    BenefitsFin1 = data[(data['Country']=='Finland') & (data['benefits'] == 1)].shape[0]
    BenefitsFin2 = data[(data['Country']=='Finland') & (data['benefits'] == 2)].shape[0]
    BenefitsFin3 = data[(data['Country']=='Finland') & (data['benefits'] == 3)].shape[0]

    BenefitsNor1 = data[(data['Country']=='Norway') & (data['benefits'] == 1)].shape[0]
    BenefitsNor2 = data[(data['Country']=='Norway') & (data['benefits'] == 2)].shape[0]
    BenefitsNor3 = data[(data['Country']=='Norway') & (data['benefits'] == 3)].shape[0]

    BenefitsUS1 = data[(data['Country']=='United States') & (data['benefits'] == 1)].shape[0]
    BenefitsUS2 = data[(data['Country']=='United States') & (data['benefits'] == 2)].shape[0]
    BenefitsUS3 = data[(data['Country']=='United States') & (data['benefits'] == 3)].shape[0]

    BenefitsJap1 = data[(data['Country']=='Japan') & (data['benefits'] == 1)].shape[0]
    BenefitsJap2 = data[(data['Country']=='Japan') & (data['benefits'] == 2)].shape[0]
    BenefitsJap3 = data[(data['Country']=='Japan') & (data['benefits'] == 3)].shape[0]

    BenefitsIta1 = data[(data['Country']=='Italy') & (data['benefits'] == 1)].shape[0]
    BenefitsIta2 = data[(data['Country']=='Italy') & (data['benefits'] == 2)].shape[0]
    BenefitsIta3 = data[(data['Country']=='Italy') & (data['benefits'] == 3)].shape[0]

    BenefitsSin1 = data[(data['Country']=='Singapore') & (data['benefits'] == 1)].shape[0]
    BenefitsSin2 = data[(data['Country']=='Singapore') & (data['benefits'] == 2)].shape[0]
    BenefitsSin3 = data[(data['Country']=='Singapore') & (data['benefits'] == 3)].shape[0]

    BenefitsNZ1 = data[(data['Country']=='New Zealand') & (data['benefits'] == 1)].shape[0]
    BenefitsNZ2 = data[(data['Country']=='New Zealand') & (data['benefits'] == 2)].shape[0]
    BenefitsNZ3 = data[(data['Country']=='New Zealand') & (data['benefits'] == 3)].shape[0]

    BenefitsSA1 = data[(data['Country']=='South Africa') & (data['benefits'] == 1)].shape[0]
    BenefitsSA2 = data[(data['Country']=='South Africa') & (data['benefits'] == 2)].shape[0]
    BenefitsSA3 = data[(data['Country']=='South Africa') & (data['benefits'] == 3)].shape[0]

    BenefitsCR1 = data[(data['Country']=='Czech Republic') & (data['benefits'] == 1)].shape[0]
    BenefitsCR2 = data[(data['Country']=='Czech Republic') & (data['benefits'] == 2)].shape[0]
    BenefitsCR3 = data[(data['Country']=='Czech Republic') & (data['benefits'] == 3)].shape[0]

    BenefitsPor1 = data[(data['Country']=='Portugal') & (data['benefits'] == 1)].shape[0]
    BenefitsPor2 = data[(data['Country']=='Portugal') & (data['benefits'] == 2)].shape[0]
    BenefitsPor3 = data[(data['Country']=='Portugal') & (data['benefits'] == 3)].shape[0]

    BenefitsHun1 = data[(data['Country']=='Hungary') & (data['benefits'] == 1)].shape[0]
    BenefitsHun2 = data[(data['Country']=='Hungary') & (data['benefits'] == 2)].shape[0]
    BenefitsHun3 = data[(data['Country']=='Hungary') & (data['benefits'] == 3)].shape[0]

    BenefitsPol1 = data[(data['Country']=='Poland') & (data['benefits'] == 1)].shape[0]
    BenefitsPol2 = data[(data['Country']=='Poland') & (data['benefits'] == 2)].shape[0]
    BenefitsPol3 = data[(data['Country']=='Poland') & (data['benefits'] == 3)].shape[0]

    BenefitsSlok1 = data[(data['Country']=='Slovakia') & (data['benefits'] == 1)].shape[0]
    BenefitsSlok2 = data[(data['Country']=='Slovakia') & (data['benefits'] == 2)].shape[0]
    BenefitsSlok3= data[(data['Country']=='Slovakia') & (data['benefits'] == 3)].shape[0]

    BenefitsSlo1 = data[(data['Country']=='Slovenia') & (data['benefits'] == 1)].shape[0]
    BenefitsSlo2 = data[(data['Country']=='Slovenia') & (data['benefits'] == 2)].shape[0]
    BenefitsSlo3 = data[(data['Country']=='Slovenia') & (data['benefits'] == 3)].shape[0]

    BenefitsBnH1 = data[(data['Country']=='Bosnia and Herzegovina') & (data['benefits'] == 1)].shape[0]
    BenefitsBnH2 = data[(data['Country']=='Bosnia and Herzegovina') & (data['benefits'] == 2)].shape[0]
    BenefitsBnH3 = data[(data['Country']=='Bosnia and Herzegovina') & (data['benefits'] == 3)].shape[0]

    BenefitsMol1 = data[(data['Country']=='Moldova') & (data['benefits'] == 1)].shape[0]
    BenefitsMol2 = data[(data['Country']=='Moldova') & (data['benefits'] == 2)].shape[0]
    BenefitsMol3 = data[(data['Country']=='Moldova') & (data['benefits'] == 3)].shape[0]

    BenefitsGeo1 = data[(data['Country']=='Georgia') & (data['benefits'] == 1)].shape[0]
    BenefitsGeo2 = data[(data['Country']=='Georgia') & (data['benefits'] == 2)].shape[0]
    BenefitsGeo3 = data[(data['Country']=='Georgia') & (data['benefits'] == 3)].shape[0]
    
    BenefitsRus1 = data[(data['Country']=='Russia') & (data['benefits'] == 1)].shape[0]
    BenefitsRus2 = data[(data['Country']=='Russia') & (data['benefits'] == 2)].shape[0]
    BenefitsRus3 = data[(data['Country']=='Russia') & (data['benefits'] == 3)].shape[0]

    BenefitsInd1 = data[(data['Country']=='India') & (data['benefits'] == 1)].shape[0]
    BenefitsInd2 = data[(data['Country']=='India') & (data['benefits'] == 2)].shape[0]
    BenefitsInd3 = data[(data['Country']=='India') & (data['benefits'] == 3)].shape[0]

    BenefitsThai1 = data[(data['Country']=='Thailand') & (data['benefits'] == 1)].shape[0]
    BenefitsThai2 = data[(data['Country']=='Thailand') & (data['benefits'] == 2)].shape[0]
    BenefitsThai3 = data[(data['Country']=='Thailand') & (data['benefits'] == 3)].shape[0]

    BenefitsPhil1 = data[(data['Country']=='Philippines') & (data['benefits'] == 1)].shape[0]
    BenefitsPhil2 = data[(data['Country']=='Philippines') & (data['benefits'] == 2)].shape[0]
    BenefitsPhil3 = data[(data['Country']=='Philippines') & (data['benefits'] == 3)].shape[0]

    BenefitsChi1 = data[(data['Country']=='China') & (data['benefits'] == 1)].shape[0]
    BenefitsChi2 = data[(data['Country']=='China') & (data['benefits'] == 2)].shape[0]
    BenefitsChi3 = data[(data['Country']=='China') & (data['benefits'] == 3)].shape[0]

    BenefitsMex1 = data[(data['Country']=='Mexico') & (data['benefits'] == 1)].shape[0]
    BenefitsMex2 = data[(data['Country']=='Mexico') & (data['benefits'] == 2)].shape[0]
    BenefitsMex3 = data[(data['Country']=='Mexico') & (data['benefits'] == 3)].shape[0]

    BenefitsGer1 = data[(data['Country']=='Germany') & (data['benefits'] == 1)].shape[0]
    BenefitsGer2 = data[(data['Country']=='Germany') & (data['benefits'] == 2)].shape[0]
    BenefitsGer3 = data[(data['Country']=='Germany') & (data['benefits'] == 3)].shape[0]

    BenefitsCro1 = data[(data['Country']=='Croatia') & (data['benefits'] == 1)].shape[0]
    BenefitsCro2 = data[(data['Country']=='Croatia') & (data['benefits'] == 2)].shape[0]
    BenefitsCro3 = data[(data['Country']=='Croatia') & (data['benefits'] == 3)].shape[0]

    BenefitsBul1 = data[(data['Country']=='Bulgaria') & (data['benefits'] == 1)].shape[0]
    BenefitsBul2 = data[(data['Country']=='Bulgaria') & (data['benefits'] == 2)].shape[0]
    BenefitsBul3 = data[(data['Country']=='Bulgaria') & (data['benefits'] == 3)].shape[0]



# Extracting data for each category
yes = [results[country][0] for country in results]
no = [results[country][1] for country in results]
dontKnow = [results[country][2] for country in results]

# Creating scatter plots
plt.scatter(list(results.keys()), yes, color='red', label='Yes')
plt.scatter(list(results.keys()), no, color='green', label='No')
plt.scatter(list(results.keys()), dontKnow, color='lightblue', label='Don\'t Know/No')

# Adding labels and title
plt.title('Countries with companies providing Benefits for Mental Health')
plt.xlabel('Countries')
plt.ylabel('Companies')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()

# Showing the plot
plt.show()
