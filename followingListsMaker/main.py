import itertools

from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import datetime, time, random, os, csv
import pyautogui as pt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
options = Options()

def login(driver):
    username = "sasikapamith2016@gmail.com"  # <username here>
    password = "fRqbiHJP2V!j,QA"  # <password here>

    # Load page
    driver.get("https://www.instagram.com/accounts/login/")
    sleep(3)
    # Login
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    submit = driver.find_element_by_tag_name('form')
    submit.submit()

    # Wait for the user dashboard page to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "See All")))


def scrape_followers(driver, account):
    # Load account page
    driver.get("https://www.instagram.com/{0}/".format(account))

    # Click the 'Follower(s)' link
    # driver.find_element_by_partial_link_text("follower").click
    sleep(2)
    driver.find_element_by_partial_link_text("follower").click()

    # Wait for the followers modal to load
    waiter.find_element(driver, "//div[@role='dialog']", by=XPATH)
    allfoll = int(driver.find_element_by_xpath("//li[2]/a/span").text)
    # At this point a Followers modal pops open. If you immediately scroll to the bottom,
    # you hit a stopping point and a "See All Suggestions" link. If you fiddle with the
    # model by scrolling up and down, you can force it to load additional followers for
    # that person.

    # Now the modal will begin loading followers every time you scroll to the bottom.
    # Keep scrolling in a loop until you've hit the desired number of followers.
    # In this instance, I'm using a generator to return followers one-by-one
    follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
    for group in itertools.count(start=1, step=12):
        for follower_index in range(group, group + 12):
            if follower_index > allfoll:
                raise StopIteration
            yield waiter.find_element(driver, follower_css.format(follower_index)).text

        # Instagram loads followers 12 at a time. Find the last follower element
        # and scroll it into view, forcing instagram to load another 12
        # Even though we just found this elem in the previous for loop, there can
        # potentially be large amount of time between that call and this one,
        # and the element might have gone stale. Lets just re-acquire it to avoid
        # tha
        last_follower = waiter.find_element(driver, follower_css.format(group+11))
        driver.execute_script("arguments[0].scrollIntoView();", last_follower)


if __name__ == "__main__":
    account = "apoorwa_jayawarna"  # <account to check>
    geckoDriverPath = os.getcwd()
    driver = webdriver.Chrome(chrome_options=options,executable_path=str(geckoDriverPath)+'\\chromedriver.exe')
##    driver.get('http://www.instagram.com/')
    try:
        login(driver)
        print('Followers of the "{}" account'.format(account))
        for count, follower in enumerate(scrape_followers(driver, account=account), 1):
            print("\t{:>3}: {}".format(count, follower))
    finally:
        driver.quit()
