import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from wordcloud import WordCloud

# CREATE a web driver to access indeed.com and scrape the data from the first page.
s = Service('C:/Users/Natalie Fletcher/Dropbox (CSL)/Natalie Folder/Arden/Python/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)

# SET the variables for 'next buttons' at the bottom of the page
next_button_page_one = '//*[@id="resultsCol"]/nav/div/ul/li[6]/a'
next_button_two = '//*[@id="resultsCol"]/nav/div/ul/li[7]/a'
actions = ActionChains(driver)
URL = 'https://uk.indeed.com/jobs?q&l=Preston%2C%20Lancashire&vjk=ba2a57eca5a1f7de'
driver.get(URL)


company_names_list = []

# FIND the element by name of 'companyName' scrape and append into a list
company_names = driver.find_elements(By.CLASS_NAME, 'companyName')
for company_name in company_names:
    company_names_list.append(company_name.text)

# CREATE reference of next page button
Next_Button_Ref = driver.find_element(By.XPATH, next_button_page_one)

# USE action to move page to element(next button)
actions.move_to_element(Next_Button_Ref).perform()
# CLICK Accept button on cookies popup
driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
# CLICK next page button
driver.find_element(By.XPATH, next_button_page_one).click()
# WAIT 15 for popup to appear
driver.implicitly_wait(15)
# CLICK X button on popup
driver.find_element(By.XPATH, '//*[@id="popover-x"]/button').click()

# CREATE a while loop to repeat the scrape and append,
# FIND the 'next' button, scroll to the next button and click to navigate to next page until list is over 500 rows
while len(company_names_list) < 500:
    scraped_companies = driver.find_elements(By.CLASS_NAME, 'companyName')
    for company_name in scraped_companies:
        company_names_list.append(company_name.text)
    next_button_ref_two = driver.find_element(By.XPATH, next_button_two)
    actions.move_to_element(next_button_ref_two).perform()
    driver.find_element(By.XPATH, next_button_two).click()

# CLEAN data set, removing special characters and standardising the text to 'Title' format
cleaned_company_names_list = []

for company_name in company_names_list:
    company_name = company_name.replace(r'\W', '')
    company_name = company_name.replace(r'NaN', '')
    company_name = company_name.strip().title()
    cleaned_company_names_list.append(company_name)

# CREATE two lists, 1 of company's advertising roles, 2 count of repetitions
seen = set()
company_result = []
count_result = []
for item in cleaned_company_names_list:
    if item not in seen:
        seen.add(item)
        LocalCountResult = cleaned_company_names_list.count(item)
        if LocalCountResult > 3:
            company_result.append(item)
            count_result.append(cleaned_company_names_list.count(item))

# SET the header names on each column
d = {'Company Name': company_result, 'Count': count_result}

# CREATE df and save to CSV
df = pd.DataFrame(d)
df.to_csv('C:/Users/Natalie Fletcher/Desktop/Indeed_Company_Data.csv')

# GROUP companies by company name and provide count
new_list = list({i: cleaned_company_names_list.count(i) for i in cleaned_company_names_list})
# CONVERT list to string and generate wordcloud
unique_string = (' ').join(new_list)
wordcloud = WordCloud(width=500, height=500).generate(unique_string)
plt.figure(figsize=(15, 8))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('Word_Cloud_Graph' + '.png', bbox_inches='tight')


# TRUNCATE the length of the titles (x) to <=20
def trunc_string(company_strings):
    truncated_strings = []
    for business_name in company_strings:
        truncated_strings.append(business_name[0:20])
    return truncated_strings


company_column = d['Company Name']
x = trunc_string(company_column)

# CREATE a horizontal bar chart
fig, ax = plt.subplots()
y = d['Count']
plt.ylabel('Company Name', fontsize=10)
plt.xlabel('Count', fontsize=10)
x_pos = np.arange(len(x))
height = y
plt.barh(x, y, color=(0.1, 0.1, 0.1, 0.1), edgecolor='blue')

# CREATE pie chart
fig, ax = plt.subplots()
ax.pie(y, autopct='%1.0f%%')
ax.set_title('Companies Advertising')
ax.legend(d['Company Name'], loc='upper right')
ax.axis('equal')
plt.tight_layout()
plt.show()

# CREATE donut chart
plt.pie(y, labels=company_result, autopct='%1.1f%%', pctdistance=0.85)
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Companies Advertising')
plt.show()
