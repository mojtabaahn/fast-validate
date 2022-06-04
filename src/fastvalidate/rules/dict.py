import json
from json import JSONDecodeError
from typing import Any, Union, List, Optional, Dict

from fastvalidate.rule_abstract import RuleAbstract


class DictRule(RuleAbstract):
    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['dict', 'dictionary']

    def message(self) -> str:
        return 'Field must be dictionary'

    def __dict_from_string(self, string: str) -> Optional[Dict]:
        try:
            string = json.loads(string)
            if isinstance(string, dict): return string
            return None
        except JSONDecodeError:
            return None

    def validate(self, field: Any, value: Any) -> bool:
        if isinstance(value, dict): return True
        if isinstance(value, str): return self.__dict_from_string(value) is not None
        return False

    def process(self, field: Any, value: Any) -> Any:
        if isinstance(value, dict): return value
        if isinstance(value, str): return self.__dict_from_string(value)
        return None
