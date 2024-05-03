import sys

import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
#url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=data%2Bscience&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DUnited%2520States%26geoId%3D103644278%26f_TPR%3D%26f_JT%3DF%26position%3D1%26pageNum%3D0&start=20'
url = 'https://www.linkedin.com/jobs/view/data-scientist-product-analytics-at-meta-3912361526?position=9&pageNum=0&refId=7dk72T%2FLSIuD3UvZAtA2aw%3D%3D&trackingId=rBPCBFhCKdmjWhoirAPSrg%3D%3D&trk=public_jobs_jserp-result_search-card'
# Define the bearer token
bearer_token = 'AQUlN-nEkFgrAioTvzkLHZkPQ_qyyyBJaV5VL5UbGngBitrKy2Ny0ijZW6hiyi_VSSjvSKpMfrOuIfgRyn_1Lp9EyFaMwWj6rg6ffiuqnXoGRxEeaAyNOCJZU8AdUw5IA1SWIaPNhaBib-NMffUCuFLCk0UgsGt6UYL2hZ4QuKyIJogpPGaSWTo8a-igYLTxZA3X2socD4QhsOsQf3DjycEm4WjksUdhe9txZ_tcZWCMwCZrn78iZlZNeG1lSsi3eE_iFkf8dQ6npCf5QQtvnxV_AXfznvqHl6I8NBpFq6AwgP92PICq2Vtk_teB2Ml7S5oMvOvFYy7oP9xQmz7-I0JpDumrYw'

# Define the headers with the bearer token
headers = {
    'Authorization': f'Bearer {bearer_token}'
}

# Send a GET request to the URL with the headers
response = requests.get(url, headers=headers)
#print(response)
# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)
    # Extract data by finding specific HTML elements
    # For example, to extract all <a> tags with class 'link':
    #Company_name=soup.find_all('a',class_='hidden-nested-link')
    links = soup.find_all('div',class_='description__text description__text--rich')
    #print(links)
    # Print out the text content of each link
    #for link in links:
        #print(f'JOB-Title {link.text}')
        #url_des=link.get('href')
        #print(url_des)
    #strong_tags = links.find_all('strong')
    for tag in links:
        print(tag.get_text(separator='\n').strip())
        print('-' * 50)
        #print('JOB-Desc',link.get('href'))
else:
    print('Failed to retrieve data from the website.')