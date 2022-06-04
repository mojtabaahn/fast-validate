import re
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class UrlRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['url']

    def validate(self, field: Any, value: Any) -> bool:
        pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        return re.fullmatch(pattern, value) is not None

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be url'
