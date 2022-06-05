import re
from typing import Optional, Any

import pytest
from pydantic import ValidationError, BaseConfig, Extra

from fastvalidate.pydantic import BaseModel

def test_base_model():
    class Model(BaseModel):
        first_name: str
        last_name: str
        email: str
        website: str

        class Config(BaseConfig):
            rules = dict(
                email='required|email|min:3',
                website='required|url|min:3'
            )

    try:
        Model(first_name='moji', last_name='hab', email='hi', website='hell')
    except ValidationError as err:
        print(err.errors())
