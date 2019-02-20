#Find the possible venues that are wheelchair accessible, in Toronto, and can fit at least 150 people. 
#These results should be stored in a list.

venues = [
{ 'address': "123 Main Street", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 100 },

{ 'address': "567 Centre Street", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 400 },

{ 'address': "9B Ontario Street", 'city': "Montreal", 'wheelchair_accessible': True, 'capacity': 1000 },

{ 'address': "56 Road Avenue", 'city': "Ottawa", 'wheelchair_accessible': True, 'capacity': 650 },

{ 'address': "938 Avenue Way East", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 90 },

{ 'address': "34 Main Street West", 'city': "London", 'wheelchair_accessible': False, 'capacity': 300 },

{ 'address': "44 Quebec Road", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 200 },

{ 'address': "10 Spruce Avenue Ouest", 'city': "Montreal", 'wheelchair_accessible': False, 'capacity': 525 }

]


accessible_venues = []

for stations in venues:
	
	wheelchair = stations["wheelchair_accessible"]
	city = stations["city"]
	capacity = stations["capacity"]

	if stations ['city'] == "Toronto" and stations ['wheelchair_accessible'] == True and stations ['capacity'] >= 150:
		accessible_venues.append(stations['address'])
		
print(accessible_venues)