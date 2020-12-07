dct_all_symptoms = {'most common symptoms': ['fever', 'dry cough', 'fatigue'], 'less common symptoms': ['aches and pains', 'sore throat', 'diarrhea', 'conjunctivitis', 'headache', 'loss of appetite', 'chills', 'dizziness', 'skin rash', 'vomit'], 'serious symptoms': ['difficulty breathing', 'shortness of breath', 'chest pain', 'loss of movement']}
dct_level_symptoms = {'less common symptoms' : -1, 'most common symptoms': 1} 

#traveller_country = 

count_symptoms = []
print(dct_all_symptoms.values()) #show user list of symptoms to input
list_of_symptoms = input("From all the symptom above, input every symptom you are experiencing with comma between each. If you have no symptoms listed above, please input None:").split(',')
if list_of_symptoms != ['None']:
    for symptom in list_of_symptoms: #from user's inputted info, store if these symptoms is common/serious
        for key, value in dct_all_symptoms.items():
            if symptom in value:
                count_symptoms.append(key)

    traveller_status = 0 #calculate the posibility level of user being affected by Covid-19
    for level_symptom in count_symptoms:
        if level_symptom == 'serious symptoms': #if symptoms are serious. End.
            print("You may be infected with Coronavirus, please manage your symptoms at home and call doctor before visiting health facility.")
            break
        else: #if symptoms are not serious (aka most common/less common)
            for key,value in dct_level_symptoms.items():
                if level_symptom in key:
                    traveller_status += int(value)
    print(traveller_status)
"""                    
            dct_medical_conditions = ['cancer','diabetes','obesity','sickle cell disease','heart conditions', 'weakened immune system', 'Asthma']
            print(dct_medical_conditions) #give user list of dangerous underlying medical conditions
            
            underlying_medical_conditions = (input('Please enter any underlying medical conditions you have above. If not, please input None: ')).split()
            
            if underlying_medical_conditions != ['None']: 
                for condition in underlying_medical_conditions: #add to the posibility level of user being affected by Coivd-19
                    traveller_status += 1
                visit_countries_14_days = (input('Enter every countries you have visited in the last 14 days? If not, please input None: ')).split()
                if visit_countries_14_days != 'None':
                    print('check')
            
            if traveller_status >= 5: #Not a correctr number yet. Need to decide how high the result should be to assume that user is possibly affected
                print("You may be infected with Coronavirus, please manage your symptoms at home and call doctor before visiting health facility.")
                break
"""                       
    
