from apistar import Route
from .search import instant_answer


api_urls = [
    Route('/instant_answer', 'GET', instant_answer)
]
