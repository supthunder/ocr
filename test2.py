from selenium import webdriver
browser = webdriver.Chrome("C:\\Users\\j0tdr\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get('http://www.google.com/')
browser.save_screenshot('screenie.png')
browser.quit()