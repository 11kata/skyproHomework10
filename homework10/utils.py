import json
from pprint import pprint as pp
from homework import DATA_PATH


def _load_data(path=DATA_PATH):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def all_candidates():
    """Загрузка всех кандидатов"""
    data = _load_data()
    return data


def candidates_pk(pk):
    """ Загрузка кандидатов по PK"""
    candidates = _load_data()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate


def candidates_skill(skill_name):
    """Загрузка скиллов кандидата"""

    skill_candidates = []
    skill_name_lower = skill_name.lower()
    candidates = _load_data()
    for candidate in candidates:
        skills = candidate['skill'].loswer().strip().split(', ')
        if skill_name_lower in skills:
            skill_candidates.append(candidates)
            continue
    return skill_candidates
