class Vacancy:
    """
    Класс для работы с вакансией
    """
    all = []

    def __init__(self, title=None, url=None, salary=0, requirements=None, area=None, employer=None):
        self.title = title
        self.url = url
        self.salary = salary
        self.requirements = requirements
        self.area = area
        self.employer = employer

    def __str__(self):
        """
        Отображает информацию о ваканси для пользователей
        """
        return f'{self.title}: {self.salary}'

    def __repr__(self):
        """
        Отображает информацию о вакансии для разработчика
        """
        return (f'{self.__class__.__name__}({self.title}, {self.url}, {self.salary}, '
                f'{self.requirements}, {self.area}, {self.employer})')

    def __lt__(self, other) -> bool:
        """
        Проверяет, является ли зарпата по данной вакансии ниже, чем по другой вакансии
        """
        return self.salary < other.salary

    def __gt__(self, other) -> bool:
        """
        Проверяет, является ли зарпата по данной вакансии выше, чем по другой вакансии
        """
        return self.salary > other.salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if isinstance(salary, dict):
            currency = salary.get('currency')
            if currency == 'RUR':
                self.__salary = salary.get('from')
            else:
                self.__salary = Vacancy.convert_to_rub(currency, salary.get('from'))
        elif isinstance(salary, (int, float)):
            self.__salary = salary
        else:
            self.__salary = 0

    @staticmethod
    def convert_to_rub(currency, amount):
        """
        Переводит в рубли сумму в евро или долларах по заданному курсу
        """
        rates = {
            'EUR': 100,
            'USD': 90
        }
        rate = rates.get(currency)
        if rate is None:
            print('Нет информации о курсе валюты')
            return 0
        return amount * rate

    @classmethod
    def cast_to_object_list(cls, data) -> list:
        """
        Создает список объектов класса Vacancy по данным из JSON
        """
        for item in data:
            title = item.get('name')
            url = item.get('url')
            salary = item.get('salary')
            requirements = item.get('snippet').get('requirement')
            area = item.get('area').get('name')
            employer = item.get('employer').get('name')
            vacancy = Vacancy(title, url, salary, requirements, area, employer)
            Vacancy.all.append({
                'title': vacancy.title,
                'url': vacancy.url,
                'salary': vacancy.salary,
                'requirements': vacancy.requirements,
                'area': vacancy.area,
                'employer': vacancy.employer
            })
        return Vacancy.all
