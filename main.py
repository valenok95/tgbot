import datetime
import json

import requests
from bs4 import BeautifulSoup


def get_first_price():
    aks = {'SU': 'Аэрофлот', 'U6': 'Уральские авиалинии', 'N4': 'Nordwind Airlines', 'S7': 'S7', 'DP': 'Победа'}
    start_city = "MOW"
    finish_city = "LED"
    start_headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
                     'X-Origin-Cookie': 'language=ru; auid=rBMumGM9QnuQ+gAhFViiAg==; nuid=5e925d7c-da3c-482d-950a-893fd9cbe20e; _awt=3812526963e93d0795ee63423c36363320f3256393c0333-41116235366f132f6463363461e1960bf; currency=RUB; _gcl_au=1.1.646717896.1664959105; uxs_uid=13fdc580-4489-11ed-9190-4353b23c415b; uncheck_hotel_cookie=true; last_search=MOW0710LED1; currency=rub; marker=google; cto_bundle=IilWEF9JeXJhWVJlMHNVOHNpdFA5WWVGTVY4MCUyRmslMkJjWFZEOCUyRllmaEk3RUN2eUpOTDRKJTJCbTA3S3ZSc2o4dFpWVkM4aXZrU1YwczZsbXRWZDglMkYlMkJoNmNyZnVwWFpKTThqSThCMjBLeXA4TVJyeXl6MklZc1hJekZkVGpVdjFWWHBWQ0FERzEzeEFpeFZwUjhtdzEyJTJGTVA2ZDEyZyUzRCUzRA; tmr_lvid=0bb17e6bf15fc88534cc34a06a0adfe6; tmr_lvidTS=1664959105681; _ym_uid=1664959106127351759; _ym_d=1664959126; _ym_isad=2; tmr_detect=0%7C1664959129466; google_recaptcha_token=2bb097db29198d8b841936f092c0c25f%3A3033414949756b7a68384e6e535653497677446b38527a6843466b364d5f2d3239545f496b59556d367134496935587843524c725049346d69536b4b5f61476735674f4c52615933566c44356c6161326f675468366c336e7049385870642d5257575056332d4341303479394152726c38714a485777726949424e734a727131744f76384e5f495878734b537837742d5670734f71316c416a38426a695a774a32447569795471703070774854764343636f354a795f74755f414a4d4775514859546a74626c335443744e41655633724e7657764b57794944794c65756a4c4f697839736a754958494136566638504f6c6f696176544733626e6c4a76724277303658705450616a56787973494d414c4838736a462d43795755585670394e6242346d6450445044744a316d753477614858327a674975564c4b77736b4954553075456f7a724e694834306a717849356174324e484269674c6c77625443687a433754335a685242675a6f596a7a4d686b65714f35594650424f425862355a755043664f5666397632315a786e784b4c364762354d343047303246672d426b574343496b4176364a6d4d4e68634f66736e4d6e51736579514853506e51434e69315638577677676a644f7874425a6839304e5f4d3541376d683650354f70695378567a386c4a736866616c4f635a504b4465436b70456d762d3650472d5f7550444d3450374552532d4566714846377851374c7472565961364d524c7377355336713751%3A1667561837; _ym_visorc=b; auid=fwAAAWM9bnIfEi3wAwypAg==; _ga=GA1.2.968792858.1664959126; _gid=GA1.2.912888511.1664959126; _dc_gtm_UA-1481416-4=1; _ga_EVCZWTNN22=GS1.1.1664969799.2.1.1664970679.0.0.0; _fbp=fb.1.1664959126450.949577949; search_init_stamp=1664970679647; tmr_reqNum=57; _gat_unoTracker=1; _gat_gtag_UA_51187097_10=1; _sp_id.dc27=12580f8e-6ae0-4681-9ec0-d0dd566e4588.1664959103.2.1664970680.1664959698.285a480c-665e-474f-bb76-8fc257aed3c0; _sp_ses.dc27=*',
                     'Content-type': 'application/json',
                     'Accept': 'application/json'}

    url_start = "https://tickets-api.aviasales.ru/search/v2/start"
    request_start_json = json.load(open('startRequest.json'))
    # устанавливаем параметры для запроса

    for item in request_start_json['search_params']['directions']:
        item['date'] = "2022-10-07"
        item['origin'] = start_city
        item['destination'] = finish_city

    start_response = requests.post(url=url_start, headers=start_headers, json=request_start_json)
    response_start_json = start_response.json()

    search_id = response_start_json["search_id"]

    next_host = start_response.headers.get('X-Delta-DC')

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0',
               'Content-type': 'application/json',
               'X-Origin-Cookie': 'language=ru; auid=rBMumGM9QnuQ+gAhFViiAg==; nuid=5e925d7c-da3c-482d-950a-893fd9cbe20e; _awt=3812526963e93d0795ee63423c36363320f3256393c0333-41116235366f132f6463363461e1960bf; currency=RUB; _gcl_au=1.1.646717896.1664959105; uxs_uid=13fdc580-4489-11ed-9190-4353b23c415b; uncheck_hotel_cookie=true; currency=rub; marker=google; cto_bundle=IilWEF9JeXJhWVJlMHNVOHNpdFA5WWVGTVY4MCUyRmslMkJjWFZEOCUyRllmaEk3RUN2eUpOTDRKJTJCbTA3S3ZSc2o4dFpWVkM4aXZrU1YwczZsbXRWZDglMkYlMkJoNmNyZnVwWFpKTThqSThCMjBLeXA4TVJyeXl6MklZc1hJekZkVGpVdjFWWHBWQ0FERzEzeEFpeFZwUjhtdzEyJTJGTVA2ZDEyZyUzRCUzRA; tmr_lvid=0bb17e6bf15fc88534cc34a06a0adfe6; tmr_lvidTS=1664959105681; _ym_uid=1664959106127351759; _ym_d=1664959126; _ym_isad=2; tmr_detect=0%7C1664959129466; google_recaptcha_token=2bb097db29198d8b841936f092c0c25f%3A3033414949756b7a68384e6e535653497677446b38527a6843466b364d5f2d3239545f496b59556d367134496935587843524c725049346d69536b4b5f61476735674f4c52615933566c44356c6161326f675468366c336e7049385870642d5257575056332d4341303479394152726c38714a485777726949424e734a727131744f76384e5f495878734b537837742d5670734f71316c416a38426a695a774a32447569795471703070774854764343636f354a795f74755f414a4d4775514859546a74626c335443744e41655633724e7657764b57794944794c65756a4c4f697839736a754958494136566638504f6c6f696176544733626e6c4a76724277303658705450616a56787973494d414c4838736a462d43795755585670394e6242346d6450445044744a316d753477614858327a674975564c4b77736b4954553075456f7a724e694834306a717849356174324e484269674c6c77625443687a433754335a685242675a6f596a7a4d686b65714f35594650424f425862355a755043664f5666397632315a786e784b4c364762354d343047303246672d426b574343496b4176364a6d4d4e68634f66736e4d6e51736579514853506e51434e69315638577677676a644f7874425a6839304e5f4d3541376d683650354f70695378567a386c4a736866616c4f635a504b4465436b70456d762d3650472d5f7550444d3450374552532d4566714846377851374c7472565961364d524c7377355336713751%3A1667561837; _ym_visorc=b; auid=fwAAAWM9bnIfEi3wAwypAg==; _ga=GA1.2.968792858.1664959126; _gid=GA1.2.912888511.1664959126; _dc_gtm_UA-1481416-4=1; _ga_EVCZWTNN22=GS1.1.1664969799.2.1.1664970679.0.0.0; _fbp=fb.1.1664959126450.949577949; search_init_stamp=1664970679647; tmr_reqNum=57; _gat_unoTracker=1; _gat_gtag_UA_51187097_10=1; _sp_id.dc27=12580f8e-6ae0-4681-9ec0-d0dd566e4588.1664959103.2.1664970680.1664959698.285a480c-665e-474f-bb76-8fc257aed3c0; _sp_ses.dc27=*',
               'Accept': 'application/json'}

    url = "https://tickets-api.{}.aviasales.ru/search/v3/results".format(next_host)
    # request_json = json.dumps({"search_id": search_id})
    response = requests.post(url=url, headers=headers, json={
        "search_id": search_id
    })

    cheapest_ticker_info = response.json()[0]['filtered_cheapest_ticket']['proposals'][0]
    a_to = response.json()[0]['filtered_cheapest_ticket']['proposals'][0]
    price = cheapest_ticker_info['price_per_person']['value']
    for key in cheapest_ticker_info['flight_terms']:
        term_number = key

    airline_id = cheapest_ticker_info['flight_terms'][term_number]['marketing_carrier_designator']['airline_id']
    race_number = cheapest_ticker_info['flight_terms'][term_number]['marketing_carrier_designator']['number']
    price = cheapest_ticker_info['price_per_person']['value']
    airlineName = aks[airline_id]
    result_message = "Самый дешевый авиабилет {} - {} : {} рублей. Авиакомпания: {} . Номер рейса {}-{}".format(
        start_city, finish_city,
        price, airlineName, airline_id, race_number)
    #print(result_message)

    return result_message

#get_first_price()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# print("Hello, World!")
