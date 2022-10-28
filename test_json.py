import keyword
import json


class Convertor:


    def __init__(self, dictionary):
        self.dictionary = {}
        for key, value in dictionary.items():
            if keyword.iskeyword(key):
                self.dictionary[key + '_'] = value
            else:
                self.dictionary[key] = value


    def __getattr__(self, key):
        value = self.dictionary.get(key)
        if isinstance(value, dict):
            return Convertor(value)
        return value

class ColorizeMixin:
    def __repr__(self):
        return f'\033[{self.repr_color_code}m{self.title} | {self.price} ₽\033[0m'


class Advert(ColorizeMixin):
    repr_color_code = 33


    def __init__(self, dictionary):
        dictionary = json.loads(dictionary)
        if not 'price' in dictionary:
            dictionary['price'] = 0
        elif dictionary['price'] < 0:
            raise ValueError("price must be >= 0")
        self.conv = Convertor(dictionary)


    def __getattr__(self, key):
        return  self.conv.__getattr__(key)

if __name__ == '__main__':
    lesson_str = """{
                    "title": "python",
                    "price": 0,
                    "location": {
                    "address": "город Москва, Лесная, 7",
                    "metro_stations": ["Белорусская"]
                    }
                    }"""
    advert = Advert(lesson_str)
    print(advert)
    print("title: {}".format(advert.title))
    print("price: {}".format(advert.price))
    print("address: {}".format(advert.location.address))
    print("metro_stations: {}".format(advert.location.metro_stations))

    lesson_str = """{
                    "title": "Вельш-корги",
                    "price": 1000,
                    "class": "dogs",
                    "location": {
                    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
                                }
                    }"""
    advert = Advert(lesson_str)
    print(advert)
    print("title: {}".format(advert.title))
    print("price: {}".format(advert.price))
    print("class: {}".format(advert.class_))
    print("address: {}".format(advert.location.address))

    lesson_str = """{
                    "title": "iPhone X",
                    "price": 100,
                    "location": {
                    "address": "город Самара, улица Мориса Тореза, 50",
                    "metro_stations": ["Спортивная", "Гагаринская"]
                    }
                    }"""
    advert = Advert(lesson_str)
    print(advert)
    print("title: {}".format(advert.title))
    print("price: {}".format(advert.price))
    print("address: {}".format(advert.location.address))
    print("metro_stations: {}".format(advert.location.metro_stations))

    lesson_str = '{"title": "python"}'
    advert = Advert(lesson_str)
    print(advert)
    print("title: {}".format(advert.title))
    print("price: {}".format(advert.price))

    lesson_str = '{"title": "python", "price": -1}'
    lesson_ad = Advert(lesson_str)
