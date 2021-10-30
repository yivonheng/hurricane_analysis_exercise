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

# write your update damages function here:

new_damages = [] 
def new_list_damages(): 
    for i in range(len(damages)):
        if damages[i][-1] == "M":
            damages[i] = int(float(damages[i][:-1])*1000000)
        elif damages[i][-1] == "B": 
            damages[i] = int(float(damages[i][:-1])*1000000000)
    else:
        return damages                  
print(new_list_damages()) 

# write your construct hurricane dictionary function here:
dict_key_names = {}
for i in range(len(names)):
    dict_key_names[names[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
print(dict_key_names)

print("\n") 
    #test display Bahamas values
print(dict_key_names["Bahamas"]) 


# write your construct hurricane by year dictionary function here:
dict_key_years = {} 
for i in range(len(years)): 
    dict_key_years[years[i]] = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
print(dict_key_years)
print("\n") 

    #test display 1928 values
print(dict_key_years[1928])
print("\n")   

# write your count affected areas function here:  
count_areas_affected = {} 
for lst in areas_affected:
    for area in lst:
        if area not in count_areas_affected:
            count_areas_affected[area] = 1 
        else:
            count_areas_affected[area] += 1 
print(count_areas_affected) 
print("\n")

# write your find most affected area function here:
def most_affected_area(): 
    most_affected = max(count_areas_affected, key = lambda i: count_areas_affected[i])
    num_of_affected = count_areas_affected[most_affected]  
    print("The most affected area is " + most_affected + " which recorded " + str(num_of_affected) + " hits.")    
most_affected_area()   
print("\n")     

# write your greatest number of deaths function here:
names_to_deaths = {key: value for key, value in zip(names, deaths)} 
print(names_to_deaths) 
print("\n")

def most_deaths(): 
    most_death = max(names_to_deaths, key = lambda i: names_to_deaths[i]) 
    num_of_death = names_to_deaths[most_death] 
    print("The hurricane that caused most deaths is " + most_death + " which caused " + str(num_of_death) + " of deaths.")  
most_deaths()
print("\n") 

# write your catgeorize by mortality function here:
hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5:[]} 

def rate_hurricanes(): 
    for i in names_to_deaths: 
        if names_to_deaths[i] == 0:
            hurricanes_by_mortality[0].append(i) 
        elif 0 < names_to_deaths[i] <= 100:
            hurricanes_by_mortality[1].append(i)
        elif 100 < names_to_deaths[i] <= 500:
            hurricanes_by_mortality[2].append(i)
        elif 500 < names_to_deaths[i] <= 1000:
            hurricanes_by_mortality[3].append(i)
        elif 1000 < names_to_deaths[i] <= 5000:
            hurricanes_by_mortality[4].append(i)
        elif names_to_deaths[i] > 5000:
            hurricanes_by_mortality[5].append(i)
    print(hurricanes_by_mortality, "\n")  
rate_hurricanes()

# write your greatest damage function here:

names_to_damages = {key: value for key, value in zip(names, damages)} 

print(names_to_damages)
print("\n") 

def get_max_damage(): 
    max_damage_cane = " "
    max_damage = 0 
    for i in names_to_damages:
        if names_to_damages[i] == "Damages not recorded":
            continue
        if names_to_damages[i] > max_damage:
            max_damage = names_to_damages[i] 
            max_damage_cane = i   
    print("The hurricane that caused the most damage is " + i + " which incurred $" + str(max_damage) + ". \n")   
get_max_damage() 

# write your catgeorize by damage function here:
damages_by_rating = {0: [], 1: [], 2: [], 3: [], 4: []} 

def rate_damages(): 
    for i in names_to_damages: 
        if names_to_damages[i] == "Damages not recorded":
            continue
        elif names_to_damages[i] == 0:
            damages_by_rating[0].append(i) 
        elif 0 < names_to_damages[i] <= 100000000:
            damages_by_rating[1].append(i)
        elif 100000000 < names_to_damages[i] <= 1000000000:
            damages_by_rating[2].append(i)
        elif 1000000000 < names_to_damages[i] <= 10000000000:
            damages_by_rating[3].append(i)
        elif 10000000000 < names_to_damages[i] <= 50000000000:
            damages_by_rating[4].append(i)       
    print(damages_by_rating)  
rate_damages() 
print("\n") 
