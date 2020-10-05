import datetime


def translate_date(some_str):
    """
    We expect day/month/year

    We don't use strptime because we don't have leading 0s
    """
    if not some_str:
        return None
    day, month, year = some_str.strip().split("/")
    if int(year) > datetime.date.today().year:
        year = "19{}".format(year)
    else:
        year = "20{}".format(year)

    return datetime.date(int(year), int(month), int(day))


def get_and_check(row_value, choices):
    row_value = row_value.strip()
    if not row_value:
        return None
    if row_value not in [i[0] for i in choices]:
        raise ValueError("{} not in {}".format(row_value, choices))
    return row_value


def no_yes_unknown(row_value):
    NO_YES_UNKNOWN = {
        0: "No", 1: "Yes", 2: "Unknown"
    }
    return NO_YES_UNKNOWN.get(int(row_value))


def get_and_check_ll(row_value, ll):
    row_value = row_value.strip()
    if not row_value:
        return
    if not ll.objects.filter(name=row_value).exists():
        raise ValueError("{} not in {}".format(row_value, ll))
    return row_value


def get_or_create_ll(row_value, ll):
    row_value = row_value.strip()
    if not row_value:
        return
    ll.objects.get_or_create(name=row_value)
    return row_value


def int_or_non(row_value):
    row_value = row_value.strip()
    if not row_value:
        return
    return int(row_value)



