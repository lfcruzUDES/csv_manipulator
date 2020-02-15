"""Functions for program."""
import csv


def get_datas(path_file):
    """
    Get data from CSV

    Args:
        path_file (string): Path to file.

    Returns:
        dict: {
        headers: list,
        datas: list of list
        }

    """
    datas = None
    with open(path_file, 'r') as f:
        datas = [list(row) for row in csv.reader(f)]

    return {
        'headers': datas[0],
        'datas': datas[1:]
    }


def save_datas(path_file, datas):
    """
    Save datas in file from datas.

    Args:
        - path_file (string): Path to file.
        - datas (list of list): Datas to save.

    Returns:
        None
    """
    if datas:
        with open(path_file, 'w') as f:
            wf = csv.writer(f)
            wf.writerows(datas)
    else:
        raise Exception('There are not data to save.')


def get_headers(datas):
    """
    Return first column.

    Args:
        - datas (list of list): Datas to work.

    Returns:
        list: Return numbered headers.
    """

    headers = datas
    numbered_headers = [(index + 1, value)
                        for index, value in enumerate(headers)]
    return numbered_headers


def extract_cols(datas, cols):
    """
    A short description.

    Args:
        - datas (list of list): Data to work.
        - cols (list): cols to extract.

    Returns:
        list of tuples: description
    """

    if type(cols) != list:
        raise Exception('cols param must be a list type.')
    if not cols:
        raise Exception('cols param is empty.')
    if not datas:
        raise Exception('There are not datas to work.')

    splited_datas = []
    for data in datas:
        row = []
        for col in cols:
            if '-' in col:
                value_joined = ''
                splited_col = col.split('-')
                for sc in splited_col:
                    value_joined += f"{data[int(sc) - 1]} "
                row.append(value_joined.strip())
            else:
                row.append(data[int(col) - 1])
        splited_datas.append(row)

    return splited_datas


def change_case(datas, cols):

    def case(data, param):
        if param == 'u':
            return data.upper()
        elif param == 'l':
            return data.lower()
        elif param == 'lu':
            return data.title()
        else:
            raise Exception("There is not a case coincidence.")

    for data in datas:
        for index, d in enumerate(data):
            if not 'a' in cols[0]:
                data[index - 1] = case(data[index - 1], cols[index - 1])
            else:
                case_param = cols[0].split('-')
                data[index - 1] = case(data[index - 1], case_param[1])

    return datas
