import json
import os
from abc import ABC, abstractmethod


class VacanciesFile(ABC):
    """
    Абстрактный класс для работы с файлом вакансий
    """
    @ abstractmethod
    def add_vacancy(self, vacancy) -> None:
        """
        Добавляет вакансии в файл
        """

    @abstractmethod
    def filter_vacancies(self, filter_words):
        """
        Получает данные из файла с вакансиями по указанным критериям
        """

    @abstractmethod
    def delete_vacancy(self, vacancy) -> None:
        """
        Удаляет информацию о вакансиях из файла
        """


class VacanciesJSON(VacanciesFile):
    """
    Класс для сохранения информации о вакансиях в JSON-файле
    """
    PATH = os.path.join('data', 'vacancies.json')

    def __init__(self, vacancies_list):
        """
        Создает объект класса VacanciesJSON
        """
        self.vacancies_list = vacancies_list
        try:
            self.write_json(self.vacancies_params_list, VacanciesJSON.PATH)
        except TypeError:
            print('Отсутсвуеют вакансии для записи в файл')

    @property
    def vacancies_params_list(self):
        """
        Возвращает параметры вакансий из списка в виде списка словарей
        :return:
        """
        vacancies_params_list = []
        for vacancy in self.vacancies_list:
            vacancies_params_list.append({
                'title': vacancy.title,
                'url': vacancy.url,
                'salary': vacancy.salary,
                'requirements': vacancy.requirements,
                'area': vacancy.area,
                'employer': vacancy.employer
            })
        return vacancies_params_list

    def add_vacancy(self, vacancy) -> None:
        """
        Добавляет вакансии в JSON-файл
        """
        self.vacancies_list.append(vacancy)
        self.write_json(self.vacancies_params_list, VacanciesJSON.PATH)

    def delete_vacancy(self, vacancy) -> None:
        """
        Удаляет информацию о вакансиях из JSON-файла
        """
        if vacancy in self.vacancies_list:
            self.vacancies_list.remove(vacancy)
            self.write_json(self.vacancies_params_list, VacanciesJSON.PATH)

    def filter_vacancies(self, filter_words) -> list:
        """
        Отбирает вакансии из списка по ключевым словам
        """
        if not filter_words:
            return self.vacancies_list

        new_list = []
        for vacancy in self.vacancies_list:
            if filter_words in vacancy:
                new_list.append(vacancy)
        return new_list

    @staticmethod
    def write_json(data, filename) -> None:
        """
        Запись в JSON-файл
        """
        with open(filename, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
