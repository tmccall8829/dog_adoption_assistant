import sys
import csv
import pandas
from requests_html import HTMLSession
from os import path

session = HTMLSession()
#print("Successfully set up HTML session!")

# pass the shelter's dog listing URL as a script arg
#print("Gathering dog data...")
r = session.get(sys.argv[1])
petango_link_iframe = r.html.find("iframe")
petango_link = petango_link_iframe[0].attrs['src']

# now, use that petango link to get the HTML instead of having to use
# a python library to render the javascript
r = session.get(petango_link)
animal_info_block_list_raw = r.html.find("div.list-animal-info-block")

dogs = [a.text.splitlines() for a in animal_info_block_list_raw]
#print("Names: ", [d[0] for d in dogs])

# read the old dog data to compare
shelter_name = sys.argv[1].split("//")[1].split("/")[0].split(".")[-2]
filename = f'{shelter_name}_data.csv'
if path.exists(filename):
    old_data = pandas.read_csv(filename)
    #print("Old data: \n", old_data)

    # compare the old data to the new data
    old_dog_names = [d[0] for d in old_data.values]
    new_dog_names = [d[0] for d in dogs]
    #print("old_dog_names: ", old_dog_names)
    #print("new_dog_names: ", new_dog_names)

    added_dogs = []
    for name in new_dog_names:
        if name not in old_dog_names:
            print("Found a new dog: ", name)
            added_dogs.append(name)

    if len(added_dogs) > 0:
        print("Found new dogs: ", added_dogs)
    else:
        print("No new dogs found at", shelter_name)
else:
    print("First time running. No comparison needed.")
    
# save the new data off to a CSV for next time
#print("Writing saved dog data to a file...")
with open(filename, mode='w') as dog_file:
    dog_writer = csv.writer(dog_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # write column names
    cols = list(range(len(dogs[0])))
    cols[0] = "Name"
    cols[1] = "ID"
    dog_writer.writerow(cols)
    for dog in dogs:
        dog_writer.writerow(dog)
print("Done writing new data. Goodbye!")
