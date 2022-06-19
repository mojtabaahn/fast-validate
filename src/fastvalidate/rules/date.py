from typing import Any, Union, List

import arrow
from arrow import ParserError

from fastvalidate.rule_abstract import RuleAbstract


class DateRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['date']

    def validate(self, field: Any, value: Any) -> bool:
        try:
            arrow.get(value)
            return True
        except ParserError:
            return False

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be a valid date'
