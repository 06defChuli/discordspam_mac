import sys
import subprocess
import os

#implement pip as a subprocess:
try:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException  
except ImportError as er:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException  
import time, keyboard
import pathlib

def pprint(text):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.02)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
wd = str(pathlib.Path(__file__).parent.resolve())
path = 'chromedriver.exe'
driver = webdriver.Chrome(wd + '/' + path) 



class User():
    def login(self, username, password):
        global driver
        try:
            if driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[1]/div'):
                pass
        except NoSuchElementException:
            driver.get('https://discord.com/login')
            time.sleep(4.5)
            user = driver.find_element_by_name('email')
            passw = driver.find_element_by_name('password')
            user.send_keys(username)
            time.sleep(1)
            passw.send_keys(password)
            login = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]/div')
            time.sleep(1)
            login.click()
            time.sleep(5)
            try:
                clear = driver.find_element_by_xpath('/html/body/div/div[6]/div/div/div/div/button')
                clear.click()
            except:
                pass
            if driver.current_url != 'https://discord.com/channels/@me':
                pprint('Oh no, something went wrong. \nPlease make sure you have the right information.\n')
                createUser()
                toe.login(credentials[1].strip(), credentials[2].strip())  
            try:
                folders = driver.find_elements_by_class_name('closedFolderIconWrapper-2sTcE6')
                for elem in folders:
                    elem.click()
            except:
                pass
            print('Logged in!')      
    def spamUser(self):
        global driver
        os.system('clear')
        pprint('What user will you be spamming?\n')
        users = input()
        pprint('What will you message be?\n')
        msg = input()
        pprint('How many times will you send this message?\n')
        amount = int(input())
        user = driver.find_element_by_css_selector('.clickable-1JJAn8[aria-label="' + str(users) + ' (direct message)"]')
        user.click()
        text_box = driver.find_element_by_css_selector('.fontSize16Padding-3Wk7zP[aria-label="Message @' + users + '"]')
        msg_sent = 0
        while msg_sent != amount:
            text_box.send_keys(str(msg))
            text_box.send_keys(Keys.ENTER)
            time.sleep(1.5)
            msg_sent += 1
            print('Messages sent:' + str(msg_sent))
            if msg_sent == amount:
                break
    def spam(self, amount): #Add functions which finds all server names for you to then click on
        os.system('clear')
        global driver
        servorder = 0
        pprint('Please chose which server to spam.\n')
        sheesh = driver.find_elements_by_class_name('wrapper-1BJsBx')
        for elem in sheesh:
            servorder += 1
            try:
                if elem.get_attribute('aria-label') == 'Home':
                    pass
                else:
                    print(str(servorder) + '. ' + elem.get_attribute('aria-label'))
            except NoSuchElementException:
                pass
        while True:
            server_choice = input('\n')
            try:
                choice = int(server_choice) - 1
                try:
                    sheesh[choice].click()
                    break
                except NoSuchElementException:
                    pprint('Please enter a valid number.\n')
                    continue
            except ValueError as er:
                pprint('Please enter a valid input.')
                continue
        try:
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[3]/button').click()
        except NoSuchElementException:
            pass
        """pprint('What is the name of the server?\n')
        server_name = input()
        if driver.find_element_by_css_selector('.wrapper-1BJsBx[aria-label="  ' + str(server_name) + '"]'):
            pass
        else:
            pprint('Oh no. Something went wrong, please make sure you have the exact server name.')
            menu()
        server = driver.find_element_by_css_selector('.wrapper-1BJsBx[aria-label="  ' + str(server_name) + '"]')
        server.click()"""
        #pprint('What is the name of the channel?\n')
        #channel_name = input()
        channel = driver.find_elements_by_xpath('//*[@id="channels"]/div/div')
        channel.pop(0)
        order = 0
        os.system('clear')
        pprint('Please chose a text channel.\n')
        for elem in channel:
            try:
                find_tag = driver.find_element_by_xpath('//*[@id="channels"]/div/div' + '[' + str(channel.index(elem) + 1) + ']' + '/div/div')
                if find_tag.get_attribute('class') == 'content-1x5b-n':
                    try:
                        find_name = driver.find_element_by_xpath('//*[@id="channels"]/div/div' + '[' + str(channel.index(elem) + 1) + ']' + '/div/div/a')
                        order += 1
                        print(str(order) + '. ' + str(find_name.get_attribute('aria-label')))
                    except NoSuchElementException:
                        pass
            except NoSuchElementException:
                pass
        while True:
            order_input = input('\n')
            try:
                bruh = int(order_input) + 1
                clickable = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/div/div/div[1]/nav/div[4]/div/div' + '[' + str(bruh) + ']' + '/div')
                clickable.click()
            except ValueError as er:
                pprint('Oh no, something went wrong. Please enter a valid input.\n')
                print('Issue: ' + str(er))
            time.sleep(0.5)
            try:
                text = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/main/form/div[1]/div/div/div[1]/div/div[3]/div[2]')
                break
            except NoSuchElementException:
                pprint('This text channel seems to be off limits. Please try a text channel you are allowed to use.\n')
                continue
        
        pprint('What message would you like to spam?\n')
        message = input()
        msg_sent = 0
        while msg_sent != amount:
            text.send_keys(message)
            time.sleep(0.5)
            text.send_keys(Keys.ENTER)
            time.sleep(1)
            msg_sent += 1
            print('Messages sent: ' + str(msg_sent))
            continue
        menu()
