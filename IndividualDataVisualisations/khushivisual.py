import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")
#Which continent has the highest mental health issues?

#seekYes = data[(data['seek_help'] == 1)]
#seekNo = data[(data['seek_help'] == 2)] 
#seekUnsure = data[(data['seek_help'] == 3)]
            
        
#northAmerica = (data['Country'] == 'United States') | (data['Country'] == 'Canada') | (data['Country'] == 'Mexico')
#southAmerica = (data['Country'] == 'Brazil') | (data['Country'] == 'Colombia')
#oceania = (data['Country'] == 'Australia') | (data['Country'] == 'New Zealand')
#africa = (data['Country'] == 'South Africa')
#asia= (data['Country'] == 'India') | (data['Country'] == 'Thailand') | (data['Country'] == 'Japan')| (data['Country'] == 'Philippines')| (data['Country'] == 'China')| (data['Country'] == 'Singapore')
#europe = (data['Country'] == 'United Kingdom') | (data['Country'] == 'Bulgaria') | (data['Country'] == 'Netherland')| (data['Country'] == 'Poland')| (data['Country'] == 'France')| (data['Country'] == 'Germany')| (data['Country'] == 'Slovenia')| (data['Country'] == 'Ireland')| (data['Country'] == 'Russia')| (data['Country'] == 'Italy')| (data['Country'] == 'Portugal')| (data['Country'] == 'Switzerland')| (data['Country'] == 'Belgium')| (data['Country'] == 'Sweden')| (data['Country'] == 'Finland')| (data['Country'] == 'Bosnia and Herzegovina')| (data['Country'] == 'Austria')| (data['Country'] == 'Hungary')| (data['Country'] == 'Crotia')| (data['Country'] == 'Denmark')| (data['Country'] == 'Moldova')| (data['Country'] == 'Georgia')| (data['Country'] == 'Czech Republic')                               
#x_labels=['North America', 'South America', 'Oceania', 'Africa', 'Asia', 'europe']
           
#na_y = data[(northAmerica) & (data['seek_help'] == 1)].shape[0]
#sa_y = data[(southAmerica) & (data['seek_help'] == 1)].shape[0]
#oc_y = data[(oceania) & (data['seek_help'] == 1)].shape[0] # 10
#af_y = data[(africa) & (data['seek_help'] == 1)].shape[0] # 0
#as_y = data[(asia) & (data['seek_help'] == 1)].shape[0]
#eu_y = data[(europe) & (data['seek_help'] == 1)].shape[0]
            
#na_n = data[(northAmerica) & (data['seek_help'] == 2)].shape[0]
#sa_n = data[(southAmerica) & (data['seek_help'] == 2)].shape[0]
#oc_n = data[(oceania) & (data['seek_help'] == 2)].shape[0] # 10
#af_n = data[(africa) & (data['seek_help'] == 2)].shape[0] # 0
#as_n = data[(asia) & (data['seek_help'] == 2)].shape[0]
#eu_n = data[(europe) & (data['seek_help'] == 2)].shape[0]
            
#na_us = data[(northAmerica) & (data['seek_help'] == 3)].shape[0]
#sa_us = data[(southAmerica) & (data['seek_help'] == 3)].shape[0]
#oc_us = data[(oceania) & (data['seek_help'] == 3)].shape[0] # 10
#af_us = data[(africa) & (data['seek_help'] == 3)].shape[0] # 0
#as_us = data[(asia) & (data['seek_help'] == 3)].shape[0]
#eu_us = data[(europe) & (data['seek_help'] == 3)].shape[0]
            
#yes_labels=[na_y, sa_y, oc_y, af_y, as_y, eu_y]
#no_labels=[na_n, sa_n, oc_n, af_n, as_n, eu_n]
#unsure_labels=[na_us, sa_us, oc_us, af_us, as_us, eu_us]
    
#plt.plot(x_labels, yes_labels, color='red', label='Experienced mental health')
#plt.plot(x_labels, no_labels, color='green', label='Not experienced mental health')
#plt.plot(x_labels, unsure_labels, color='purple', label='Unsure ')
        
#plt.plot(country_ref3, color='green', label='Unsure')

#plt.title('Most common country for experiencing mental health')
#plt.xlabel('Country')
#plt.ylabel('Number of employees')
#plt.grid(True)
#plt.legend()
#plt.show()

print("--- In what ways do cultural distinctions affect how tech workers in Japan and the US see and handle mental health concerns? ---")
            # Your method call for the question here
us1 = data[(data['Country']) == 'United States' & (data['seek_help'] == 'Yes')].shape[0] 
us2= data[(data['Country']) == 'United States' & (data['seek_help'] == 'No')].shape[0] 

jp1= data[(data['Country']) == 'Japan' & (data['seek_help'] == 'Yes')].shape[0] 
jp2 = data[(data['Country']) =='Japan' & (data['seek_help'] == 'No')].shape[0]
a= ['Yes', 'No']
b= [us1,us2]
c=[jp1,jp2]

fig, (japan, unitedStates) = plt.subplots(1, 2, sharey=True, figsize=(8,8))
japan.set_title("Staff seeking help in japan")
unitedStates.set_title("Staff seeking help in united States")

plt.bar(a, b, color='blue', label='seekedhelp')
plt.bar(a,c, color='pink', label='no_treatment')
                                                         
japan.set_xlabel('seek_help')
japan.set_ylabel('no_treatment')
unitedStates.set_xlabel('seeked_help')
unitedStates.set_ylabel('no_treatment')
                                                                                 
plt.ylim(bottom=0)                                              
plt.legend()
plt.show()
            
