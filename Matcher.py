import re

from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class IsEmail(BaseMatcher):
    def __init__(self):
        pass

    def _matches(self, item):
        regexp = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return re.match(regexp, item)

    def describe_to(self, description):
        description.append_text("Is a valid email address.")


def valid_email():
    return IsEmail()
