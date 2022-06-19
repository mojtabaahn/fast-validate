import ipaddress
import re
from typing import Any, Union, List

from fastvalidate.rule_abstract import RuleAbstract


class Ipv4Rule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['ipv4']

    def validate(self, field: Any, value: Any) -> bool:
        try:
            ipaddress.IPv4Address(value)
            return True
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            return False

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be a valid ipv4'


class Ipv6Rule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['ipv6']

    def validate(self, field: Any, value: Any) -> bool:
        try:
            ipaddress.IPv6Address(value)
            return True
        except (ipaddress.AddressValueError, ipaddress.NetmaskValueError):
            return False

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be a valid ipv6'


class IpRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['ip']

    def validate(self, field: Any, value: Any) -> bool:
        try:
            ipaddress.ip_address(value)
            return True
        except ValueError:
            return False

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be a valid ip address'


class MacAddressRule(RuleAbstract):

    @classmethod
    def slug(cls) -> Union[str, List[str]]:
        return ['mac', 'mac_address']

    def validate(self, field: Any, value: Any) -> bool:
        pattern = "[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$"
        return isinstance(value, str) and re.fullmatch(pattern, value.lower()) is not None

    def process(self, field: Any, value: Any) -> Any:
        return value

    def message(self) -> str:
        return 'Field must be a valid mac address'
