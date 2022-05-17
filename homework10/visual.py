def build_html_for_candidate(candidate):
    """ Создает HTML код для одного кандидата"""
    list_of_candidates = ''
    list_of_candidates += f'<img src=\"{candidate["picture"]}\">\n'
    list_of_candidates += f'{candidate["name"]}\n'
    list_of_candidates += f'{candidate["skills"]}\n'
    list_of_candidates += f'{candidate["position"]}\n'
    list_of_candidates += '\n'
    return '<pre>' + list_of_candidates + '</pre>'


def build_html_for_some_candidates(candidates):
    """ Формирует HTML для нескольких кандидатов"""
    list_of_candidates = ''

    for candidate in candidates:

        list_of_candidates += f'{candidate["name"]}\n'
        list_of_candidates += f'{candidate["skills"]}\n'
        list_of_candidates += f'{candidate["position"]}\n'
        list_of_candidates += '\n'

    return '<pre>'+list_of_candidates+'</pre>'
