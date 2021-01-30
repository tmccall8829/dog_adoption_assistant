import sys
import csv
from requests_html import HTMLSession

session = HTMLSession()
print("Successfully set up HTML session!")

# pass the shelter's dog listing URL as a script arg
print("Gathering dog data...")
r = session.get(sys.argv[1])
petango_link_iframe = r.html.find("iframe")
petango_link = petango_link_iframe[0].attrs['src']

# now, use that petango link to get the HTML instead of having to use
# a python library to render the javascript
r = session.get(petango_link)
animal_info_block_list_raw = r.html.find("div.list-animal-info-block")

dogs = [a.text.splitlines() for a in animal_info_block_list_raw]
print("Names: ", [d[0] for d in dogs])

# save the data off to a CSV
print("Writing saved dog data to a file...")
shelter_name = sys.argv[1].split("//")[1].split("/")[0].split(".")[-2]
with open(f'{shelter_name}_data.csv', mode='w') as dog_file:
    dog_writer = csv.writer(dog_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for dog in dogs:
        dog_writer.writerow(dog)
print("Done.")
