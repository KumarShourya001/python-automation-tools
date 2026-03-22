#Scrape Content from Dynamic Websites
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import  By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



chrome_options=Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(
    "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.265 Safari/537.36"
)
driver = webdriver.Chrome(options=chrome_options)
url=("https://www.naukrigulf.com/top-jobs-by-designation")

driver.get(url)
WebDriverWait(driver,30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"soft-link")))

html=driver.page_source
soup = BeautifulSoup(html,"html.parser")
job_profile=soup.find_all('a',"soft-link")

for i , job in enumerate(job_profile[:10],start=1):
    print(f"{i}.{job.text.strip()}")

driver.quit()