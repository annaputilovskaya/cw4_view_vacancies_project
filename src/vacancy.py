class Vacancy:
    """
    Класс для работы с вакансией
    """
    all = []

    def __init__(self, title=None, url=None, salary=0, requirements=None, area=None, employer=None):
        """
        Создает объект класса Vacancy
        """
        self.title = title
        self.url = url
        self.salary = salary
        self.requirements = requirements
        self.area = area
        self.employer = employer

    def __str__(self) -> str:
        """
        Отображает информацию о ваканси для пользователей
        """
        return f'{self.title}: {self.salary}'

    def __repr__(self) -> str:
        """
        Отображает информацию о вакансии для разработчика
        """
        return (f'{self.__class__.__name__}({self.title}, {self.url}, {self.salary}, '
                f'{self.requirements}, {self.area}, {self.employer})')

    def __ge__(self, other) -> bool:
        """
        Проверяет, является ли зарпата по данной вакансии выше или равна другой
        """
        if isinstance(other, self.__class__):
            return self.salary >= other.salary
        elif isinstance(other, int):
            return self.salary >= other
        else:
            raise TypeError("Сравнение данных объектов невозможно")

    def __gt__(self, other) -> bool:
        """
        Проверяет, является ли зарпата по данной вакансии выше другой
        """
        if isinstance(other, self.__class__):
            return self.salary > other.salary
        elif isinstance(other, int):
            return self.salary > other
        else:
            raise TypeError("Сравнение данных объектов невозможно")

    def __le__(self, other) -> bool:
        """
        Проверяет, является ли зарпата по данной вакансии ниже или равна другой
        """
        if isinstance(other, self.__class__):
            return self.salary <= other.salary
        elif isinstance(other, int):
            return self.salary <= other
        else:
            raise TypeError("Сравнение данных объектов невозможно")

    def __lt__(self, other) -> bool:
        """
        Проверяет, является ли зарпата по данной вакансии ниже другой
        """
        if isinstance(other, self.__class__):
            return self.salary < other.salary
        elif isinstance(other, int):
            return self.salary < other
        else:
            raise TypeError("Сравнение данных объектов невозможно")

    def __contains__(self, words):
        """
        Проверяет, содержит ли вакансия ключевые слова
        """
        flag = False
        for word in words:
            if word in self.requirements:
                flag = True
                break
        return flag

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        """
        Устанавливает значение зарплаты.
        Если в вакансии не указан размер зарплаты или
        неизвестен курс перевода валюты, зарплата устанавливается  равной 0.
        """
        if isinstance(salary, dict):
            currency = salary.get('currency')
            if currency == 'RUR':
                salary = salary.get('from')
            else:
                salary = Vacancy.convert_to_rub(currency, salary.get('from'))

        if isinstance(salary, (int, float)):
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
            Vacancy.all.append(vacancy)
        return Vacancy.all
