import re
from datetime import date
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validator_mobileNumber(value):
    if not re.findall('^(\+91)([789]\d{2})-?(\d{3})-?(\d{4})|^[789]\d{9}', value):
        raise ValidationError( _("The mobile number must be as indian number."),code='mobile_number',
        params={'mobile_number': value})
    # return value


def validator_password(value ):
    min_digits=1
    if not len(re.findall('\d', value)) >= min_digits:
        raise ValidationError(
            _("The password must contain at least 1 digit(s), 0-9."),
            code='password_no_number',
        )
    if not re.findall('[A-Z]', value):
        raise ValidationError(
            _("The password must contain at least 1 uppercase letter, A-Z."),
            code='password_no_upper'
        )
    if not re.findall('[a-z]', value):
        raise ValidationError(
            _("The password must contain at least 1 lowercase letter, a-z."),
            code='password_no_lower'
        )
    if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
        raise ValidationError(
            _("The password must contain at least 1 symbol: " +
                "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?"),
            code='password_no_symbol'
        )    
    # return value


def validator_dob(dob):
    today = date.today()
    # age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if dob > today:
        raise ValidationError(_("Date of birth should not be future date."),code='dob_error')
    # return dob