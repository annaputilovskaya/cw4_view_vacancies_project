class Vacancy:
    """
    Класс для работы с вакансией
    """
    def __init__(self):
        self.title = None
        self.url = None
        self.salary = self.get_salary()
        self.requirements = None

    def get_salary(self) -> float:
        """
        Получает информацию о зарплате
        :return: Размер зарплаты. В случае, если зарплата не укзана, 0.
        """

        return self.salary

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
