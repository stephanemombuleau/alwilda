from apistar.exceptions import ValidationError


def search_address(q: str):
    if q is None:
        # value is None if the query param is absent in request
        raise ValidationError({'q': '"q" is required'})

    return {
        'q': q,
        'is_address': False
    }
