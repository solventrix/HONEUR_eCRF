import datetime
from entrytool.models import PatientDetails


def cast_date(some_str):
    """
    We expect day/month/year
    """
    some_str = some_str.strip()
    if not some_str:
        return None
    try:
        return datetime.datetime.strptime(some_str, "%d/%m/%Y").date()
    except:
        return datetime.datetime.strptime(some_str, "%Y-%m-%d").date()


def get_and_check(row_value, choices):
    row_value = row_value.strip()
    if not row_value:
        return None
    for c in choices:
        result = c[0]
        if result.lower() == row_value.lower():
            return result
    raise ValueError(
        "{} not in {}".format(row_value, [i[0] for i in choices])
    )


def no_yes_unknown(row_value):
    return get_and_check(row_value, PatientDetails.CHOICES)


def get_and_check_ll(row_value, ll):
    row_value = row_value.strip()
    if not row_value:
        return

    # do a case insensitive lookup and return what we expect
    result = ll.objects.filter(name__iexact=row_value)
    if result.exists():
        return result.get().name
    else:
        raise ValueError("{} not in {}".format(row_value, ll))


def int_or_none(row_value):
    row_value = row_value.strip()
    if not row_value:
        return
    return int(row_value)


def float_or_none(row_value):
    row_value = row_value.strip()
    if not row_value:
        return
    return float(row_value)
