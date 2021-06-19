<center>

# Скрипт создан специально для компании "EvoSoft". 
____
## Описание скрита

Данный "скрипт-парсер" написан на языке Python с помощью инструмента Selenium WebDriver.
Данный скрипт создан для сбора данных c рынка акций на сайте [nseindia.com](https://www.nseindia.com)

###Применение:
С помощью Selenium скрипт заходит на сайт [nseindia.com](https://www.nseindia.com). Наводится на hover меню раздела 
"MARKET DATA". Нажимает на ссылку [Pre-Open Market](https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market).
После чего парсит автоматически данные с таблицы, а именно колонку "Symbol" и "Final Price" и всё это сохраняет в 
файл с расширением CSV.

Далее имитирует небольшой пользовательский сценарий, а именно:
Заходит на главную страницу сайта [nseindia.com](https://www.nseindia.com), пролистывает вниз до графика, выбирает 
график "NIFTY BANK", нажимает на [View all](https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20BANK)
под "TOP 5 STOCKS - NIFTY BANK", далее выбирает в селекторе “NIFTY ALPHA 50” и пролистывает таблицу до конца.

###Что нужно для установки скрипта:
IDE, к примеру [Pycharm](https://www.jetbrains.com/pycharm/) <br>
[Python](https://www.python.org/) (на данный момент актуальная версия 3.9.5)<br>
[Веб-драйвер Selenium](https://pypi.org/project/selenium/) <br>
[Pandas](https://pypi.org/project/pandas/) <br>

</center>