"""        text.send_keys('Sus')
        text.send_keys(Keys.ENTER)
        msg_sent = 0
        while msg_sent != amount:
            cooldown = 0
            msg_sent += 1
            while cooldown != 10:
                time.sleep(1.3)
                text.send_keys('Sus')
                time.sleep(0.2)
                text.send_keys(Keys.ENTER)
                cooldown += 1
                if cooldown > 9:
                    keyboard.press_and_release('enter')
                    break
                else:  
                    continue
            time.sleep(1.3)
            text.send_keys('~grab')
            time.sleep(0.2)
            text.send_keys(Keys.ENTER)
            print(f'Loops sent: {msg_sent}')"""

os.system('clear')
credentials = []
user_file = open('./user.txt', 'r+')

def createUser():
    user_file.seek(0)
    user_file.truncate(0)
    credentials.clear()
    pprint('What is your name?\n')
    use = input()
    credentials.append(use)
    user_file.write(str(use) + '\n')
    pprint('What is your email or phone number? (For discord login)\n')
    email = input()
    credentials.append(email)
    user_file.write(str(email) + '\n')
    pprint('What is your discord password?\n')
    dsc_pass = input()
    credentials.append(dsc_pass)
    user_file.write(dsc_pass)
    os.system('clear')

for each_line in user_file.readlines():
    credentials.append(each_line.strip())
if len(credentials) == 0:
    createUser()


try:
    toe = str(credentials[0])
except IndexError or TypeError as er:
    pprint('There seems to be an error, please rewrite your user information.\n')
    print('Issue: ', str(er))
    createUser()
toe = User()

def ifLogged():
    pprint('What would you like to do now?\n')
    print("""   1. Spam a user(direct messages)
    2. Spam a server text channel
    3. Quit program
        """)
    spam_type = input()
    if spam_type == '2':
        pprint('How many times do you want to spam your message?')
        while True:
            ammount = input()
            try:
                toe.spam(int(ammount))
                break
            except ValueError as er:
                pprint('Oh no something went wrong.')
                print('Issue: ', er)
                print('Please type a number for the amount of messages you want to send.')
    elif spam_type == '1':
        toe.spamUser()
    elif spam_type == '3':
        print('Quitting...')
        quit()
    elif driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[1]/div/div[2]/div/svg/foreignObject/div/div'):
        pprint('What would you like to do now?')
        print("""   1. Spam a user(direct messages)
        2. Spam a server text channel
        3. Quit program
        """)

def menu():
    os.system('clear')
    try:
        if driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/nav/ul/div[2]/div[1]/div'):       
            ifLogged()
    except NoSuchElementException:
        pprint('Welcome, ' + credentials[0].strip() + '. What would you like to do?\n')
        time.sleep(0.5)
        print("""    1. Login
    2. Rewrite user info
    3. Quit""")

        func = input()
        if func == '1':
            try:
                os.system('clear')
                print('Logging in...')
                toe.login(credentials[1].strip(), credentials[2].strip())
                pprint('What would you like to do now?\n')
                print("""    1. Spam a user(direct messages)
    2. Spam a server text channel
                    """)
                spam_type = input()
                if spam_type == '2':
                    os.system('clear')
                    pprint('How many times do you want to spam your message?\n')
                    while True:
                        ammount = input()
                        try:
                            toe.spam(int(ammount))
                            break
                        except ValueError as er:
                            pprint('Oh no something went wrong.')
                            print('Issue: ', er)
                            print('Please type a number for the amount of messages you want to send.')
                elif spam_type == '2':
                    toe.spamUser()
            except IndexError or TypeError as er:
                pprint('There seems to be an error, please rewrite your user information.\n')
                print('Issue -> ', str(er))
                createUser()
                menu()
        elif func == '2':
            createUser()
        elif func == '3':
            pprint('Quitting program...')
            quit()
        else:
            pprint('Please enter a valid input')
            menu()
time.sleep(5)
os.system('clear')
menu()