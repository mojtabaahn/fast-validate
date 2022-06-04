from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class BoolRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['boolean', 'bool']

    def validate(self, field: Any, value: Any) -> bool:
        return isinstance(value, bool) or value in ['true', 'false']

    def process(self, field: Any, value: Any) -> Any:
        if isinstance(value, bool): return value
        if value == 'true': return True
        return False

    def message(self) -> str:
        return 'Field must be boolean'
