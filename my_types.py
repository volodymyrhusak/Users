# -*- coding: utf-8 -*-
from schematics.exceptions import ValidationError
from schematics.types import BaseType


class PhoneType(BaseType):
    MESSAGES = {
        'plus': 'Phone must start with + and length must be 11'
    }

    def validatePhone(self, value):
        if not value.startswith('+') or len(value) != 11:
            raise ValidationError(self.messages['plus'])


if __name__ == '__main__':
    p = PhoneType()
    p.validatePhone('123')
