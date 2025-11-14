from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@given('I open Google')
def step_open_google(context):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.google.com")

@when('I search for "{query}"')
def step_search(context, query):
    search_box = context.driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.submit()

@then('the results should contain "{text}"')
def step_verify_results(context, text):
    assert text.lower() in context.driver.page_source.lower()
    context.driver.quit()