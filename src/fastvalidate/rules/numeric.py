from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class NumericRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['numeric', 'number', 'int', 'integer']

    def validate(self, field: Any, value: Any) -> bool:
        if isinstance(value, int): return True
        if isinstance(value, str): return value.isnumeric()
        return False

    def process(self, field: Any, value: Any) -> Any:
        if isinstance(value, int): return value
        if isinstance(value, str): return int(value)

    def message(self) -> str:
        return 'Field must be numeric'
