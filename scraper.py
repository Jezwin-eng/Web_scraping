import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime
from config import ALERT_THRESHOLD
from alert import send_email_alert
service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)
driver.get("https://www.amazon.in")
time.sleep(3)
search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys("Laptops")
search_button = driver.find_element(By.ID,"nav-search-submit-button")
search_button.click()
time.sleep(5)
#driver.quit()
today = datetime.now().strftime("%Y-%m-%d")

result = driver.find_elements(By.XPATH,"//div[@data-component-type= 's-search-result']")
for item in result[:20]:
    try:
        title_element = item.find_element(By.TAG_NAME,"h2")
        product_name = title_element.text
        
    except:
        product_name = "N/A"   

    try:
        
        link_element = item.find_element(By.XPATH, ".//a[.//span[contains(@class, 'a-price')]]")
        product_link = link_element.get_attribute("href")
        if not product_link.startswith('http'):
            product_link = "https://www.amazon.in" + product_link if product_link.startswith('/') else "Link N/A"
    except Exception as e:
        product_link = f"Link Error: {str(e)}"

    try:
   
     symbol = item.find_element(By.CLASS_NAME,"a-price-symbol").text.strip()
     whole = item.find_element(By.CLASS_NAME,"a-price-whole").text.strip()
     product_price = f"{symbol}{whole}"
    except Exception as e:
     product_price = "Price N/A" 
     
     
         # Step 6: Print the result
    #print(f"Name: {product_name}")
    #print(f"Price: {product_price}")
    #print(f"Link: {product_link}")
    #print("-" * 40)  
    
    
    data = []
    data.append({
    "Date": today,
    "Name": product_name,
    "Price": product_price,
    "Link": product_link
     })
    df = pd.DataFrame(data)


    file_exists = os.path.isfile("laptop_prices.csv")


    df.to_csv("laptop_prices.csv", mode='a', index=False, header=not file_exists, encoding='utf-8-sig')


    print(" Data saved to laptop_prices.csv")
    
    
    try:
        numeric_price = int(product_price.replace('₹','').replace(',',''))
        if numeric_price < ALERT_THRESHOLD:
            print(f"🔔 Alert triggered: {product_name} - ₹{numeric_price}")
            send_email_alert(product_name,product_price,product_link)
    
    except Exception as e:
        print("❌ Email alert failed:", e)


