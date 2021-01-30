# dog_adoption_assistant
This script runs a simple web scraper written in Python to help me keep track of new dogs added to my favorite shelter websites -- hopefully in order to help me find a dog more quickly!

## Methodology
I use a couple libraries here to help me scrape and analyze the data:
1. Requests-HTML
2. CSV and Pandas

These packages help me (1) collect the data, and (2) analyze it (respectively). The process, generally, is as follows:
1. Use the link passed to the script to find the `petango` link (this brings us to a page with HTML that is easily readable, compared to the shelter pages)
2. Scrape all the data from the `petango` link
3. Read the old data file (if there is one)
4. Compare the new data to the old data
5. Report if there are any new dogs listed, via email
6. Save the new data to a file
7. Profit (not really)
