from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.48"
}
firefox_options = Options()
firefox_options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"  # <-- Update this to your Firefox installation path
driver = webdriver.Firefox(executable_path="geckodriver.exe",options=firefox_options)
driver.get("https://efundi.nwu.ac.za/portal")


driver.maximize_window()
Login_Prompt = driver.find_element(By.CLASS_NAME,"Mrphs-login-Message")
Login_Prompt.click()

#driver.set_window_size(1920,1080)

Username = driver.find_element(By.CLASS_NAME,"required")
Username.send_keys()#this is where my student numbr would go

Password = driver.find_element(By.XPATH,"//*[@id='password']")
Password.send_keys()# This is where my password would go

Login = driver.find_element(By.CLASS_NAME,"btn-submit")
Login.click()

time.sleep(86400)


