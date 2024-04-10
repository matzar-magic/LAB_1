# Лабораторная работа 1 - Назаров
from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests
import xlsxwriter


def parse():

    url = 'https://www.chitai-gorod.ru/'  # передаем необходимый URL адрес
    page = requests.get(url)  # получаем страницу
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4
    block = soup.find_all('div', class_='slider__item')  # находим контейнер с нужным классом

    workbook = xlsxwriter.Workbook('books.xlsx')  # создаем файл для записи
    worksheet = workbook.add_worksheet()  # добавляем лист

    price1 = 1
    title1 = 1
    author1 = 1
    worksheet.write(0, 0, 'price')
    worksheet.write(0, 1, 'title')
    worksheet.write(0, 2, 'author')

    for data in block:  # проходим циклом по содержимому контейнера
        title = data.find('div', class_='product-title__head').text
        author = data.find('div', class_='product-title__author').text
        price = data.find('div', class_='product-price__value').text

        worksheet.write(price1, 0, price)
        worksheet.write(title1, 1, title)
        worksheet.write(author1, 2, author)
        price1 += 1
        title1 += 1
        author1 += 1

    workbook.close()  # закрываем файл


parse()
