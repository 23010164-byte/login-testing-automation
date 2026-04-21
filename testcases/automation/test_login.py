from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com/login")

print("Open login page successfully")
driver.quit()
