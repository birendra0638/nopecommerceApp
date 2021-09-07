from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        # path set in c drive bin folder and folder added in environment variable
        driver = webdriver.Firefox()
        print("launching firefox browser")
    else:
        driver = webdriver.Ie()
        print("launching ie  browser")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will return the browser value to setup method
    return request.config.getoption("--browser")


##############Pytest HTMl Report##################
# It is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'User1'


# It is hook for delete/modify Environment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

