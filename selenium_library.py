from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import os
from . import config


print('setup driver started')
browser = WebDriver()
browser.get(config.url)


def teardown_driver():
    print('teardown driver started')
    global browser
    browser.close()


def create_acc():
    '''


    '''
    submit = browser.find_element_by_link_text("Sign in")
    submit.click()
    textarea = browser.find_element_by_xpath("//input[@id='email_create']")
    textarea.send_keys(config.email2)
    submit = browser.find_element_by_xpath("//button[@id='SubmitCreate']/span")
    submit.click()

    # browser.find_element_by_xpath("label[@class='top']").click()

    # textarea = browser.find_element_by_id("customer_firstname").click()
    # textarea.send_keys(config.first_name)
    #
    # textarea = browser.find_element_by_xpath("//input[@id='customer_lastname']")
    # textarea.send_keys(config.last_name)
    #
    # textarea = browser.find_element_by_xpath("//input[@id='passwd']")
    # textarea.send_keys(config.password)
    #
    # browser.find_element_by_xpath("select[@id='days']/option[text()= '5&nbsp;&nbsp']").click()


    # textarea = browser.find_element_by_xpath("//input[@id='email']")
    # textarea.send_keys(config.email)
    # textarea = browser.find_element_by_xpath("//input[@id='passwd']")
    # textarea.send_keys(config.password)
    # submit = browser.find_element_by_xpath("//button[@id='SubmitLogin']")
    # submit.click()
    # username = browser.find_element_by_tag_name("span").text
    return(text)

def login():
    '''


    '''
    submit = browser.find_element_by_link_text("Sign in")
    submit.click()
    textarea = browser.find_element_by_xpath("//input[@id='email']")
    textarea.send_keys(config.email)
    textarea = browser.find_element_by_xpath("//input[@id='passwd']")
    textarea.send_keys(config.password)
    submit = browser.find_element_by_xpath("//button[@id='SubmitLogin']")
    submit.click()
    username = browser.find_element_by_tag_name("span").text
    return(username)


def logout():
    '''


    '''
    submit = browser.find_element_by_link_text("Sign in")
    submit.click()
    textarea = browser.find_element_by_xpath("//input[@id='email']")
    textarea.send_keys(config.email)
    textarea = browser.find_element_by_xpath("//input[@id='passwd']")
    textarea.send_keys(config.password)
    submit = browser.find_element_by_xpath("//button[@id='SubmitLogin']")
    submit.click()
    submit = browser.find_element_by_xpath("//a[@class='logout']")
    submit.click()
    text = browser.find_element_by_link_text("Sign in").text
    return text


def forgot_pas():
    '''


    '''
    submit = browser.find_element_by_link_text("Sign in")
    submit.click()
    submit = browser.find_element_by_link_text("Forgot your password?")
    submit.click()
    textarea = browser.find_element_by_id("email")
    textarea.send_keys(config.email)
    submit = browser.find_element_by_xpath("//button[@class='btn btn-default button button-medium']/span")
    submit.click()
    text = browser.find_element_by_class_name("alert.alert-success").text
    return text


def contact_us():
    '''


    '''
    submit = browser.find_element_by_link_text("Contact us")
    submit.click()
    browser.find_element_by_xpath("//select[@id='id_contact']/option[text()='Webmaster']").click()
    textarea = browser.find_element_by_xpath("//input[@id='email']")
    textarea.send_keys(config.email)
    textarea = browser.find_element_by_xpath("//input[@id='id_order']")
    textarea.send_keys(config.order)
    textarea = browser.find_element_by_xpath("//textarea[@id='message']")
    textarea.send_keys(config.message)
    submit = browser.find_element_by_xpath("//button[@id='submitMessage']/span")
    submit.click()
    text = browser.find_element_by_xpath("//p[@class='alert alert-success']").text
    return(text)













