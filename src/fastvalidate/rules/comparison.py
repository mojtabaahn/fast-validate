import abc
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class ComparisonRule(RuleAbstract, abc.ABC):

    def __init__(self, threshold: int) -> None:
        super().__init__()
        self._threshold = int(threshold)

    @abc.abstractmethod
    def compare(self, value: int, threshold: int) -> bool:
        pass

    def validate(self, field: Any, value: Any) -> bool:
        if isinstance(value, int): return self.compare(value, self._threshold)
        if isinstance(value, str) and value.isnumeric(): return self.compare(int(value), self._threshold)
        return False

    def process(self, field: Any, value: Any) -> Any:
        return int(value)


class GreaterThanRule(ComparisonRule):
    def compare(self, value: int, threshold: int) -> bool:
        return value > threshold

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['gt']

    def message(self) -> str:
        return f'Field must be greater than {self._threshold}'


class GreaterThanEqualRule(ComparisonRule):
    def compare(self, value: int, threshold: int) -> bool:
        return value >= threshold

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['gte']

    def message(self) -> str:
        return f'Field must be greater than or equal {self._threshold}'


class LessThanRule(ComparisonRule):
    def compare(self, value: int, threshold: int) -> bool:
        return value < threshold

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['lt']

    def message(self) -> str:
        return f'Field must be less than {self._threshold}'


class LessThanEqualRule(ComparisonRule):
    def compare(self, value: int, threshold: int) -> bool:
        return value <= threshold

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['lte']

    def message(self) -> str:
        return f'Field must be less than or equal {self._threshold}'
