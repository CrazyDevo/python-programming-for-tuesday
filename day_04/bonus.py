from  selenium import webdriver
# open a Chrome browser
driver=webdriver.Chrome()
# maximize the window
driver.maximize_window()
# navigate to the page
driver.get("https://practice.cydeo.com")
# verify url contains cydeo
expected_in_url="cydeo"
actual_url=driver.current_url

if expected_in_url in actual_url:
    print("URL contains cydeo")
else:
    print("URL does not contain cydeo")

# verify title is Practice

expected_title=driver.title
actual_title=driver.title

if expected_title == actual_title:
    print("Title verification is PASSED")
else:
    print("Title verification is FAILED")

driver.close()
























































