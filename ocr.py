from PIL import Image
from pytesseract  import image_to_string
from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import time
from selenium import webdriver

def getScreen(captchaLink):
	browser = webdriver.Chrome("C:\\Users\\j0tdr\\Downloads\\chromedriver_win32\\chromedriver.exe")
	browser.get(captchaLink)
	browser.save_screenshot('newCaptcha.jpg')
	browser.quit()

def cropImage():
	img = Image.open("newCaptcha.jpg")
	# img2 = img.crop((0, 20, 220, 80))
	img2 = img.crop((30, 20, 160, 80))
	img2.save("newCaptcha2.jpg")
	

def image(image):
	print("Starting..")
	start = "C:\\Users\\j0tdr\\Desktop\\code\\ocr\\ocr\\"
	image = start+image
	print(image)
	solved = str(image_to_string(Image.open(image)))
	print(solved)
	return solved

# C:\Users\j0tdr\AppData\Local\Tesseract-OCR

def getCaptcha():
	s = requests.Session()
	url= "http://www.nakedcph.com/commodity/5028-adidas-originals-yeezy-boost-350-v2"
	r  = s.post(url)
	soup = BeautifulSoup(r.text,"html.parser")

	captcha = soup.find('img',{'class':'securityimage-image'}).get('src')
	print(captcha)
	urllib.request.urlretrieve(captcha, "newCaptcha.jpg")
	return captcha

def main():
	# cropImage()
	captchaLink = getCaptcha()
	# getScreen(captchaLink)
	cropImage()
	solved = image('newCaptcha2.jpg')

	while solved == "":
		print("Could not solve, trying again...")
		time.sleep(1)
		captchaLink = getCaptcha()
		cropImage()
		solved = image('newCaptcha2.jpg')

	# os.remove("captcha.png")
# image("solve.jpg")
# screen()
main()