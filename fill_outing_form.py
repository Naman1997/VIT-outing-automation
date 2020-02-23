from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import datetime

def fill():
	#Selecting approving authority
	approving_auth = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[2]/select/option[2]")
	approving_auth.click()
	
	#Entering Place and address
	places = ['Tambaram','Egmore','Velacherry','Addiyar']
	place_value = random.choice(places)
	place_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[5]/td[2]/textarea")
	place_holder.send_keys(place_value)
	
	#Entering Reason
	reasons = ['Shopping','Project Work']
	reason_value = random.choice(reasons)
	reason_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[6]/td[2]/input")
	reason_holder.send_keys(reason_value)
	
	#Entering mobile number
	mobile_number = '#Your_Number'
	mobile_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[7]/td[2]/input")
	mobile_holder.send_keys(mobile_number)
	
	#Entering parent mobile number
	parent_number = '#Your_parent_number'
	number_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[8]/td[2]/input")
	number_holder.send_keys(parent_number)
	
	#Entering faculty mobile number
	faculty_number = '#Your_faculty_number'
	faculty_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[10]/td[2]/input")
	faculty_holder.send_keys(faculty_number)
	
	
def time_fill():
	#Fills exit and entry time as 8am and 6pm respectively
	
	#Fills 8:00
	exit_hrs = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[2]/td[2]/select[1]/option[9]")
	exit_min = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[2]/td[2]/select[2]/option[2]")
	exit_hrs.click()
	exit_min.click()

	#Fills AM
	exit_am = driver.find_element_by_xpath("//input[@type='radio' and @value='AM' and @name='frm_timetype']")
	exit_am.click()

	#Fills 6:00
	entry_hrs = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[3]/td[2]/select[1]/option[7]")
	entry_min = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[3]/td[2]/select[2]/option[2]")
	entry_hrs.click()
	entry_min.click()

	#Fills PM
	entry_pm = driver.find_element_by_xpath("//input[@type='radio' and @value='PM' and @name='to_timetype']")
	entry_pm.click()


day_of_month = datetime.datetime.now().day
week_number = (day_of_month - 1) // 7 + 1
week_number +=2
path1 ='//*[@id="calBorder"]/span/table/tbody/tr[2]/td/table/tbody/tr['+str(week_number)+']/td[6]'
			# //*[@id="calBorder"]/span/table/tbody/tr[2]/td/table/tbody/tr[5]/td[6]
path2 ='//*[@id="calBorder"]/span/table/tbody/tr[2]/td/table/tbody/tr['+str(week_number)+']/td[7]'

valve = int(input("2 for both saturday and sunday, 1 for saturday and 0 for sunday : "))
print(valve)
driver = webdriver.Chrome(executable_path='/home/ironheart/Documents/Github/VIT-outing-automation/chromedriver')

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://academicscc.vit.ac.in/student/stud_login_submit.asp')
alert_obj = driver.switch_to.alert
alert_obj.accept()

regno = driver.find_element_by_name("regno")
regno.send_keys("16BLC1030")


passw = driver.find_element_by_name("passwd")
passw.send_keys("United@123")


driver.execute_script(open("/home/ironheart/Documents/Github/VIT-outing-automation/value.js").read())

driver.find_element_by_name("passwd").send_keys(Keys.ENTER)

driver.get('https://academicscc.vit.ac.in/student/outing.asp')


if(valve == 2):
	fill()
	time_fill()

	controller = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[1]/td[2]/a/img")
	controller.click()
	time.sleep(2)

	#For this week's Saturday
	path_holder1 = driver.find_element_by_xpath(path1)
	path_holder1.click()
	
	#Apply button click
	apply_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[14]/td/input[1]")
	apply_holder.click()

	#Reset page
	driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[14]/td/input[2]").click()

	fill()
	time_fill()
	
	controller = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[1]/td[2]/a/img")
	controller.click()
	time.sleep(2)

	#For this week's Sunday
	path_holder2 = driver.find_element_by_xpath(path2)
	path_holder2.click()
	

	#Apply button click
	apply_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[14]/td/input[1]")
	apply_holder.click()
	

elif(valve == 1):
	fill()
	time_fill()

	controller = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[1]/td[2]/a/img")
	controller.click()
	time.sleep(2)
	
	#For this week's Saturday
	path_holder1 = driver.find_element_by_xpath(path1)
	path_holder1.click()

	#Apply button click
	apply_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[14]/td/input[1]")
	apply_holder.click()

elif(valve == 0):
	fill()
	time_fill()

	controller = driver.find_element_by_xpath("//*[@id='txtHint']/table/tbody/tr[1]/td[2]/a/img")
	controller.click()
	time.sleep(2)

	#For this week's Sunday
	path_holder2 = driver.find_element_by_xpath(path2)
	path_holder2.click()

	#Apply button click
	apply_holder = driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/form/table/tbody/tr[14]/td/input[1]")
	apply_holder.click()

else:
	print("ERROR!!!!!!!!!!!!")

