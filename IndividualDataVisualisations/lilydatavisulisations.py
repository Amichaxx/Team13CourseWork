import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("survey.csv")

#Which age group of people is more likely to experience mental health issues?
seekYes = data[(data['seek_help'] == 1)]
seekNo = data[(data['seek_help'] == 2)]
seekUnsure = data[(data['seek_help'] == 3)]

mao = seekYes['Age'].value_counts().sort_index()
chikka = seekNo['Age'].value_counts().sort_index()
maowow = seekUnsure['Age'].value_counts().sort_index()

plt.plot(mao, color='pink', label='Experienced mental health')
plt.plot(chikka, color='green', label='Not experienced mental health')
plt.plot(maowow, color='blue', label='Unsure')

plt.title('Most common age for experiencing mental health')
plt.xlabel('Age')
plt.ylabel('Number of employees')
plt.grid(True)
plt.legend()
plt.show()
plt.show()

#Are younger employees more likely to seek help for mental health issues?
soughtTreatment = data[(data['treatment'] == 'Yes')]
notSoughtTreatment = data[(data['treatment'] == 'No')]

boo = soughtTreatment['Age'].value_counts().sort_index()
bow = notSoughtTreatment['Age'].value_counts().sort_index()

plt.plot(boo, color='pink', label='Sought treatment')
plt.plot(bow, color='green', label='Not sought treatment')

plt.title('Most common age for seeking treatment')
plt.xlabel('Age')
plt.ylabel('Number of employees')
plt.grid(True)
plt.legend()
plt.show()