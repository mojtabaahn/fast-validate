from typing import Any, Union, List, Tuple, Optional

from fastvalidate.rule_abstract import ComplexRuleAbstract


class MinRule(ComplexRuleAbstract):

    def __init__(self, threshold: int) -> None:
        super().__init__()
        self.__threshold = int(threshold)

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['min']

    def validate_with_message(self, field: Any, value: Any) -> Tuple[bool, Optional[str]]:
        if isinstance(value, int):
            return value >= self.__threshold, f"Field must be greater that or equal {self.__threshold}"

        if isinstance(value, float):
            return value >= self.__threshold, f"Field must be greater that or equal {self.__threshold}"

        if isinstance(value, str):
            return len(value) >= self.__threshold, f"Field length must be at least {self.__threshold} characters"

        if isinstance(value, list):
            return len(value) >= self.__threshold, f"Field must have at least {self.__threshold} items"

        if isinstance(value, dict):
            return len(value.keys()) >= self.__threshold, f"Field must have at least {self.__threshold} items"

        return False, None

    def process(self, field: Any, value: Any) -> Any:
        return value