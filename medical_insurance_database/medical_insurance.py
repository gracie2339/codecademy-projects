medical_costs = {}
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0
medical_costs.update({'Connie': 8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0})
print(medical_costs)
medical_costs['Vinay'] = 3325.0
print(medical_costs)

total_cost = 0
for value in medical_costs.values():
    total_cost += value

average_cost = total_cost / len(medical_costs)
print('Average Insurance Cost: ' + str(average_cost))

names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)

names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get('Marina', None)
print('Marina\'s age is: ' + str(marina_age))

medical_records = {}
medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
names = ['Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [24, 43, 35, 52]
sex = ['Male', 'Female', 'Male', 'Female']
bmi = [26.9, 25.3, 20.6, 18.7]
children = [0, 3, 4, 1]
smoker = ['Non-smoker', 'Non-smoker', 'Smoker', 'Non-smoker']
insurance_costs = [3225.0, 8886.0, 16444.0, 6420.0]

for i in range(4):
    name = names[i]
    medical_records[name] = {"Age": ages[i], "Sex": sex[i], "BMI": bmi[i], "Children": children[i], "Smoker": smoker[i], "Insurance_cost": insurance_costs[i]}
print(medical_records)

connie_insurance_cost = medical_records.get('Connie')['Insurance_cost']
print('Connie\'s insurance cost is {cost} dollars'.format(cost=connie_insurance_cost))

medical_records.pop('Vinay')
print(medical_records)

for key, val in medical_records.items():
    print('{name} is a {age} year old {sex} {smoker} with a BMI of {bmi} and insurance cost of {insurance_cost}'.format(name=key, age=val['Age'], sex=val['Sex'], smoker=val['Smoker'], bmi=val['BMI'], insurance_cost=val['Insurance_cost']))