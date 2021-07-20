from typing import List

from test_framework import generic_test, test_utils
from string import ascii_uppercase

def phone_mnemonic(phone_number: str) -> List[str]:
    if not phone_number:
        return []
    mappings = {'0': '0', '1':'1', '2': 'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7': 'PQRS', '8':'TUV', '9':'WXYZ'}
    res = [letter for letter in mappings[phone_number[0]]]
    for n in phone_number[1:]:
        temp = []
        for letter in mappings[n]:
            for arr in res:
                temp.append(arr+letter)
        res = temp[:]
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
