from fastvalidate.validator import Validator


def test_validator():
    validator = Validator(
        data=dict(name=None),
        rules=dict(name='required')
    )

    result = validator.validate()
    assert result.errors() == dict(name='Field is required')


def test_read_me():
    validator = Validator({
        'first_name': 'Mo',
        'last_name': None,
        'age': '5',
        'email': 'mojtabaa.hn@gmail',
        'website': 'https://mojtabaahn',
        'languages': ['en', 'fa'],
    }, {
        'first_name': 'required|min:3',
        'last_name': 'required|min:3',
        'age': 'required|numeric|gt:10|lt:120',
        'email': 'required|email',
        'website': 'required|url',
        'languages': 'required|list|min:3'
    })

    assert validator.validate().errors()['website'] == 'Field must be url'