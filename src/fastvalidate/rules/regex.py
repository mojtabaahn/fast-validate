import re
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class RegexRule(RuleAbstract):

    def __init__(self, pattern: str) -> None:
        super().__init__()
        self.__pattern = pattern

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['regex']

    def validate(self, field: Any, value: Any) -> bool:
        return isinstance(value, str) and re.fullmatch(self.__pattern, value) is not None

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field is not valid'
