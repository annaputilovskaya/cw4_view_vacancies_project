import pytest

from src.vacancy import Vacancy


@pytest.fixture
def new_vacancy():
    vacancy1 = Vacancy("Python Developer", "", 100_000, "опыт работы от 3 лет")
    vacancy2 = Vacancy("Python Developer", "", {
        'currency': 'USD', 'from': 2000})
    vacancy3 = Vacancy("Python Developer", "", 'по результатам собеседования')
    return vacancy1, vacancy2, vacancy3


def test_initial_vacancy(new_vacancy):
    assert new_vacancy[0].title == "Python Developer"
    assert new_vacancy[0].url == ''
    assert new_vacancy[0].salary == 100000
    assert new_vacancy[0].requirements == "опыт работы от 3 лет"
    assert new_vacancy[0].area is None
    assert new_vacancy[0].employer is None
    assert new_vacancy[1].salary == 180000
    assert new_vacancy[1].requirements is None
    assert new_vacancy[2].salary == 0


def test_str_vacancy(new_vacancy):
    assert str(new_vacancy[0]) == 'Python Developer: 100000'
    assert str(new_vacancy[2]) == 'Python Developer: 0'


def test_repr_vacancy(new_vacancy):
    assert repr(new_vacancy[1]) == ("Vacancy(self.title='Python Developer', "
                                    "self.url='', self.salary=180000, "
                                    "self.requirements=None, self.area=None, self.employer=None)")


def test_lt_salary(new_vacancy):
    assert new_vacancy[0] < new_vacancy[1]


def test_gt_salary(new_vacancy):
    assert new_vacancy[1] > new_vacancy[2]