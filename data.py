import pyautogui
import webbrowser
import pyperclip
import time
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Users\\Naman\\Desktop\\Scraper\\chromedriver.exe')

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://academicscc.vit.ac.in/student/stud_login_submit.asp')
alert_obj = driver.switch_to.alert
alert_obj.accept()



pyautogui.click(x=909,y=386)
pyautogui.typewrite('16BLC1030')
pyautogui.click(x=950,y=421)
pyautogui.typewrite('United@123')

driver.execute_script(open("C:\\Users\\Naman\\Desktop\\Scraper\\value.js").read())

day_of_month = datetime.datetime.now().day
week_number = (day_of_month - 1) // 7 + 1

data = [[1035,453],[1064,453],
		[1035,472],[1064,472],
		[1035,491],[1064,491],
		[1035,510],[1064,510],
		[1035,528],[1064,528]
]

for i in data:
	dat1 = data[week_number-1]
	dat2 = data[week_number]

for i in data:
	dat1 = data[week_number-1]
	dat2 = data[week_number]

x1 = dat1[0]
y1 = dat1[1]
x2 = dat2[0]
y2 = dat2[1]

pyautogui.click(x=863,y=531)#Login

time.sleep(5)#Sleep


pyautogui.click(x=76,y=720)#Hosteller
pyautogui.click(x=150,y=770)#Outing Request

time.sleep(2)

#############################################################################################################################
#######################################################SATURDAY##############################################################
#############################################################################################################################

pyautogui.click(x=900,y=348)#Approving Authority
pyautogui.click(x=868,y=371)#OUTING

time.sleep(1)

pyautogui.click(x=888,y=497)#Place and address
pyautogui.typewrite('Kellambakkam')

pyautogui.click(x=800,y=576)#Reason
pyautogui.typewrite('Shopping')

pyautogui.click(x=800,y=601)#Mobile Number
pyautogui.typewrite('9690479443')

pyautogui.click(x=800,y=621)#Parent Mobile Number
pyautogui.typewrite('9837031637')

pyautogui.click(x=800,y=667)#Faculty Number
pyautogui.typewrite('9840119868')

pyautogui.click(x=878,y=402)#Exit Date

pyautogui.click(x=x1,y=y1)#Date Selector

pyautogui.click(x=852,y=432)#Exit Time Hrs
pyautogui.click(x=821,y=552)

pyautogui.click(x=977,y=430)#Exit Time Min
pyautogui.click(x=958,y=460)

pyautogui.click(x=1002,y=428)#AM/PM

pyautogui.click(x=859,y=461)#Entry Time Hrs
pyautogui.click(x=832,y=554)

pyautogui.click(x=983,y=461)#Entry Time Min
pyautogui.click(x=960,y=490)

pyautogui.click(x=1052,y=456)#AM/PM

pyautogui.click(x=838,y=758)#Apply

#############################################################################################################################
#######################################################SUNDAY################################################################
#############################################################################################################################

time.sleep(4)

pyautogui.click(x=150,y=770)#Outing Request

time.sleep(2)

pyautogui.click(x=900,y=348)#Approving Authority
pyautogui.click(x=868,y=371)#OUTING

time.sleep(1)

pyautogui.click(x=888,y=497)#Place and address
pyautogui.typewrite('Kellambakkam')

pyautogui.click(x=800,y=576)#Reason
pyautogui.typewrite('Shopping')

pyautogui.click(x=800,y=601)#Mobile Number
pyautogui.typewrite('9690479443')

pyautogui.click(x=800,y=621)#Parent Mobile Number
pyautogui.typewrite('9837031637')

pyautogui.click(x=800,y=667)#Faculty Number
pyautogui.typewrite('9840119868')

pyautogui.click(x=878,y=402)#Exit Date

pyautogui.click(x=x2,y=y2)#Date Selector

pyautogui.click(x=852,y=432)#Exit Time Hrs
pyautogui.click(x=821,y=552)

pyautogui.click(x=977,y=430)#Exit Time Min
pyautogui.click(x=958,y=460)

pyautogui.click(x=1002,y=428)#AM/PM

pyautogui.click(x=859,y=461)#Entry Time Hrs
pyautogui.click(x=832,y=554)

pyautogui.click(x=983,y=461)#Entry Time Min
pyautogui.click(x=960,y=490)

pyautogui.click(x=1052,y=456)#AM/PM

pyautogui.click(x=838,y=758)#Apply