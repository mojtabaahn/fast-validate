#### Requirements

- Python 3.6+

#### Installation & Upgrade

```shell
pip install fastvalidate --upgrade
```

#### Usage

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

#### Testing

```bash
# install pytest
pip install pytest

# run tests
python -m pytest
```

#### Development

```bash
# install requirements
pip install build twine

# Build package
make build

# Push to basalam repository
make push
```