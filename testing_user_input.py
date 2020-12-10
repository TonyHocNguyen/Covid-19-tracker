"""
Covid tracker
Author:
"""
def user_symptoms_input():
    user_symptoms_list = []
    user_score = 0
    all_symptoms = ['fever', 'dry cough', 'fatigue', 'aches and pains', 'sore throat', 'diarrhea', 'conjunctivitis',
                        'headache', 'loss of appetite', 'chills', 'dizziness', 'skin rash', 'vomit', 'difficulty breathing',
                        'shortness of breath', 'chest pain', 'loss of movement']
    
    common_symptoms = {'most common symptoms': ['fever', 'dry cough', 'fatigue'],
                       'less common symptoms': ['aches and pains', 'sore throat', 'diarrhea', 'conjunctivitis', 'headache',
                                                'loss of appetite', 'chills', 'dizziness', 'skin rash', 'vomit']}
    
    serious_symptoms = {'difficulty breathing', 'shortness of breath', 'chest pain', 'loss of movement'}
    
    level_symptoms = {'most common symptoms': -1, 'less common symptoms': 1} 
        
    print('*** Welcome to the covid traveling advising engine ***')
    destination = input("Please enter a country you want to travel to: ")
    origin = input("Please enter your current country: ")
    print(all_symptoms)
    user_symptoms = input("Please enter a symptom from the reference list above. If you don't have any symptoms, type in none: ")
    
    while user_symptoms != '':
        if user_symptoms == 'none':
            return
        elif user_symptoms in user_symptoms_list:
            print("You have already input this symptom.")
            user_symptoms = input("Please enter a symptom from the reference list above. If you don't have any symptoms, type in none: ")
        elif user_symptoms in all_symptoms:
            user_symptoms_list += [user_symptoms]
            user_symptoms = input("Please enter a symptom from the reference list above. If you don't have any symptoms, type in none: ")
        elif user_symptoms not in all_symptoms:
            print("Your symptom is not in the reference list.")
            user_symptoms = input("Please enter a symptom from the reference list above. If you don't have any symptoms, type in none: ")
    for symptoms in user_symptoms_list:
        if symptoms in serious_symptoms:
            return "Stay home"
        else:
            for types in common_symptoms:
                if symptoms in common_symptoms[types]:
                    user_score += level_symptoms[types]
    return user_score, user_symptoms_list