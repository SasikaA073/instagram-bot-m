#! python3
# instabot.py - developed by Sasika Amarasinghe in order to chat ******


import datetime, time, random, pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

start = datetime.datetime.now()

# login Info
myEmail = input('Enter your user name here...> ')
myPassword = input('Enter your password here...> ')


#driver = webdriver.Chrome()
driver.get('http://www.instagram.com/')



### login page
##browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(myEmail)
##
##browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(myPassword)
##
##browser.find_element_by_css_selector('button[type=submit]').click()
##

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()
username.send_keys(myEmail)
password.send_keys(myPassword)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
print("Log in completed...")

not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Not Now')]"))).click()
print('Dismissed Notifications...')

# Choose the chat
profile_link = input('Enter the profile url...> ')
driver.get(profile_link)
message_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']"))).click()
print('Entered the chat successfully...')

# Enter the message you want to send

messages = ['Hi',"Hello!",'Hey']
def chat(message):
    mbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
    mbox.clear()
    for letter in message:
        mbox.send_keys(letter)
    mbox.send_keys(Keys.RETURN)

name = " "
time.sleep(10)
chat(random.choice(messages)+ name )
print('n/Successfully sent the message....')

# send likes
def like():
    y = driver.find_elements_by_xpath("//button[@class]/div[@class='QBdPU ']")
    y[4].click()

like()
print('Sending a like...')

# Now check the reply

"""
Here, I am going to use pyautogui
"""

def click_icon(img):
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(img)))
    time.sleep(2)



# Declare icons to be used 
replies = ['Hello.png','hello_simple.png','Hey.png','hey_simple.png','Hi.png','hi_simple.png']

heart = '/Icons/heart.png'
triplt_dot = '/Icons/three_dots.png'
image_send_icon = '/Icons/image_send.png'
copy_message = '/Icons/insta_copy.png'
smiley = '/Icons/insta_smiley.png'
reply_message = 'reply.png'

x = False
time.sleep(3)

##m = []    
##for i in replies:
##	z = pyautogui.locateOnScreen(i)
##	m.append(z)
##	click_icon(i)

# Reply the message

n = []
time.sleep(3)
x = False




def replyFirst():        
    for i in range(len(replies)):
        q = pyautogui.locateOnScreen(replies[i])
        try:
            q.click()
        except:
            pass
        n.append(q)
        
        if n[-1] != None:
            w = list(q)
            x = w[0] + w[2]/2
            y = w[1] + w[3]/2
            a = pyautogui.moveTo(x, y, duration = 0.5)
            b = pyautogui.locateOnScreen(reply_message)
            c = list(b)
            pyautogui.moveTo(c[0],c[1],duration=0.5)
            pyautogui.click()
            time.sleep(2)
            chat('This is the first time that you greet me')
        n.pop()
        break
time.sleep(5)
while True:
    replyFirst()
""" 
### TEST_CODES

click_icon('insta_smiley.png')



time.sleep()
print('Sending a like')
"""
    
"""
##reply = driver.find_elements_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[1]/div/div/div[11]/div[2]/div/div/div/div/div/div/div/div/span')
##Replies = []
##Replies.append(reply)
##return(Replies)



//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea



# Login
##emailElem = browser.find_elements_by_id('_2hvTZ pexuQ zyHYP')
##emailElem.send_keys(myEmail)
##passElem = browser.find_elements_by_id('_2hvTZ pexuQ zyHYP')
##passElem.send_keys(myPassword)
##
##passElem.submit()

# 
"""
print("Processing time: " + str(datetime.datetime.now()-start))

def get_messages():
    time.sleep(2)
    position = pyautogui.locateOnScreen('insta_smiley.png',confidence=9)
    pyautogui.moveTo(position[0:2],duration=.5)
    pyautogui.moveRel(50, -50, duration=.5)
    pyautogui.click()

    # Click on the three dot
    position = pyautogui.locateOnScreen('insta_smiley.png',confidence=9)
    pyautogui.moveTo(position[0:2],duration=.5)
    pyautogui.click()


