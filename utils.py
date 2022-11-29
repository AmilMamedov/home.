import json

from config import DATA_PATH


def _load_data(path=DATA_PATH):
    with open(path, "r", encoding='utf-8') as file:
        data = json.data(file)
        return data


def candidates_get_all():
    data = _load_data()
    return data

def candidates_get_by_pk(pk):
    candidates = _load_data()
    for candidate in candidates:
        if candidate["id"] == pk:
            return candidate


def candidates_get_by_skill(skill_name):

     skilled_candidates = []
     skill_name_lower = skill_name.lower()

     candidates = _load_data()
     for candidate in candidates:
         skills = candidate["skills"].lower.strip().split(",")
         if skill_name_lower in skills:
             skilled_candidates.append(candidate)

     return skilled_candidates