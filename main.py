#perfect connection and no interruption
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
following_list = []
followers_list = []
handle = input()
driver = webdriver.Chrome("/Users/jasonmoses/Downloads/chromedriver")
username = "saturdayadam612@gmail.com"
password = "Harmonymane7"
driver.get(f"https://www.instagram.com/{handle}/")
sleep(2)
sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/span/a[1]/button').click()
sleep(4)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)
sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]/button').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
sleep(3)
count_followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span')
print(count_followers.text)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
sleep(4)
print("..............................")
print("FOLLOWERS")
print("..............................")
sleep(2)
cfs = count_followers.text.replace(',','')
print(cfs)
#Please remember cf means follwers count but intsagram does not keep perfect count
# of all its your followers and following so the best option is to add a offset to minus.
for k in range(int(cfs) - 30):
    sleep(0.7)
    followers = driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{k+1}]")
    followers_list.append(followers.text)
    if k%8 == 0:
        sleep(2)
        driver.execute_script('arguments[0].scrollIntoView(true);',  driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{k+1}]"))
        sleep(2)
    else:
        sleep(0.5)
        driver.execute_script('arguments[0].scrollIntoView(true);',  driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{k+1}]"))
print(followers_list)
sleep(1)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()
sleep(1)
count_following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span')
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
sleep(2)
print("..............................")
print(count_following.text)
print("FOLLOWING")
print("..............................")
sleep(2)
cf = count_following.text.replace(',','')
#Please remember cfs means follwers count but intsagram does not keep perfect count
# of all its your followers and following so the best option is to add a offset to minus.
print(cfs)
for j in range(int(cf) - 30):
    sleep(1)
    following = driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{j+1}]")
    following_list.append(followers2.text)
    if j%8 == 0:
        sleep(4)
        driver.execute_script('arguments[0].scrollIntoView(true);',  driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{j+1}]"))
        sleep(2)
    else:
        sleep(0.8)
        driver.execute_script('arguments[0].scrollIntoView(true);',  driver.find_element_by_xpath(f"/html/body/div[4]/div/div/div[2]/ul/div/li[{j+1}]"))
print(following_list)
scum_bags = list(set(followers_list) - set(following_list))
if scum_bags == []:
    print("everyone u follow followers back")
else:
    print("some people")
print(scum_bags)
print(len(scum_bags))
