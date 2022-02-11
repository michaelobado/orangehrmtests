from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path = "C:\Drivers\chromedriver.exe")
    #context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()