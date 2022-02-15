from bs4 import BeautifulSoup
import requests
import time

def find_jobs():#searchChoice, familiar_skill):
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs): #enumerate function enable to iterate over the index of the job list and the content
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ','') #replace spaces ' ' with nothing ''
            skills = job.find('span', class_='srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href'] #['href] to receive the value of href attribute
            # print(company_name)
            # print(skills)
            # print(published_date)

            #if searchChoice == "1" or (searchChoice == "2" and familiar_skill in skills):
            with open(f'data/{index}.txt', 'w') as f:
                f.write(f"Company name: {company_name.strip()}\n") 
                #strip() is py function, can be used inside {}
                #strip() remove space and empty line
                f.write(f"Required skills: {skills.strip()}\n")
                f.write(f"Published data: {published_date}\n")
                f.write(f"More Info: {more_info}")
            print(f"File saved: {index}.txt")

if __name__ == "__main__" :  #scrap every 20 seconds
    while True:
        find_jobs()
        print(f"Waiting 20 seconds...\n\n")
        time.sleep(20)