import re
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class AlphaDashRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['alpha_dash']

    def validate(self, field: Any, value: Any) -> bool:
        return isinstance(value, str) and re.fullmatch(r'[a-zA-Z0-9-]+', value) is not None

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be alphanumeric and dash'
