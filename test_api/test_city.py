from random import random

import requests
from unittest import TestCase, TestSuite, TextTestRunner


test_data = {}


class City01TestCase(TestCase):
    def test_all_city(self):
        url = 'http:localhost:8000/city/all'
        resp = requests.get(url)
        city_list = resp.json().get('data')

        city = random.choice(city_list)

        test_data['city_id'] = city['id']

        print('---定位当前的城市---', city['city_name'])


class City02TestCase(TestCase):
    def test_city_area(self):
        url = 'http://localhost:8000/city/area/?one_id=%s'
        resp = requests.get(url, {
            'one_id': test_data['city_id']
        })

        area_list = resp.json().get('data')

        area = random.choice(area_list)

        print('---定位的区县--', area['id'])
        test_data['area_id'] = area['id']


def suite1():
    suite1 = TestSuite()
    suite1.addTest(City01TestCase.test_all_city)


def suite2():
    suite2 = TestSuite
    suite2.addTest(City02TestCase.test_city_area)


def suite_all():
    return TestSuite((suite1, suite2))


if __name__ == '__main__':
    TextTestRunner().run(suite_all())
