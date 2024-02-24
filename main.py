from src.sorting_funcs import get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies, \
    string_to_number
from src.vacancies_file import VacanciesJSON
from src.vacancies_service import HHVacanciesService
from src.vacancy import Vacancy

# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_vacancies_service = HHVacanciesService()


# Функция для взаимодействия с пользователем
def user_interaction():
    platforms = ["HeadHunter"]

    # Получение вакансий с hh.ru в формате JSON
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_vacancies_service.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    # Сохранение информации о вакансиях в файл
    vacancies_json = VacanciesJSON(vacancies_list)

    # Отбор вакансий по заданным параметрам
    top_n = string_to_number(input("Введите количество лучших вакансий для вывода: "))
    filter_words = input("Введите ключевые слова через пробел для фильтрации вакансий: ").split()

    salary = string_to_number(input("Введите минимальную зарплату. "
                                    "Для рассмотрения вакансий без укзанаия зарплаты, введите 0: "))

    filtered_vacancies = vacancies_json.filter_vacancies(filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary)

    sorted_vacancies = sort_vacancies(ranged_vacancies)

    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
