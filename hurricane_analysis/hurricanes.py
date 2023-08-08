# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def convert_to_float(list):
  new_list = []
  for item in list:
    if item == 'Damages not recorded':
      new_list.append(item)
    elif 'M' in item:
      m_int = conversion.get('M')
      new_list.append(float(item.strip('M')) * m_int)
    elif 'B' in item:
      b_int = conversion.get('B')
      new_list.append(float(item.strip('B')) * b_int)
  return new_list

# test function by updating damages
#print(convert_to_float(damages))
damages = convert_to_float(damages)

# 2 
# Create a Table

# Create and view the hurricanes dictionary

def create_hurricanes_dictionary():
  hurricanes = {}
  single_dict = {}
  for i in range(34):
    hurricane_name = names[i]
    single_dict['Name'] = names[i]
    single_dict['Month'] = months[i]
    single_dict['Year'] = years[i]
    single_dict['Max Sustained Wind'] = max_sustained_winds[i]
    single_dict['Areas Affected'] = areas_affected[i]
    single_dict['Damage'] = damages[i]
    single_dict['Deaths'] = deaths[i]
    hurricanes[hurricane_name] = single_dict
    single_dict = {}
  return hurricanes

hurricanes = create_hurricanes_dictionary()
#print(hurricanes)

# 3
# Organizing by Year

# create a new dictionary of hurricanes with year and key
def organize_by_year(hurricane_dict):
  new_dict = {}
  list_of_hurricanes = []
  for i in range(34):
    year = years[i]
    for dict_val in hurricanes.values():
      if dict_val['Year'] == year:
        list_of_hurricanes.append(dict_val)
    new_dict[year] = list_of_hurricanes
    list_of_hurricanes = []
  return new_dict

hurricanes_sorted_by_year = organize_by_year(hurricanes)
#print(hurricanes_sorted_by_year)

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
#print(hurricanes)
def count_areas_affected(hurricanes_dict):
  counts_dict = {}
  list_of_areas = [dict_val['Areas Affected'] for dict_val in hurricanes_dict.values()]
  flat_list = [item for sublist in list_of_areas for item in sublist]
  for area in flat_list:
    if area in counts_dict:
      counts_dict[area] += 1
    else:
      counts_dict[area] = 1
  return counts_dict

count_areas_affected = count_areas_affected(hurricanes)
#print(count_areas_affected )


# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def find_most_affected_area(dictionary):
  most_affected_area = ''
  max_times_hit = 0
  for key, val in dictionary.items():
    if val > max_times_hit:
      most_affected_area = key
      max_times_hit = val
  return most_affected_area, max_times_hit

max_area, max_area_count = find_most_affected_area(count_areas_affected)
#print(max_area)
#print(max_area_count)


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
#print(hurricanes)
def find_deadliest_hurricane(dictionary):
  deadliest_hurricane = ''
  max_num_of_deaths = 0
  for dict_val in dictionary.values():
    hurricane = dict_val['Name']
    deaths = dict_val['Deaths']
    if deaths > max_num_of_deaths:
      deadliest_hurricane = hurricane
      max_num_of_deaths = deaths
  return deadliest_hurricane, max_num_of_deaths

deadliest_hurricane, num_of_deaths = find_deadliest_hurricane(hurricanes)
#print(deadliest_hurricane)
#print(num_of_deaths)


# 7
# Rating Hurricanes by Mortality

# categorize hurricanes in new dictionary with mortality severity as key

def sort_by_mortality_scale(dictionary):
  new_dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for val in dictionary.values():
    num_of_deaths = val['Deaths']
    name_of_hurricane = val['Name']
    if num_of_deaths == 0:
      new_dictionary[0].append(val)
    elif num_of_deaths <= 100:
      new_dictionary[1].append(val)
    elif num_of_deaths <= 500:
      new_dictionary[2].append(val)
    elif num_of_deaths <= 1000:
      new_dictionary[3].append(val)
    elif num_of_deaths <= 10000:
      new_dictionary[4].append(val)
    elif num_of_deaths > 10000:
      new_dictionary[5].append(val)
  return new_dictionary

mortality_ratings_sorted = sort_by_mortality_scale(hurricanes)
#print(mortality_ratings_sorted)


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def find_most_costly_hurricane(dictionary):
  max_damage = 0
  most_costly_hurricane = ''
  for val in dictionary.values():
    name = val['Name']
    damages = val['Damage']
    if type(damages) == str:
      max_damage = 0
    elif damages > max_damage:
      max_damage = damages
      most_costly_hurricane = name
  return most_costly_hurricane, max_damage

most_costly_hurricane, damage = find_most_costly_hurricane(hurricanes)
#print(most_costly_hurricane)
#print(damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def sort_by_damages(dictionary):
  new_dictionary = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for val in dictionary.values():
    damages = val['Damage']
    if type(damages) == str or damages == 0:
      new_dictionary[0].append(val)
    elif damages <= damage_scale[1]:
      new_dictionary[1].append(val)
    elif damages <= damage_scale[2]:
      new_dictionary[2].append(val)
    elif damages <= damage_scale[3]:
      new_dictionary[3].append(val)
    elif damages <= damage_scale[4]:
      new_dictionary[4].append(val)
    else:
      new_dictionary[5].append(val)
  return new_dictionary

categorized_by_damages = sort_by_damages(hurricanes)
print(categorized_by_damages)



