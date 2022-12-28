# !python3
# followingListsMaker.py - Makes a list of following and followers of a specific profile

# IMPORT LIBRARIES
import datetime, time, random, os, csv
import pyautogui as pt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
chromeoptions = Options()

# INITIALIZE ICONS
followers_btn = 'followers.png'
following_btn = 'following.png'
x_btn = 'x.png'

"""
ALL FUNCTIONS--------------------------------------------------------------------
"""
def click_icon(img):
    pt.click(pt.center(pt.locateOnScreen(img)))

###############################################
##followers = []
##Links = []
##names = []
##def infoFollowers(iteration):    # ACCOUNT INFO FUNCTION FOR FOLLOWERS
##    stringPart = "//li["+ str(iteration) + "]"
##    follower = driver.find_element_by_xpath(stringPart +"//div[1]/span/a")
##    link = follower.get_attribute('href')
##    name = driver.find_element_by_xpath(stringPart + "//div[2]/div[2]").text
##    follower = follower.text
##    followers.append(follower)
##    Links.append(link)
##    names.append(name)
##    
####    followersCsvFileWriter.writerow([iteration,follower,name,link])
##    print(iteration,follower, name,link)
##    print("")
##    time.sleep(1)

##############################################

followings = []
links = []
fnames = []
##def info(iteration):    # ACCOUNT INFO FUNCTION FOR FOLLOWERS
##    stringPart = "//li["+ str(iteration) + "]" //li[110]//div[1]/span/a
##    following = driver.find_element_by_xpath(stringPart +"//div[1]/span/a")
##    link = follower.get_attribute('href')
##    name = driver.find_element_by_xpath(stringPart + "//div[2]/div[2]").text
##    following = following.text
##    followings.append(following)
##    links.append(link)
##    fnames.append(name)
##    
####    followersCsvFileWriter.writerow([iteration,follower,name,link])
##    print(iteration,following, name,link)
##    print("")
##    time.sleep(1)

#############################################   
##print('Enter the name => ')
##nameInit = input()

# LOG INTO INSTAGRAM
geckoDriverPath = os.getcwd()
##driver = webdriver.Firefox()
start = datetime.datetime.now()
driver = webdriver.Chrome(options=chromeoptions,executable_path=str(geckoDriverPath)+'\\chromedriver.exe')
driver.get('http://www.instagram.com/')

# CREDENTIALS
myEmail = 'sasikapamith2016@gmail.com'
myPassword = 'fRqbiHJP2V!j,QA'

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys(myEmail)
password.send_keys(myPassword)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
print("Log in completed...")

# DISMISS THE NOTIFICATIONS
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
print('Dismissed Notifications...')

# GO TO THE SPECIFIC PROFILE

profile_link = "https://www.instagram.com/apoorwa_jayawarna/"
driver.get(profile_link)
time.sleep(2) # wait 2 second



# GET THE LENGTH OF FOLLOWING & FOLLOWERS LIST

noFollowers = driver.find_element_by_xpath("//main//li[2]/a/span").text
noFollowers = int(noFollowers)
print(noFollowers,'followers')
noFollowing = driver.find_element_by_xpath("//main//li[3]/a/span").text
noFollowing = int(noFollowing)
print(noFollowing,'following')
print("")

##"""
##FOLLOWERS LIST-------------------------------------------------------------
##"""
##    
click_icon(following_btn)


time.sleep(2)

# CLICK RELETIVE TO THE X BUTTON
m = pt.center(pt.locateOnScreen(x_btn))
n = (m[0]-150,m[1]+200)
pt.click(n)

# PRESS 'END' FOR 10 SECONDS ( LOAD THE LIST )
##for i in range(int(int(noFollowing)/8)):
##    pt.keyDown('end')
##    pt.click(n)
##    time.sleep(3)
##    pt.keyUp('end')

##pt.keyUp('home')
##pt.keyDown('home')

### MAKE A CSV FILE
####followersCsv = open('followers_%s.csv'%nameInit,'w',newline='')
####followersCsvFileWriter = csv.writer(followersCsv)
####followersCsvFileWriter.writerow(['no','follower','name','profile_link'])
##    
### WHILE TRUE WRITE TO THE CSV FILE ABOUT THE DETAILS OF EACH PROFILE IN EACH ITERATION
for i in range(1,noFollowing+1):
    try:
        info(i)
        time.sleep(0.25)
    except:
        pass
##
### CLOSE THE CSV FILE
####followersCsv.close()
##
### CLOSE THE FOLLOWERS INSTAGRAM PAGE
##pt.click(m)
##time.sleep(2)
print('Followings List done!')

##
##
##"""
##FOLLOWING LIST-------------------------------------------------------------
##"""
##    
##click_icon(following_btn)
##
##
##time.sleep(2)
##
## CLICK RELETIVE TO THE X BUTTON
##m = pt.center(pt.locateOnScreen(x_btn))
##n = (m[0]-150,m[1]+200)
##pt.click(n)
##
## PRESS 'END' FOR 10 SECONDS ( LOAD THE LIST )
##for i in range(int(int(noFollowers)/8)):
##    pt.keyDown('end')
##    pt.click(n)
##    time.sleep(3)
##    pt.keyUp('end')
##
##pt.keyUp('home')
##pt.keyDown('home')
##
## MAKE A CSV FILE
##followersCsv = open('followers_%s.csv'%nameInit,'w',newline='')
##followersCsvFileWriter = csv.writer(followersCsv)
##followersCsvFileWriter.writerow(['no','follower','name','profile_link'])
##    
## WHILE TRUE WRITE TO THE CSV FILE ABOUT THE DETAILS OF EACH PROFILE IN EACH ITERATION
##
##for i in range(1,noFollowing+1):
##    try:
##        info(i)
##        time.sleep(0.25)
##    except:
##        pass

# CLOSE THE CSV FILE
##followersCsv.close()

# CLOSE THE FOLLOWERS INSTAGRAM PAGE
##pt.click(m)
time.sleep(2)
print('Followers List done!')
print(len(followings), 'following')
print(len(links))
print(len(fnames))
