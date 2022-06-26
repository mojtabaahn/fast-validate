from typing import Dict, Any

from fastvalidate import Validator


def assert_validation_error_for_item(value: Any, rule: str, error: str):
    assert_validation_error(
        dict(field_name=value),
        dict(field_name=rule),
        dict(field_name=error)
    )


def assert_no_validation_error_for_item(value: Any, rule: str):
    assert_no_validation_error(
        dict(field_name=value),
        dict(field_name=rule),
    )


def assert_validation_error(data: Dict, rules: Dict, errors):
    validator = Validator(data=data, rules=rules)

    result = validator.validate()
    assert result.errors() == errors


def assert_no_validation_error(data: Dict, rules: Dict):
    validator = Validator(data=data, rules=rules)

    result = validator.validate()
    assert len(result.errors().keys()) == 0, result.errors()


def test_required():
    assert_validation_error_for_item(None, 'required', 'Field is required')

    assert_no_validation_error_for_item('Hi', 'required')


def test_bool():
    assert_no_validation_error_for_item('true', 'bool')
    assert_no_validation_error_for_item('false', 'bool')
    assert_no_validation_error_for_item(True, 'bool')
    assert_no_validation_error_for_item(False, 'bool')

    assert_validation_error_for_item('Hi', 'bool', 'Field must be boolean')


def test_numeric():
    assert_no_validation_error_for_item('1', 'numeric')
    assert_no_validation_error_for_item(1, 'numeric')

    assert_validation_error_for_item('Hi', 'numeric', 'Field must be numeric')


def test_list():
    assert_no_validation_error_for_item([], 'list')
    assert_no_validation_error_for_item(['1', 1], 'list')
    assert_no_validation_error_for_item('["1", 1]', 'list')

    assert_validation_error_for_item('Hi', 'list', 'Field must be array')


def test_dict():
    assert_no_validation_error_for_item({}, 'dict')
    assert_no_validation_error_for_item({"a": "b"}, 'dict')
    assert_no_validation_error_for_item('{"a": "b"}', 'dict')

    assert_validation_error_for_item('Hi', 'dict', 'Field must be dictionary')


def test_email():
    assert_no_validation_error_for_item('hello@there.com', 'email')

    assert_validation_error_for_item('Hi', 'email', 'Field must be email')


def test_password():
    assert_validation_error_for_item(1, 'password', 'Field must be string')
    assert_validation_error_for_item('123', 'password', 'Field must be at least 8 characters')
    assert_validation_error_for_item('qweasdzxc', 'password', 'Field must have at least one numeric characters')
    assert_validation_error_for_item('qweasdzxc123', 'password', 'Field must have at least one uppercase characters')
    assert_validation_error_for_item('QWEASDZXC123', 'password', 'Field must have at least one lowercase characters')
    assert_validation_error_for_item('QWEasdZXC123', 'password', 'Field must have at least one symbol characters')
    assert_no_validation_error_for_item('QWEasdZXC123@', 'password')


def test_regex():
    assert_validation_error_for_item('heLLo', 'regex:[a-z]{2}[A-Z]{3}', 'Field is not valid')
    assert_no_validation_error_for_item('heLLo', 'regex:[a-z]{2}[A-Z]{2}[a-z]{1}')


def test_url():
    assert_validation_error_for_item('heLLo', 'url', 'Field must be url')
    assert_no_validation_error_for_item('http://hello.com', 'url')


def test_length():
    assert_validation_error_for_item('heLLo', 'len:4', "Field must be 4 characters")
    assert_no_validation_error_for_item('heLLo', 'len:5')

    assert_validation_error_for_item(25, 'len:4', "Field must be 4 characters")
    assert_no_validation_error_for_item(22554, 'len:5')

    assert_validation_error_for_item(2.5, 'len:4', "Field must be 4 characters")
    assert_no_validation_error_for_item(22.54, 'len:5')

    assert_validation_error_for_item([1, 2, 3], 'len:4', "Field must have 4 items")
    assert_no_validation_error_for_item([1, 2, 3, 4], 'len:4')

    assert_validation_error_for_item(dict(a=1), 'len:4', "Field must have 4 items")
    assert_no_validation_error_for_item(dict(a=1, b=2, c=3, e=4), 'len:4')


def test_min():
    assert_validation_error_for_item(4, 'min:6', "Field must be greater that or equal 6")
    assert_no_validation_error_for_item(6, 'min:6')
    assert_no_validation_error_for_item(7, 'min:6')

    assert_validation_error_for_item(4.2, 'min:6', "Field must be greater that or equal 6")
    assert_no_validation_error_for_item(6.0, 'min:6')
    assert_no_validation_error_for_item(7.5, 'min:6')

    assert_validation_error_for_item("hello", 'min:6', "Field length must be at least 6 characters")
    assert_no_validation_error_for_item("helloO", 'min:6')
    assert_no_validation_error_for_item("helloOo", 'min:6')

    assert_validation_error_for_item([1, 2, 3, 4], 'min:6', "Field must have at least 6 items")
    assert_no_validation_error_for_item([1, 2, 3, 4, 5, 6], 'min:6')
    assert_no_validation_error_for_item([1, 2, 3, 4, 5, 6, 7], 'min:6')

    assert_validation_error_for_item(dict(a=1), 'min:3', "Field must have at least 3 items")
    assert_no_validation_error_for_item(dict(a=1, b=2, c=3), 'min:3')
    assert_no_validation_error_for_item(dict(a=1, b=2, c=3, d=4), 'min:3')


