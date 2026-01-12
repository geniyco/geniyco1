candidates_db = [
    {"name": "Олексій", "skills": ["Python", "Django", "Git", "SQL", "English", "Docker"]},
    {"name": "Марія", "skills": ["Java", "Spring", "SQL", "English", "Docker"]},
    {"name": "Іван", "skills": ["Python", "Git", "Linux"]},
    {"name": "Оксен не", "skills": ["Python", "FastAPI", "PostgreSOL", "Git", "English", "Docker"]}
]
vacancy_requirements = ["Python", "Django", "Git", "SQL", "Docker"]

def calculate_match(candidate_skills, required_skills):
    common_skills = set(candidate_skills).intersection(set(required_skills))
    missing_skills = set(required_skills) - set(candidate_skills)
    match_percent = (len(common_skills) / len(required_skills)) * 100 if required_skills else 0
    return {
        "match_percent": round(match_percent),
        "missing_skills": list(missing_skills),
        "is_perfect": match_percent == 100
    }

def find_best_candidates(candidates, vacancy_reqs):
    best_candidates = []
    for candidate in candidates:
        match_info = calculate_match(candidate["skills"], vacancy_reqs)
        if match_info["match_percent"] >= 50:
            candidate_report = {
                "name": candidate["name"],
                "match_info": match_info
            }
            best_candidates.append(candidate_report)
    return best_candidates

def print_report(results):
    for candidate_report in results:
        name = candidate_report["name"]
        match_p = candidate_report["match_info"]["match_percent"]
        missing = candidate_report["match_info"]["missing_skills"]

        print(f"Кандидат: {name}")
        print(f"Відповідність: {match_p}%")
        print(f"Не вистачає: {missing if missing else '[]'}\n")
if __name__ == "__main__":
    results = find_best_candidates(candidates_db, vacancy_requirements)
    print_report(results)
