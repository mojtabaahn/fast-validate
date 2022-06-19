import re
import uuid
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class UUIDRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['uuid']

    def validate(self, field: Any, value: Any) -> bool:
        try:
            uuid.UUID(value)
            return True
        except Exception:
            return False

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be a valid uuid'
