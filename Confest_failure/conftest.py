import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item , call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup" , None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name= "Failure Screenshot",
                attachment_type= allure.attachment_type.PNG
            )
