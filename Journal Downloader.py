#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import requests

# Open the CSV file and read the DOIs
with open('yourcsv.csv', newline='') as csvfile:
    doi_reader = csv.reader(csvfile)
    next(doi_reader) # Skip header row
    dois = [row[10] for row in doi_reader]

# Loop through the DOIs and download the papers
for doi in dois:
    # Send a request to Sci-Hub with the paper's DOI
    response = requests.get('https://sci-hub.se/' + doi)

    # Save the PDF to a file
    with open(doi + '.pdf', 'wb') as f:
        f.write(response.content)


# In[ ]:




