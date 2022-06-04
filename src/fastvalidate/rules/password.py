import re
from typing import Any, Union, List, Tuple, Optional

from fastvalidate.rule_abstract import RuleAbstract, ComplexRuleAbstract


class PasswordRule(ComplexRuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['password']

    def validate_with_message(self, field: Any, value: Any) -> Tuple[bool, Optional[str]]:
        if not isinstance(value, str):
            return False, 'Field must be string'

        if len(value) < 8:
            return False, 'Field must be at least 8 characters'

        if re.search(r"\d", value) is None:
            return False, 'Field must have at least one numeric characters'

        if re.search(r"[A-Z]", value) is None:
            return False, 'Field must have at least one uppercase characters'

        if re.search(r"[a-z]", value) is None:
            return False, 'Field must have at least one lowercase characters'

        if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', value) is None:
            return False, 'Field must have at least one symbol characters'

        return True, None

    def process(self, field: Any, value: Any) -> Any:
        return value
