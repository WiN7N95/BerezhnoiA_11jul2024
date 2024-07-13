import requests
import pytest

BASE_URL = 'https://altaivita.ru/engine/cart/add_products_to_cart_from_preview.php'
HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'PHPSESSID=8ae5krtut12cfb1s97jank0p43; CID=578eafd694ead5ef15c6c93d01c262cb; _ga=GA1.1.2111352024.1720715187; _ym_uid=1720715187619026024; _ym_d=1720715187; site_countryID=395; site_country_name=%D0%9D%D0%B8%D0%B4%D0%B5%D1%80%D0%BB%D0%B0%D0%BD%D0%B4%D1%8B; _ym_visorc=w; _ym_isad=2; _ga_2JB65Y3D22=GS1.1.1720890102.4.1.1720893011.48.0.0',
    'Origin': 'https://altaivita.ru',
    'Referer': 'https://altaivita.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0 (Edition Yx GX 03)',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Opera GX";v="111", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

@pytest.fixture
def session():
    return requests.Session()

def test_add_product_to_cart(session):
    data = {
        'product_id': '675',
        'this_listId': 'popular_products',
        'LANG_key': 'ru',
        'S_wh': '1',
        'S_CID': '578eafd694ead5ef15c6c93d01c262cb',
        'S_cur_code': 'usd',
        'S_koef': '0.01407',
        'quantity': '1',
        'S_hint_code': 'eur',
        'S_customerID': ''
    }

    response = session.post(BASE_URL, headers=HEADERS, data=data)
    assert response.status_code == 200
    assert '"status":"ok"' in response.text

def test_increase_product_quantity_in_cart(session):
    data = {
        'product_id': '675',
        'this_listId': 'popular_products',
        'LANG_key': 'ru',
        'S_wh': '1',
        'S_CID': '578eafd694ead5ef15c6c93d01c262cb',
        'S_cur_code': 'usd',
        'S_koef': '0.01407',
        'quantity': '1',
        'S_hint_code': 'eur',
        'S_customerID': ''
    }

    response = session.post(BASE_URL, headers=HEADERS, data=data)
    assert response.status_code == 200
    assert '"status":"ok"' in response.text

    # Increase the quantity
    response = session.post(BASE_URL, headers=HEADERS, data=data)
    assert response.status_code == 200
    assert '"status":"ok"' in response.text
