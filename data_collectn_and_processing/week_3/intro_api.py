# in this we'll be working with REST API

# import modules
import requests
import json

# get the page
page = requests.get('https://api.datamuse.com/words?rel_rhy=go')

# type
print(type(page))

print(page.text[: 150]) # prints frist 150 charactersof th page

print(page.url) # print the url that was fetched


# turn page.text into pythn object
page_obj = page.json()

print()

print(type(page_obj)) # must be python json object

print()

print(page_obj[0])

print()

print(json.dumps(page_obj, indent=2))

############# some thing with url and its params ##################

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)