# This program is the implemntation of the dictionary in a dictionary
# known as nested dictionary or dictionary in a list of numbers etc..

# define nested dictionary
info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
        }

color = info['personal_data']['physical_features']['color']['hair']

print(color)

