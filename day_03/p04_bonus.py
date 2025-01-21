from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

print(driver.title)
print(driver.current_url)

driver.quit()
