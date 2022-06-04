import abc
from typing import Any, Union, List, Tuple, Optional


class RuleAbstract(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def slug(cls) -> Union[str, List[str]]: pass

    @abc.abstractmethod
    def message(self) -> str: pass

    @abc.abstractmethod
    def validate(self, field: Any, value: Any) -> bool: pass

    @abc.abstractmethod
    def process(self, field: Any, value: Any) -> Any: pass


class ComplexRuleAbstract(RuleAbstract, abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__message: str = ''

    @abc.abstractmethod
    def validate_with_message(self, field: Any, value: Any) -> Tuple[bool, Optional[str]]:
        pass

    def validate(self, field: Any, value: Any) -> bool:
        result, message = self.validate_with_message(field, value)
        self.__message = message
        return result

    def message(self) -> str:
        return self.__message
