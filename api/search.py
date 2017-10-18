from apistar.exceptions import ValidationError


def search_address(q: str):
    """
    Check if the query should display a map

    :param q: (str) - User query
    :return: (dict) - JSON response
    """
    if q is None:
        # value is None if the query param is absent in request
        raise ValidationError({'q': '"q" is required'})

    return {
        'q': q,
        'is_address': False
    }
