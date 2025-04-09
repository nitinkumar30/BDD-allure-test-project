import allure


def addScreenshot(context, filename):
    screenshot_path = 'screenshots/' + filename + '.png'
    # Capture the screenshot
    context.driver.save_screenshot(screenshot_path)

    # Attach the screenshot to the Allure report
    with open(screenshot_path, 'rb') as file:
        allure.attach(file.read(), filename, attachment_type=allure.attachment_type.PNG)

