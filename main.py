import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv

options = webdriver.ChromeOptions()

# Отключает режим вебдрайвера
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path="/Users/Govard/Desktop/Jobs/EvoSoft/chromedriver.exe",
    options=options
)


def go_to_site():
    """1. Зайти на https://www.nseindia.com"""
    driver.get('https://www.nseindia.com')
    driver.delete_all_cookies()


def hover_tip():
    """2. Навестись (hover) на MARKET DATA"""
    element = driver.find_element_by_link_text("MARKET DATA")
    action = ActionChains(driver)
    action.move_to_element(element).perform()


def click_link_market():
    """3. Кликнуть на Pre-Open Market"""
    driver.find_element_by_link_text("Pre-Open Market").click()


def pars_data_final_price():
    """4. Спарсить данные Final Price по всем позициям на странице и вывести их в csv файл. Имя;цена"""
    title = []
    price = []
    symbols = driver.find_elements_by_xpath('//*[@id="livePreTable"]/tbody/tr')

    for symbol in symbols:
        title_text = symbol.find_element_by_tag_name('a').text
        price_text = symbol.find_element_by_class_name('bold.text-right').text

        title.append(title_text)
        price.append(price_text)

    with open('complete.csv', 'w', encoding='cp1251', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['Имя', 'Цена'])
        writer.writerow([", ".join(title), ", ".join(price)])


def click_home():
    """5.1 Зайти на главную страницу"""
    driver.find_element_by_link_text("HOME").click()


def scroll_down_graph():
    """5.2 Пролистать вниз до графика"""
    driver.execute_script('window.scrollTo(0, 350)')


def schedule_selection_nifty_bank():
    """5.3 Выбрать график "NIFTY BANK"""
    # Сократил селектор
    driver.find_element_by_partial_link_text('NIFTY BANK').click()


def click_view_all():
    """5.4 Нажать “View all” под "TOP 5 STOCKS - NIFTY BANK"""
    driver.execute_script('window.scrollTo(0, 900)')
    driver.find_element_by_link_text('View All').click()


def choice_selector_nifty_alpha_50():
    """5.5 Выбрать в селекторе “NIFTY ALPHA 50”"""
    driver.find_element_by_class_name('custom_select').click()
    # сократил xpath путь
    driver.find_element_by_xpath('//optgroup[4]/option[7]').click()
    driver.find_element_by_class_name('custom_select').click()
    time.sleep(5)

    # с 1 раза таблица не загружается, по этому приходится обновлять страницу и открывать заново. Тогда работает.
    if driver.find_element_by_class_name('spin-loader'):
        driver.refresh()
        time.sleep(10)
        driver.find_element_by_class_name('custom_select').click()
        # сократил xpath путь
        driver.find_element_by_xpath('//optgroup[4]/option[7]').click()
        driver.find_element_by_class_name('custom_select').click()


def flip_the_table():
    """5.6 Пролистать таблицу до конца"""
    time.sleep(3)
    # сократил xpath путь
    element = driver.find_element_by_xpath('//tbody/tr[51]')
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    driver.execute_script('window.scrollTo(0, 400)')


def main():
    go_to_site()
    time.sleep(3)
    hover_tip()
    time.sleep(3)
    click_link_market()
    time.sleep(3)
    pars_data_final_price()
    driver.delete_all_cookies()
    click_home()
    time.sleep(3)
    scroll_down_graph()
    time.sleep(3)
    schedule_selection_nifty_bank()
    time.sleep(3)
    driver.delete_all_cookies()
    click_view_all()
    time.sleep(3)
    driver.delete_all_cookies()
    choice_selector_nifty_alpha_50()
    driver.delete_all_cookies()
    time.sleep(5)
    flip_the_table()
    time.sleep(5)
    # добавил закрытие сессии(всех окон)
    driver.quit()


if __name__ == '__main__':
    main()