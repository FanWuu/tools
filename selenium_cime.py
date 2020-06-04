from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import sys
import argparse

path = r"D:\chromedriver.exe"
url = "http://10.42.3.210/"
user_name = 'admin'
passwd = 'ddzdh@798'

def browser():
    browsers = webdriver.Chrome(path)
    return   browsers

def login(browser):

    # http://10.172.246.227:8095/imsTaskService/imsTask/executeTask?sign=moJoa40Reux9umaCCX2_3ADwPVWlYVNktJMgeEhg7YiraitJPhGahnaJPYvX1SKI7a_b1Q3LsJYkb9gcEpwTNw--___1590842735225___8000400001___8000400001___8000400001___2___
    #打开网页
    browser.get(url)

    time.sleep(3)
    #输入密码
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/form/div/div/div[1]/input').send_keys(user_name)
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/form/div/div/div[2]/input').send_keys(passwd)
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/div/form/div/div/input').click()
    time.sleep(3)
    # 进入e文件生成页面
    url_ims='http://10.42.3.210/#/efiles?sysId=8000600001&sonid=8000600145'
    browser.get(url_ims)
    time.sleep(3)
def get_logs(browser):
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[1]/div[1]/div[2]/div/div[1]/p').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[2]/select/option[3]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[3]/button').click()

def get_cime(browser):
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[1]/div[1]/div[2]/div/div[1]/p').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[2]/select/option[2]').click()
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[3]/button').click()

def get_tariff( browser , startime, endtime  ):
    start_time=startime[0:2]+'-'+startime[2:5]
    end_time=endtime[0:2]+'-'+endtime[2:5]
    #print(start_time,end_time)

    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[1]/div[1]/div[2]/div/div[1]/p').click()
    time.sleep(1)
    #修改开始时间
    begin_time_tag=browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[3]/div/input[1]')
    begin_time_tag.send_keys(5*Keys.BACKSPACE)
    begin_time_tag.send_keys(start_time)
    time.sleep(3)
    #修改结束时间
    end_time_tag=browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[3]/div/input[2]')
    end_time_tag.send_keys(5*Keys.BACKSPACE)
    end_time_tag.send_keys(end_time)
    time.sleep(3)
    #确认提交
    browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[4]/button').click()
    #选择计量点档案
    # browser.find_element_by_xpath('//*[@id="app"]/div[2]/main/div/div[2]/div/div/p[2]/select/option[2]').click()
def time_arg():
    parser=argparse.ArgumentParser()
    parser.add_argument('-m','-model', choices=['cime' ,'tariff' , 'meterlog' ],required=True,type=str ,help='输入需要生成的文件类型  cime：计量点档案 ，tariff：日冻结 ，meterlog:换表记录')
    parser.add_argument('-s','-start_time',required=True,type=str ,help='输入开始时间  例如：-s 0501')
    parser.add_argument('-e','-end_time',required=True,type=str , help='输入结束时间  例如：-e 0501')
    parser.add_argument('-example' , help='举例 ： python  ./selenim_cime.py  -m tariff -s 0501 -e 0501 ')
    args = parser.parse_args()
    return  args.m , args.s ,args.e

def main():
    times=time_arg()  #时间
    a=browser() # 打开浏览器
    login(a)    # 登录
    if times[0]=='cime':
        get_cime(a)
    if times[0]=='meterlog':
        get_logs(a)
    if  times[0]=='tariff':
        get_tariff(a, times[1] ,times[2] )  #生成e文件
    time.sleep(10)
    a.quit()  # 关闭浏览器


if __name__ == '__main__':
    main()

