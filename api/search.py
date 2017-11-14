from apistar import typesystem
from apistar.exceptions import ValidationError
from addr_detector.Fasttext_clf import Fasttext_clf
from addr_detector.Postal_clf import Postal_clf


class Result(typesystem.Object):
    properties = {
        'q': typesystem.string(),
        'is_address': typesystem.Boolean,
    }


fasttext = Fasttext_clf()
postal = Postal_clf()


def instant_answer(q: str) -> Result:
    """
    Check if the query should display a map
    """
    if q is None:
        # value is None if the query param is absent in request
        raise ValidationError({'q': '"q" is required'})

    postal_response = postal.predict(q)
    ft_response = fasttext.predict(q)

    # for the moment we decide that it's an address if fasttext and postal agree on it
    is_addr = postal_response and ft_response

    return Result(q=q, is_address=is_addr)
