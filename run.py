from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as Exceptions

driver = webdriver.Firefox(firefox_binary='C:\\Program Files\\Mozilla Firefox\\firefox.exe')
wait = WebDriverWait(driver=driver, timeout=5)

base_url = "https://anilist.co/"
url_check = base_url + "user/"
url_free = base_url + "404/"

with open("usernames.txt") as file:
    usernames = file.readlines()
    for user in usernames:
        driver.get(url_check+user)
        url = driver.current_url
        try:
            wait.until(EC.url_to_be(url_free))
            print(f'{url} is free')
            with open("free_names.txt", "a") as f:
                f.write(url + "\n")
        except Exceptions.TimeoutException:
            print(f'{url} is not free')
