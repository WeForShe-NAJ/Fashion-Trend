from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

wait = WebDriverWait(driver, 30)

urls = [
        "https://www.myntra.com/women-kurtas-kurtis-suits?sort=popularity",#3000
     "https://www.myntra.com/women-shorts?sort=popularity",
    "https://www.myntra.com/women-jackets-coats?sort=popularity",
     "https://www.myntra.com/top?sort=popularity",#2000
    "https://www.myntra.com/dresses?sort=popularity",#3000
     "https://www.myntra.com/women-trousers?sort=popularity",
    "https://www.myntra.com/women-jeans?sort=popularity",#600
     "https://www.myntra.com/women-ethnic-wear?sort=popularity",#8000
      "https://www.myntra.com/saree?sort=popularity",#4000

]

for url in urls:
    driver.get(url)
    wait.until(EC.url_to_be(url))

    title = driver.find_element(By.CLASS_NAME, "title-title")
    print(title.text)
    
    count = 0
    arr = []
    while count < 250:
        soup = BeautifulSoup(driver.page_source, 'lxml')
        links = soup.find_all("li", attrs={"class": "product-base"})
        print(len(links))
        
        for link in links:

            #URL
            product_url = link.find('a').get('href')

            #Discount
            discount = link.find('span', attrs={"class": 'product-discountedPrice'})
            discount = discount.getText() if discount else None

            #Brand
            brand  = link.find('h3',attrs={"class":'product-brand'})
            # print(brand)
            # exit()
            brand=brand.getText()
            # Item
            item  = link.find('h4',attrs={"class":'product-product'})
            item = item.getText()
            # MRP
            mrp = link.find('span', attrs={"class": 'product-strike'})
            mrp = mrp.getText() if mrp else None

            # NumberREviews
            # reviews = link.find('div', attrs={"class": 'product-ratingsCount'})
            # reviews = reviews.getText() if reviews else None
            #  
            #Rating
            rating = link.find('div', attrs={"class": 'product-ratingsContainer'})
            reviews=rating.getText().split("|")[1] if rating else None
            rating = rating.getText().split("|")[0] if rating else None
            arr.append({"URL": product_url, "Discount": discount, "Rating": rating,"Brand":brand,"Item":item,"MRP":mrp,"Reviews":reviews})

        try:
            product = driver.find_element(By.CLASS_NAME, "pagination-paginationMeta")
            print(product.text)

            next_button = driver.find_element(By.CLASS_NAME, "pagination-next")
            if "pagination-disabled" in next_button.get_attribute("class"):
                print("No more pages left.")
                break
            next_button.click()
            time.sleep(3)
            print("------------------------------------------------------")
            count += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    header=['URL','Discount','Rating','Brand','Item','MRP','Reviews']
    name=url.split("/")[-1].split("?")[0]+".csv"
    with open(name,"a", encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)

    # writing headers (field names)
        writer.writeheader()

    # writing data rows
        writer.writerows(arr)
    # exit()

driver.quit()

