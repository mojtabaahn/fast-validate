from typing import Dict, List, Union, Type

from fastvalidate.rule_abstract import RuleAbstract
from fastvalidate.rules.alpha import AlphaRule
from fastvalidate.rules.alpha_dash import AlphaDashRule
from fastvalidate.rules.alpha_num import AlphaNumRule
from fastvalidate.rules.boolean import BoolRule
from fastvalidate.rules.choice import ChoiceRule
from fastvalidate.rules.comparison import GreaterThanRule, GreaterThanEqualRule, LessThanRule, LessThanEqualRule
from fastvalidate.rules.date import DateRule
from fastvalidate.rules.dict import DictRule
from fastvalidate.rules.email import EmailRule
from fastvalidate.rules.len import LenRule
from fastvalidate.rules.list import ListRule
from fastvalidate.rules.max import MaxRule
from fastvalidate.rules.min import MinRule
from fastvalidate.rules.network import Ipv4Rule, Ipv6Rule, IpRule, MacAddressRule
from fastvalidate.rules.numeric import NumericRule
from fastvalidate.rules.password import PasswordRule
from fastvalidate.rules.regex import RegexRule
from fastvalidate.rules.required import RequiredRule
from fastvalidate.rules.url import UrlRule
from fastvalidate.rules.uuid import UUIDRule

AVAILABLE_RULES: List[Type[RuleAbstract]] = [
    RequiredRule,
    BoolRule,
    GreaterThanRule,
    GreaterThanEqualRule,
    LessThanRule,
    LessThanEqualRule,
    DictRule,
    ListRule,
    EmailRule,
    ChoiceRule,
    LenRule,
    MinRule,
    MaxRule,
    NumericRule,
    PasswordRule,
    RegexRule,
    UrlRule,
    AlphaRule,
    AlphaDashRule,
    AlphaNumRule,
    DateRule,
    Ipv4Rule,
    Ipv6Rule,
    IpRule,
    MacAddressRule,
    UUIDRule,
]


class ValidationResult:

    def __init__(self, errors: Dict[str, str], values: Dict[str, str]) -> None:
        self.__errors = errors
        self.__values = values

    def errors(self) -> Dict[str, str]:
        return self.__errors

    def values(self) -> Dict[str, str]:
        return self.__values

    def fails(self) -> bool:
        return len(self.__errors.items()) > 0

    def passes(self) -> bool:
        return len(self.__errors.items()) == 0


class Validator:

    def __init__(self, data: Dict, rules: Dict[str, Union[List[Union[str, RuleAbstract]], str]]) -> None:
        self.__data = data
        self.__available_rules: Dict[str, Type[RuleAbstract]] = self.__parse_available_rules()
        self.__rules: Dict[str, List[RuleAbstract]] = self.__parse_rules(rules)

    def __parse_rules(self, rules: Dict[str, Union[List[Union[str, RuleAbstract]], str]]) -> Dict[str, List[RuleAbstract]]:
        for field, rule_set in rules.items():
            if isinstance(rule_set, str): rule_set = rule_set.split("|")
            for index, rule in enumerate(rule_set):
                if isinstance(rule, str): rule_set[index] = self.__rule_from_string(rule)
            rules[field] = rule_set

        return rules

    def __rule_from_string(self, rule: str) -> RuleAbstract:
        slug, separator, args = rule.partition(':')
        args = args.split(",") if separator != '' else []
        rule_class: Type[RuleAbstract] = self.__available_rules.get(slug, None)
        if rule_class is None: raise Exception(f"Rule with signature of {slug} is not supported")
        return rule_class(*args)

    def validate(self) -> ValidationResult:
        errors = dict()
        values = dict()
        for field, value in self.__data.items():
            rules: List[RuleAbstract] = self.__rules.get(field, [])
            for rule in rules:
                if rule.validate(field, value):
                    value = rule.process(field, value)
                else:
                    errors[field] = rule.message()
                    break
            values[field] = value

        return ValidationResult(errors, values)

    def __parse_available_rules(self):
        rules = dict()
        for rule in AVAILABLE_RULES:
            slugs = rule.slug()
            slugs = slugs if isinstance(slugs, list) else [slugs]
            rules = dict(**rules, **{slug: rule for slug in slugs})

        return rules