def test_max():
    assert_validation_error_for_item(7, 'max:6', "Field must be less that or equal 6")
    assert_no_validation_error_for_item(6, 'max:6')
    assert_no_validation_error_for_item(5, 'max:6')

    assert_validation_error_for_item(7.2, 'max:6', "Field must be less that or equal 6")
    assert_no_validation_error_for_item(6.0, 'max:6')
    assert_no_validation_error_for_item(5.5, 'max:6')

    assert_validation_error_for_item("helloOo", 'max:6', "Field length must be at most 6 characters")
    assert_no_validation_error_for_item("helloO", 'max:6')
    assert_no_validation_error_for_item("hello", 'max:6')

    assert_validation_error_for_item([1, 2, 3, 4, 5, 6, 7], 'max:6', "Field must have at most 6 items")
    assert_no_validation_error_for_item([1, 2, 3, 4, 5, 6], 'max:6')
    assert_no_validation_error_for_item([1, 2, 3, 4, 5], 'max:6')

    assert_validation_error_for_item(dict(a=1, b=2, c=3, d=4), 'max:3', "Field must have at most 3 items")
    assert_no_validation_error_for_item(dict(a=1, b=2, c=3), 'max:3')
    assert_no_validation_error_for_item(dict(a=1, b=2), 'max:3')


def test_choice():
    assert_validation_error_for_item('hi', 'choice:hello,greetings', "Field must be one of hello, greetings")
    assert_no_validation_error_for_item('hi', 'choice:hello,hi')


def test_gt():
    assert_validation_error_for_item(5, 'gt:6', "Field must be greater than 6")
    assert_validation_error_for_item(6, 'gt:6', "Field must be greater than 6")
    assert_no_validation_error_for_item(7, 'gt:6')


def test_gte():
    assert_validation_error_for_item(5, 'gte:6', "Field must be greater than or equal 6")
    assert_no_validation_error_for_item(6, 'gte:6')
    assert_no_validation_error_for_item(7, 'gte:6')


def test_lt():
    assert_validation_error_for_item(7, 'lt:6', "Field must be less than 6")
    assert_validation_error_for_item(6, 'lt:6', "Field must be less than 6")
    assert_no_validation_error_for_item(5, 'lt:6')


def test_lte():
    assert_validation_error_for_item(7, 'lte:6', "Field must be less than or equal 6")
    assert_no_validation_error_for_item(6, 'lte:6')
    assert_no_validation_error_for_item(5, 'lte:6')


def test_alpha():
    assert_validation_error_for_item('asd1', 'alpha', "Field must be alpha")
    assert_validation_error_for_item('asd-', 'alpha', "Field must be alpha")
    assert_no_validation_error_for_item('asdZXC', 'alpha')


def test_alpha_numeric():
    assert_validation_error_for_item('asd123!', 'alpha_num', "Field must be alpha numeric")
    assert_validation_error_for_item('asd123-', 'alpha_num', "Field must be alpha numeric")
    assert_no_validation_error_for_item('asd123', 'alpha_num')


def test_alpha_dash():
    assert_validation_error_for_item('asd123-_@', 'alpha_dash', "Field must be alphanumeric and dash")
    assert_no_validation_error_for_item('asd123-', 'alpha_dash')
    assert_no_validation_error_for_item('asd123', 'alpha_dash')


def test_alpha_numeric():
    assert_validation_error_for_item('asd123!', 'alpha_num', "Field must be alpha numeric")
    assert_validation_error_for_item('asd123-', 'alpha_num', "Field must be alpha numeric")
    assert_no_validation_error_for_item('asd123', 'alpha_num')


def test_date():
    assert_validation_error_for_item('hi', 'date', "Field must be a valid date")
    assert_no_validation_error_for_item('2020', 'date')
    assert_no_validation_error_for_item('2020-05', 'date')
    assert_no_validation_error_for_item('2020-05-05', 'date')


def test_uuid():
    assert_validation_error_for_item('asd', 'uuid', "Field must be a valid uuid")
    assert_no_validation_error_for_item('0dc755c0-eb84-4b9a-ac65-941e4d20e077', 'uuid')


def test_ipv4():
    assert_validation_error_for_item('127', 'ipv4', "Field must be a valid ipv4")
    assert_no_validation_error_for_item('127.0.0.1', 'ipv4')


def test_ipv6():
    assert_validation_error_for_item('127', 'ipv6', "Field must be a valid ipv6")
    assert_no_validation_error_for_item('2001:0db8:85a3:0000:0000:8a2e:0370:7334', 'ipv6')


def test_ip():
    assert_validation_error_for_item('127', 'ip', "Field must be a valid ip address")
    assert_no_validation_error_for_item('127.0.0.1', 'ip')
    assert_no_validation_error_for_item('2001:0db8:85a3:0000:0000:8a2e:0370:7334', 'ip')


def test_mac():
    assert_validation_error_for_item('00:00:5e', 'mac', "Field must be a valid mac address")
    assert_no_validation_error_for_item('00:00:5e:00:53:af', 'mac')
