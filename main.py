import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

# Отключает режим вебдрайвера
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/Users/Govard/Desktop/Jobs/Evotools/chromedriver.exe",
    options=options
)


def go_to_site():
    """1. Зайти на https://www.nseindia.com"""
    driver.get('https://www.nseindia.com')
    driver.delete_all_cookies()


def hover():
    """2. Навестись (hover) на MARKET DATA"""
    element = driver.find_element_by_link_text("MARKET DATA")
    action = ActionChains(driver)
    action.move_to_element(element).perform()


def click_link():
    """3. Кликнуть на Pre-Open Market"""
    driver.find_element_by_link_text("Pre-Open Market").click()


def pars_data():
    """4. Спарсить данные Final Price по всем позициям на странице и вывести их в csv файл. Имя;цена"""
    title = []
    price = []

    symbols = driver.find_elements_by_xpath('//*[@id="livePreTable"]/tbody/tr')

    for symbol in symbols:
        title_text = symbol.find_element_by_tag_name('a').text
        price_text = symbol.find_element_by_class_name('bold.text-right').text

        title.append(title_text)
        price.append(price_text)

    df = pd.DataFrame({
            'Имя': title,
            'Цена': price,
        })
    df.to_excel('./complete.xlsx', sheet_name='www.nseindia.com', index=False)


def click_home():
    """5.1 Зайти на главную страницу"""
    driver.find_element_by_link_text("HOME").click()


def scroll_down():
    """5.2 Пролистать вниз до графика"""
    driver.execute_script('window.scrollTo(0, 350)')


def schedule_selection():
    """5.3 Выбрать график "NIFTY BANK"""
    driver.find_element_by_xpath('//*[@id="nse-indices"]/div[2]/div/div/nav/div/div/a[4]/div').click()


def view_all():
    """5.4 Нажать “View all” под "TOP 5 STOCKS - NIFTY BANK"""
    driver.execute_script('window.scrollTo(0, 900)')
    driver.find_element_by_link_text('View All').click()


def selector_selection():
    """5.5 Выбрать в селекторе “NIFTY ALPHA 50”"""
    driver.find_element_by_class_name('custom_select').click()
    driver.find_element_by_xpath('//*[@id="equitieStockSelect"]/optgroup[4]/option[7]').click()
    driver.find_element_by_class_name('custom_select').click()

    # с 1 раза таблица не загружается, по этому приходится обновлять страницу и открывать заново. Тогда работает.
    if driver.find_element_by_class_name('spin-loader'):
        driver.refresh()
        time.sleep(10)
        driver.find_element_by_class_name('custom_select').click()
        driver.find_element_by_xpath('//*[@id="equitieStockSelect"]/optgroup[4]/option[7]').click()
        driver.find_element_by_class_name('custom_select').click()


def flip_the_table():
    """5.6 Пролистать таблицу до конца"""
    time.sleep(3)
    element = driver.find_element_by_xpath('//*[@id="equityStockTable"]/tbody/tr[51]')
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    driver.execute_script('window.scrollTo(0, 400)')


def main():
    go_to_site()
    time.sleep(3)
    hover()
    time.sleep(3)
    click_link()
    time.sleep(3)
    pars_data()
    driver.delete_all_cookies()
    click_home()
    time.sleep(3)
    scroll_down()
    time.sleep(3)
    schedule_selection()
    time.sleep(3)
    driver.delete_all_cookies()
    view_all()
    time.sleep(3)
    driver.delete_all_cookies()
    selector_selection()
    driver.delete_all_cookies()
    time.sleep(5)
    flip_the_table()
    time.sleep(5)
    driver.close()


if __name__ == '__main__':
    main()