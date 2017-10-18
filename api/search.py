from apistar import http


def search_address(request: http.Request, q: str):
    if q is None:
        # value is None if the query param is absent in request
        q = ''

    return {
        'q': q,
        'is_address': False
    }
