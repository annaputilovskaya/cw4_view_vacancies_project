from abc import ABC, abstractmethod


class VacanciesFile(ABC):
    """
    Абстрактный класс для работы с файлом вакансий
    """
    @ abstractmethod
    def add_vacancies(self) -> None:
        """
        Добавляет вакансии в файл
        """

    @abstractmethod
    def chose_vacancies(self, *args, **kwargs):
        """
        Получает данные из файла с вакансиями по указанным критериям
        """

    @abstractmethod
    def delete_vacancies(self) -> None:
        """
        Удаляет информацию о вакансиях из файла
        """


class VacanciesJSON(VacanciesFile):
    """
    Класс для сохранения информации о вакансиях в JSON-файле
    """
    def add_vacancies(self) -> None:
        """
        Добавляет вакансии в JSON-файл
        """

    def chose_vacancies(self, *args, **kwargs):
        """
        Получает данные из JSON-файла с вакансиями по указанным критериям
        """

    def delete_vacancies(self) -> None:
        """
        Удаляет информацию о вакансиях из JSON-файла
        """
