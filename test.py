"""Some TEST."""

from utils.functions import (change_case, extract_cols, get_datas, get_headers,
                             save_datas)

if __name__ == "__main__":
    datas = get_datas("./nombres.csv")
    print(get_headers(datas['headers']))

    print('*' * 30)

    extracted_cols = extract_cols(datas['datas'], ['1-3'])
    print(extracted_cols)
    print('*' * 30)

    case_change = change_case(datas['datas'], ['a-l'])
    print(case_change)
    print('*' * 30)

    save_datas('./nombres2.csv', datas['datas'])
