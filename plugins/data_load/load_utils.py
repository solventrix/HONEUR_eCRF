import datetime


def cast_date(some_str):
    """
    We expect day/month/year
    """
    some_str = some_str.strip()
    if not some_str:
        return None
    try:
        return datetime.datetime.strptime(some_str, "%d/%m/%Y").date()
    except Exception:
        return datetime.datetime.strptime(some_str, "%Y-%m-%d").date()


def match_to_choice_if_possible(row_value, choices):
    row_value = row_value.strip()
    if not row_value:
        return None
    for c in choices:
        result = c[0]
        if result.lower() == row_value.lower():
            return result
    return ""


def get_from_ll(row_value, ll):
    row_value = row_value.strip()
    if not row_value:
        return

    # do a case insensitive lookup and return what we expect
    result = ll.objects.filter(name__iexact=row_value)
    if result.exists():
        return result.get().name
    else:
        return ""


def float_or_none(row_value):
    row_value = row_value.strip()
    if not row_value:
        return
    return float(row_value)
