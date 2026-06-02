"""Automate Cookie Clicker with Selenium.

Clicks the big cookie continuously and buys the cheapest affordable product.
Press 'p' to pause and 'r' to resume.

Configuration is read from environment variables so no machine-specific path
is hardcoded:

- CHROME_BINARY    Optional path to the Chrome/Chromium binary. If unset,
                   Selenium uses the system default.
- CHROMEDRIVER     Optional path to chromedriver. If unset, Selenium Manager
                   (Selenium >= 4.6) downloads/locates a matching driver.

Run:
    python cookie_clicker.py
"""

import os
import pickle
import time

import keyboard
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

GAME_URL = "https://orteil.dashnet.org/cookieclicker/"
COOKIES_FILE = "cookies.pkl"

COOKIE_ID = "bigCookie"
COOKIES_COUNT_ID = "cookies"
PRODUCT_PRICE_PREFIX = "productPrice"
PRODUCT_PREFIX = "product"
PRODUCT_SLOTS = 4

# Delay between loop iterations, in seconds. Keeps the script from hammering
# the browser as fast as the CPU allows.
LOOP_DELAY = 0.05


def build_driver():
    """Create a Chrome WebDriver, honoring optional env-var overrides."""
    options = webdriver.ChromeOptions()

    chrome_binary = os.environ.get("CHROME_BINARY")
    if chrome_binary:
        options.binary_location = chrome_binary

    chromedriver = os.environ.get("CHROMEDRIVER")
    if chromedriver:
        # Explicit driver path provided by the user.
        return webdriver.Chrome(service=Service(chromedriver), options=options)

    # No path given: Selenium Manager resolves a matching driver automatically.
    return webdriver.Chrome(options=options)


def load_saved_cookies(driver):
    """Restore browser cookies from a previous session, if available."""
    try:
        with open(COOKIES_FILE, "rb") as file:
            for cookie in pickle.load(file):
                driver.add_cookie(cookie)
    except FileNotFoundError:
        print(f"'{COOKIES_FILE}' not found. Continuing without loading cookies.")
    except pickle.UnpicklingError:
        print("Error deserializing cookies. Continuing without loading cookies.")


def get_cookie_count(driver):
    """Return the current cookie count, or None if it cannot be read."""
    try:
        raw = driver.find_element(By.ID, COOKIES_COUNT_ID).text.split(" ")[0]
        return int(raw.replace(",", ""))
    except (NoSuchElementException, StaleElementReferenceException, ValueError):
        return None


def buy_cheapest_affordable_product(driver, cookies_count):
    """Buy the first affordable product among the visible slots."""
    for i in range(PRODUCT_SLOTS):
        try:
            price_text = driver.find_element(
                By.ID, PRODUCT_PRICE_PREFIX + str(i)
            ).text.replace(",", "")
        except (NoSuchElementException, StaleElementReferenceException):
            continue

        if not price_text.isdigit():
            continue

        if cookies_count >= int(price_text):
            try:
                driver.find_element(By.ID, PRODUCT_PREFIX + str(i)).click()
            except (NoSuchElementException, StaleElementReferenceException):
                continue
            break


def select_english(driver):
    """Click the English language button if the language prompt appears."""
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(text(), 'English')]")
            )
        )
        driver.find_element(By.XPATH, "//*[contains(text(), 'English')]").click()
    except TimeoutException:
        # Language prompt did not appear (e.g. already set); nothing to do.
        pass


def main():
    driver = build_driver()
    try:
        driver.get(GAME_URL)
        load_saved_cookies(driver)
        select_english(driver)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, COOKIE_ID))
        )

        paused = False
        print("Running. Press 'p' to pause, 'r' to resume, Ctrl+C to quit.")
        while True:
            if keyboard.is_pressed("p"):
                paused = True
            if keyboard.is_pressed("r"):
                paused = False

            if not paused:
                try:
                    driver.find_element(By.ID, COOKIE_ID).click()
                except (NoSuchElementException, StaleElementReferenceException):
                    pass

                cookies_count = get_cookie_count(driver)
                if cookies_count is not None:
                    buy_cheapest_affordable_product(driver, cookies_count)

            time.sleep(LOOP_DELAY)
    except KeyboardInterrupt:
        print("\nStopping.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
