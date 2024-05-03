
import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
#url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=data%2Bscience&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&original_referer=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%3Fkeywords%3D%26location%3DUnited%2520States%26geoId%3D103644278%26f_TPR%3D%26f_JT%3DF%26position%3D1%26pageNum%3D0&start=20'

def job_fetch_data(b_t,job_name,location_val):
    data_comp = {}
    url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search'
    # Define the bearer token
    bearer_token = b_t
    # Define the headers with the bearer token
    headers = {
        'Authorization': f'Bearer {bearer_token}'
    }
    parmeter={"keywords":job_name,
              "location":location_val}

    # Send a GET request to the URL with the headers
    response = requests.get(url, headers=headers,params=parmeter)
    #print(response)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        #print(soup)
        # Extract data by finding specific HTML elements
        # For example, to extract all <a> tags with class 'link':
        Company_name=soup.find_all('a',class_='hidden-nested-link')
        links = soup.find_all('a', class_='base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]')
        #print(links)
        # Print out the text content of each link
        for com_nam,link in zip(Company_name,links):
            print(f' Company from {com_nam.text} JOB-Title {link.text}')
            url_des=link.get('href')
            #print(url_des)
            if com_nam.text not in data_comp:
                data_comp[com_nam.text] = []
            data_comp[com_nam.text].append(link.text)
            responsfinal = requests.get(url_des, headers=headers)
            # print(response)
            # Check if the request was successful (status code 200)
            if responsfinal.status_code == 200:
                # Parse the HTML content of the page using BeautifulSoup
                soufinal = BeautifulSoup(responsfinal.content, 'html.parser')
                # print(soup)
                # Extract data by finding specific HTML elements
                # For example, to extract all <a> tags with class 'link':
                # Company_name=soup.find_all('a',class_='hidden-nested-link')
                linkfinal = soufinal.find_all('div', class_='description__text description__text--rich')
                # print(links)
                # Print out the text content of each link
                # for link in links:
                # print(f'JOB-Title {link.text}')
                # url_des=link.get('href')
                # print(url_des)
                # strong_tags = links.find_all('strong')
                for tag in linkfinal:
                    final_des=tag.get_text(separator='\n').strip()
                    print('-' * 50)
                    # print('JOB-Desc',link.get('href'))
                    data_comp[com_nam.text].append(final_des)

            else:
                print('Failed to retrieve data from the website.')
        return data_comp
            #print('JOB-Desc',link.get('href'))
    else:
        print('Failed to retrieve data from the website.')
        return response


"""        response_desc = requests.get(url_des, headers=headers)
        if response_desc.status_code == 200:
            soup_des = BeautifulSoup(response_desc.content, 'html.parser')
            #print('Desc')#jobs-description__container jobs-description__container--condensed
            links_desc = soup_des.find_all('a', class_='jobs-description__container jobs-description__container--condensed')
            for linkZz in links_desc:
                print('JOB-Desc :', linkZz.text)
        else:
            print('Failed to retrieve data.')"""


#a=job_fetch_data('AQUlN-nEkFgrAioTvzkLHZkPQ_qyyyBJaV5VL5UbGngBitrKy2Ny0ijZW6hiyi_VSSjvSKpMfrOuIfgRyn_1Lp9EyFaMwWj6rg6ffiuqnXoGRxEeaAyNOCJZU8AdUw5IA1SWIaPNhaBib-NMffUCuFLCk0UgsGt6UYL2hZ4QuKyIJogpPGaSWTo8a-igYLTxZA3X2socD4QhsOsQf3DjycEm4WjksUdhe9txZ_tcZWCMwCZrn78iZlZNeG1lSsi3eE_iFkf8dQ6npCf5QQtvnxV_AXfznvqHl6I8NBpFq6AwgP92PICq2Vtk_teB2Ml7S5oMvOvFYy7oP9xQmz7-I0JpDumrYw','Data science','Bengaluru')

#print("DIC",a)