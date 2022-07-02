#Declare an empty list
lista = list()

#Declare a list with more than 5 items
lista = [1,2,3,4,5]

#Find the length of your list
print(len(lista))

#Get the first item, the middle item and the last item of the list
print(lista[0])
print(lista[2])
print(lista[len(lista) - 1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Roberto', 'Aguilar', 1.72, 'soltero', 'Nicaragua']
print(mixed_data_types)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[len(it_companies) - 1])

#Print the list after modifying one of the companies
it_companies[4] = 'Acer'
print(it_companies)

#Add an IT company to it_companies
it_companies.append('IT')
print(it_companies)

#Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Ryzen')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = 'RYZEN'
it_companies.remove('IT')
print(it_companies)

#Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

#Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)

#Sort the list using sort() method
it_companies.sort()
print(it_companies)

print(sorted(it_companies, reverse=True))

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

it_companies.sort()
print(it_companies)

#Slice out the first 3 companies from the list
print(it_companies[:3])

#Slice out the last 3 companies from the list
print(it_companies[len(it_companies) - 3:])

#Slice out the middle IT company or companies from the list
print(it_companies[3:6])

#Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

#Remove the middle IT company or companies from the list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(3)
print(it_companies)

#Remove the last IT company from the list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(len(it_companies) - 1)
print(it_companies)

#Remove all IT companies from the list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

#Destroy the IT companies list
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

skill = front_end + back_end
print(skill)

#Copy the joined list and assign it to a variable full_stack.
full_stack = skill.copy()
print(full_stack)

#Insert Python and SQL after Redux
full_stack.insert(5,'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#-----------------------Exercises  Level 2------------------------------
#the following is a list of 10students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25,24]

#Sort the list and find the min and max age
ages.sort()
print(f'Min age: {ages[0]}. Max age: {ages[len(ages) - 1]}')

#Add the min age and the max age again to the list
min = ages[0]
max = ages[len(ages) - 1]
ages.append(min)
ages.append(max)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
media = (ages[(len(ages) - 1)//2] + ages[((len(ages) - 1)//2) - 1])//2
print(media)

#Find the average age (sum of all items divided by their number )
print(ages)
suma = 0

for i in range(0, len(ages) - 1):
    suma += ages[i] 

average = suma//len(ages)
print('Average = ',average)

#Find the range of the ages (max minus min)
range = max - min
print(range)

#Compare the value of (min - average) and (max - average), use abs() method
print(f'min - average = {abs(min - average)}. max - average = {abs(max - average)}')

#Find the middle country(ies) in the countries list
countries = ['Afghanistan','Albania','Algeria',
  'Andorra','Angola','Antigua and Barbuda','Argentina',
  'Armenia','Australia','Austria','Azerbaijan',
  'Bahamas','Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
middle = (len(countries) - 1)//2 
print(countries[middle])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(len(countries))

list1 = countries[:97].copy()
list2 = countries[97:].copy()
print(list2)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
list_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3,*scandic_countries = list_countries
print(scandic_countries)

