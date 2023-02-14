import requests
import json

class ConvertionException(Exception):
    pass

class Convertor:
    @staticmethod
    def prices(base, quote, amount):
        fin = base + quote
        r = requests.get(f"https://currate.ru/api/?get=rates&pairs={fin}&key=fa74942e04bada738f8ca5a6f7f56e40")
        resp = json.loads(r.content)
        try:
            sum_price = float(resp["data"][fin]) * float(amount)
        except ValueError:
            raise ConvertionException('Введены некорректные данные!')
        except TypeError:
            raise ConvertionException('Введены некорректные данные!')
        return sum_price
