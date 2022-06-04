from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class RequiredRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['required', 'req']

    def validate(self, field: Any, value: Any) -> bool:
        return value is not None and value != ''

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field is required'
