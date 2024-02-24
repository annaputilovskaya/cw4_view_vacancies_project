def sort_vacancies(vacancies_list) -> list:
    """
    Сортирует список вакансий по зарплате в порядке убывания
    """
    return sorted(vacancies_list, reverse=True)


def get_top_vacancies(vacancies_list, top_n: int) -> list:
    """
    Отбирает n-количество вакансий
    """
    if top_n == 0:
        return vacancies_list
    return vacancies_list[:top_n]


def get_vacancies_by_salary(vacancies_list, salary) -> list:
    """
    Отбирает вакансии c уровнем зарплаты выше заданного
    """
    new_list = []
    for vacancy in vacancies_list:
        if vacancy >= salary:
            new_list.append(vacancy)
    return new_list


def print_vacancies(vacancies_list) -> None:
    """
    Выводит в консоль список вакансий
    """
    counter = 1
    for vacancy in vacancies_list:
        print(f'{counter}) {vacancy.title}: {vacancy.salary}\n'
              f'   {vacancy.area}, {vacancy.employer}\n'
              f'   {vacancy.url}\n'
              f'   {vacancy.requirements}')
        counter += 1


def string_to_number(string) -> int:
    """
    Возвращает число из числа-строки
    :param string: строка
    :return: число
    """
    try:
        number = int(float(string))
        return number
    except ValueError:
        return 0
