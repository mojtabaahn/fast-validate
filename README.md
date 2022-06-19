![Packagist License](https://img.shields.io/packagist/l/mojtabaahn/fast-validate?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/mojtabaahn/fast-validate?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/fastvalidate?style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/fastvalidate?style=for-the-badge)

#### Requirements

- Python 3.6+

#### Installation & Upgrade

```shell
pip install fastvalidate --upgrade
```

#### Dictionary Validation

```python
from fastvalidate import Validator

validator = Validator({
    'first_name': 'Mo',
    'last_name': None,
    'age': '5',
    'email': 'mojtabaa.hn@gmail',
    'website': 'yup',
    'languages': ['en', 'fa'],
}, {
    'first_name': 'required|min:3',
    'last_name': 'required|min:3',
    'age': 'required|numeric|gt:10|lt:120',
    'email': 'required|email',
    'website': 'required|url',
    'languages': 'required|list|min:3'
})

validator.validate().errors()
# {
#     'first_name': 'Field length must be at least 3 characters',
#     'last_name': 'Field is required',
#     'age': 'Field must be greater than 10',
#     'email': 'Field must be email',
#     'website': 'Field must be url',
#     'languages': 'Field must have at least 3 items'
# }
```

#### Pydantic Validation

```python
from fastvalidate import BaseModel


class User(BaseModel):
    email: str
    website: str

    class Config:
        rules = dict(
            email='required|email|min:3',
            website='required|url|min:3'
        )


user = User(email='whatever', website='whoever')
# ValidationError
# [
#     dict(loc=('email',), msg='Field must be email', type='value_error'),
#     dict(loc=('website',), msg='Field must be url', type='value_error')
# ]

```

#### Available Rules

| Type               | Applicable              On         | signature                                        |
| ----               | ----                               | ----                                             |
| Boolean            | string, boolean                    | `bool`, `boolean`                                |
| Numeric            | string, integer                    | `numeric`, `int`, `integer`                      |
| List               | string(json), list                 | `list`, `array`                                  |
| Dictionary         | string(json), dict                 | `dict`                                           |
| Email              | string                             | `email`                                          |
| Password           | string                             | `password`                                       |
| RegEx              | string                             | `regex:<pattern>`                                |
| URL                | string                             | `url`                                            |
| Length             | string, integer, float, list, dict | `len:<length>`, `length:<length>`                |
| Min                | string, integer, float, list, dict | `min:<threshold>`                                |
| Max                | string, integer, float, list, dict | `max:<threshold>`                                |
| Choice             | string                             | `choice:<x>,<y>,<z>` `in:<x>,<y>,<z>`            |
| Greater Than       | int                                | `gt:<threshold>`                                 |
| Greater Than Equal | int                                | `gte:<threshold>`                                |
| Less Than          | int                                | `lt:<threshold>`                                 |
| Less Than Equal    | int                                | `lte:<threshold>`                                |
| Alpha              | string                             | `alpha`                                          |
| Alpha Numeric      | string                             | `alpha_num`,`alpha_numeric`                      |
| Alpha Num Dash     | string                             | `alpha_dash`                                     |
| Date               | string                             | `date`                                           |
| UUID               | string                             | `uuid`                                           |
| IPV4               | string                             | `ipv4`                                           |
| IPV6               | string                             | `ipv6`                                           |
| IP                 | string                             | `ip`                                             |
| Mac Address        | string                             | `mac`,`mac_address`                              |

#### Testing

```bash
# install pytest
pip install pytest

# run tests
python -m pytest
```