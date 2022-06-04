import json
from json import JSONDecodeError
from typing import Any, Union, List, Optional

from fastvalidate.rule_abstract import RuleAbstract


class ListRule(RuleAbstract):
    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['list', 'array']

    def message(self) -> str:
        return 'Field must be array'

    def __list_from_string(self, string: str) -> Optional[List]:
        try:
            string = json.loads(string)
            if isinstance(string, list): return string
            return None
        except JSONDecodeError:
            return None

    def validate(self, field: Any, value: Any) -> bool:
        if isinstance(value, list): return True
        if isinstance(value, str): return self.__list_from_string(value) is not None
        return False

    def process(self, field: Any, value: Any) -> Any:
        if isinstance(value, list): return value
        if isinstance(value, str): return self.__list_from_string(value)
        return None
