from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.renderers import JSONRenderer

from api.urls import api_urls

settings = {
    'RENDERERS': [JSONRenderer()]
}

routes = [
    Include('/docs', docs_urls),
    Include('/static', static_urls),
    Include('/api/v1', api_urls),
]

app = App(routes=routes, settings=settings)


if __name__ == '__main__':
    app.main()
