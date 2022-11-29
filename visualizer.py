def build_html_for_one_candidate(candidate):
    code_for_candidate = ""

    code_of_candidate += f"<img src=\"{candidate[name]}\">\n"
    code_of_candidate += f"{candidate['name']}\n"
    code_of_candidate += f"{candidate['skills']}\n"
    code_of_candidate += f"{candidate['position']}\n"
    code_of_candidate += "\n"

    return "<pre>" + code_for_candidates + "</pre>"


def build_html_some_candidates(candidates):
    list_of_candidates = ""

    for candidate in candidates:
        list_of_candidates += f"{candidate['name']}\n"
        list_of_candidates += f"{candidate['skills']}\n"
        list_of_candidates += f"{candidate['position']}\n"
        list_of_candidates += "\n"

        return "<pre>" + list_of_candidates + "</pre>"