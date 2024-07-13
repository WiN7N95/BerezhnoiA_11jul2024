import requests
import pytest
import allure
import json

BASE_URL = 'https://altaivita.ru/engine/cart'

HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PHPSESSID=8ae5krtut12cfb1s97jank0p43; CID=578eafd694ead5ef15c6c93d01c262cb',
    'Origin': 'https://altaivita.ru',
    'Referer': 'https://altaivita.ru/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0 (Edition Yx GX 03)',
    'X-Requested-With': 'XMLHttpRequest',
}

ADD_PRODUCT_DATA = {
    'product_id': '676',
    'this_listId': 'novinki',
    'LANG_key': 'ru',
    'S_wh': '1',
    'S_CID': '578eafd694ead5ef15c6c93d01c262cb',
    'S_cur_code': 'usd',
    'S_koef': '0.01407',
    'quantity': '1',
    'S_hint_code': 'eur',
    'S_customerID': ''
}

DELETE_PRODUCT_DATA = {
    'product_id': '676',
    'LANG_key': 'ru',
    'S_wh': '1',
    'S_CID': '578eafd694ead5ef15c6c93d01c262cb',
    'S_cur_code': 'usd',
    'S_koef': '0.01407',
    'S_hint_code': 'eur',
    'S_customerID': ''
}

@allure.feature('Cart API')
@allure.story('Add product to cart')
def test_add_product_to_cart():
    response = requests.post(f'{BASE_URL}/add_products_to_cart_from_preview.php', headers=HEADERS, data=ADD_PRODUCT_DATA)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['status'] == 'ok'

@allure.feature('Cart API')
@allure.story('Delete product from cart')
def test_delete_product_from_cart():
    response = requests.post(f'{BASE_URL}/delete_products_from_cart_preview.php', headers=HEADERS, data=DELETE_PRODUCT_DATA)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['status'] == 'ok'
