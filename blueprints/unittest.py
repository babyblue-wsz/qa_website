import pytest


def get_result(str_to_result):
    if '+' in str_to_result:
        res = str_to_result.split('+')
        return int(res[0]) + int(res[1])
    if '-' in str_to_result:
        res = str_to_result.split('-')
        return int(res[0]) - int(res[1])
    if '*' in str_to_result:
        res = str_to_result.split('*')
        return int(res[0]) * int(res[1])
    if '/' in str_to_result:
        res = str_to_result.split('/')
        return int(res[0]) / int(res[1])
@pytest.mark.increase
def test_get_result():
    data1 = '100+5'
    assert get_result(data1) == 105


@pytest.mark.reduce
def test_get_result1():
    data2 = '100-5'
    assert get_result(data2) == 95


@pytest.mark.increase
def test_get_result2():
    data3 = '100*5'
    assert get_result(data3) == 500


@pytest.mark.reduce
def test_get_result3():
    data4 = '100/5'
    assert get_result(data4) == 20.0