from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://www.jrspupsnstuff.org/dogs')
petango_link_iframe = r.html.find("iframe")
petango_link = petango_link_iframe[0].attrs['src']

# now, use that petango link to get the HTML instead of having to use
# a python library to render the javascript
r = session.get(petango_link)
animal_info_block_list_raw = r.html.find("div.list-animal-info-block")

# loop through the dogs
#dogs = []
#for a in animal_info_block_list_raw:
#    dogs.append(a.text.splitlines())

dogs = [a.text.splitlines() for a in animal_info_block_list_raw]
print([d[0] for d in dogs])
