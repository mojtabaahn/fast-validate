from typing import Any

from pydantic import BaseModel as PydanticBaseModel, root_validator, validator, ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.fields import ModelField

from fastvalidate import Validator


class BaseModel(PydanticBaseModel):
    @validator('*')
    def custom_validation(cls, value, field: ModelField, values, config):
        rules = getattr(config, 'rules', {})
        field_name = field.name
        validator_ = Validator({**values, field_name: value}, {field_name: rules.get(field_name, [])})
        result = validator_.validate()
        if result.fails(): raise ValueError(result.errors()[field_name])
        return value
