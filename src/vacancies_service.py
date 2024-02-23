import json
from abc import ABC, abstractmethod

import requests


class VacanciesService(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self):
        """
        Получает данные о вакансиях с сайта
        """
        pass


class HHVacanciesService(VacanciesService):
    """
    Класс для работы с вакансиями платформы hh.ru
    """
    def __init__(self):
        """
        Создает экземпляр класса HHVacanciesService
        """
        self._url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, text=''):
        """
        Получает данные о вакансиях с сайта
        """
        response = requests.get(self._url, params={'per_page': 100, 'text': text})
        if response.status_code == 200:
            return response.json()['items']
        else:
            print('Возникла ошибка при обращении к сайту hh.ru')


# hhv = HHVacanciesService()
# v = hhv.get_vacancies()
# print(json.dumps(v, indent=2, ensure_ascii=False))
