import hashlib


def is_eq_str(a: str, b: str, verbose = False) -> bool:
    assert len(a) > 0 and len(b) > 0, 'Строки не могут быть пустыми'

    ha = hashlib.sha1(a.encode('utf-8')).hexdigest()
    hb = hashlib.sha1(b.encode('utf-8')).hexdigest()

    if verbose:
        print(f'hash 1 = {ha}\nhash 2 = {hb}')

    return ha == hb


s_1 = input('Строка 1: ') 
s_2 = input('Строка 2: ')

print('Одинаковые' if is_eq_str(s_1, s_2, True) else 'Разные')