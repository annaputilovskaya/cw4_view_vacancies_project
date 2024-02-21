from abc import ABC, abstractmethod


class VacanciesService(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """
    @abstractmethod
    def get_vacancies(self):
        """
        Получает данные о вакансиях с сайта
        :return: json-файл
        """
        pass


class HHVacanciesService(VacanciesService):
    """
    Класс для работы с вакансиями платформы hh.ru
    """
    def get_vacancies(self):
        """
        Получает данные о вакансиях с сайта
        :return: json-файл
        """
        pass



