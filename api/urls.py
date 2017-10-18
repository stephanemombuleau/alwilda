from apistar import Route
from .search import search_address


api_urls = [
    Route('/search', 'GET', search_address)
]