from behave import *
from selenium import webdriver


@given(u'I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Edge(executable_path = "C:\Drivers\edgedriver_win64\msedgedriver.exe")


@when(u'I open orange hrm homepage')
def launchBrowser(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{pwd}"')
def enterCredentials(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when(u'Click on login button')
def clickLogin(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'User must successfully login to the Dashboard page')
def displayDashboard(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Test Failed"

    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"

