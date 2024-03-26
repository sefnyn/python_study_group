#!/usr/bin/env python3
import  requests
import json


welcome = "\nWelcome to Search LCNAF!\n"
welcome+= 'This program lets you search the Library of Congress Name Authority File'
welcome+= ' using the Suggest2 API.'
welcome+= '\nWe *could* limit the search by entry category, '
welcome+= 'perform a left-anchored search, or search other vocabularies,'
welcome+= '\nbut today we\'ll just be running a simple keyword search on LCANF'
print(welcome)

query = input("\nWhat term would you like to search?\n\t")
params = {'q':query}
url = 'https://id.loc.gov/authorities/names/suggest2/'

response = requests.get(url, params=params)
results = response.json()
print(f"\nSearch for \"{query}\" returned {results['count']} results.")
print(f"Here are the first {results['pagesize']}:\n")

hits = results["hits"]
labels = {
    'aLabel': 'Authorized form:', 
    'vLabel': 'Variant form:', 
    'uri': 'URI:'
    }

for hit in hits:
    for label in labels:
        print(f"{labels[label].ljust(16)} {hit[label]}")
    print('')
