from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class ChoiceRule(RuleAbstract):

    def __init__(self, *args) -> None:
        super().__init__()
        self.__options = args

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['in', 'choice']

    def message(self) -> str:
        return f"Field must be one of {', '.join(self.__options)}"

    def validate(self, field: Any, value: Any) -> bool:
        return value in self.__options

    def process(self, field: Any, value: Any) -> Any:
        return value
