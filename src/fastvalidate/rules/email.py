import re
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class EmailRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['email']

    def validate(self, field: Any, value: Any) -> bool:
        return isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value)

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be email'
