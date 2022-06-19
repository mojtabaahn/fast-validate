from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class AlphaRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['alpha']

    def validate(self, field: Any, value: Any) -> bool:
        return isinstance(value, str) and value.isalpha()

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be alpha'
