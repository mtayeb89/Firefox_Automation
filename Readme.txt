Recommendations for Libraries:

    Selenium: It's a powerful tool for browser automation but can be complex. It's great for web scraping and automating web tasks. Consider using WebDriverWait for more control over element loading.

    PyAutoGUI: Useful for controlling the mouse and keyboard, but can be a bit tricky for web automation. Often, native Selenium commands are preferable as they are more reliable.

    webdriver_manager: This library helps manage the web drivers automatically, reducing manual setup. It's very convenient and highly recommended.

    Service Class: We use the Service class from selenium.webdriver.firefox.service to correctly pass the path of the GeckoDriver to the Firefox WebDriver.
    GeckoDriverManager().install(): This still installs the correct version of the GeckoDriver, but now it's correctly wrapped in the Service class.