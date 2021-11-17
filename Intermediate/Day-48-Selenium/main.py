from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open a specified site
driver.get("https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=sr_1_6?keywords=instant+pot+duo+evo&qid=1636751087&qsid=144-7640419-4290527&sr=8-6&sres=B07W55DDFB%2CB08CF9C1LB%2CB01NBKTPTS%2CB06Y1MP2PY%2CB07VT23JDM%2CB00FLYWNYQ%2CB08DZ5TWLN%2CB077T9YGRM%2CB06Y1KP7YK%2CB07RCNHTLS%2CB082FZTJ53%2CB08CF8GMDQ%2CB07541XMKB%2CB08CF8J3M8%2CB08CF6PFZF%2CB08CF573K3&srpt=PRESSURE_COOKER")
price = driver.find_element_by_class_name("a-price a-text-price a-size-medium apexPriceToPay")

# driver.get("https://www.python.org")
# search_bar = driver.find_element_by_name('q')
# print(search_bar.tag_name)

print(price.text)
# driver.close()  # Closes an active tab
driver.quit()   # Quit the entire program