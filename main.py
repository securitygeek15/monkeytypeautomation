"""
Automates typing on Monkeytype using Selenium.
Author: Amaan (Security__geek)
Description: Opens Monkeytype, accepts cookies, retrieves words, 
and simulates human-like typing with random delays.
"""

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def open_monkeytype(url="https://monkeytype.com/"):
    """Initialize WebDriver and open Monkeytype."""
    driver = webdriver.Edge()
    driver.get(url)
    return driver


def accept_cookies(driver):
    """Accept cookies if the popup appears."""
    try:
        accept_button = driver.find_element(By.CLASS_NAME, "acceptAll")
        accept_button.click()
        print("[INFO] Cookies accepted.")
    except NoSuchElementException:
        print("[INFO] No cookies popup found.")


def get_words(driver):
    """Retrieve all words displayed on the Monkeytype test."""
    words_container = driver.find_element(By.CLASS_NAME, "full-width")
    words_container.click()

    word_elements = words_container.find_elements(By.CLASS_NAME, "word")
    words = [
        "".join([letter.text for letter in word_el.find_elements(By.TAG_NAME, "letter")])
        for word_el in word_elements
    ]
    return words, driver.find_element(By.TAG_NAME, "input")


def type_words(input_field, words):
    """Simulate typing each word with random human-like delays."""
    for word in words:
        for char in word:
            input_field.send_keys(char)
            time.sleep(random.uniform(0.05, 0.09))  # Random delay between keystrokes
        input_field.send_keys(" ")  # Space after each word


def main():
    """Main automation flow."""
    driver = open_monkeytype()
    time.sleep(2)

    accept_cookies(driver)
    time.sleep(2)

    words, input_field = get_words(driver)
    type_words(input_field, words)

    time.sleep(3)  # Wait before closing
    driver.close()
    print("[INFO] Automation complete.")


if __name__ == "__main__":
    main()
