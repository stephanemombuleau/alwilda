# alwilda
Alwilda is an API around Geo services.

For the moment it provides only one route `/v1/instant_answer` to check if a query is an address.

## Architecture

Alwilda has been made with [api star](https://github.com/encode/apistar)

The address caracterization uses [TODO]()

## Installation

Alwilda depends on python 3.6 and [pipenv](https://docs.pipenv.org/).

To install the dependencies just run:
`pipenv install`

## Running the API

`apistar run`

You can then query it:

```bash
curl http://localhost:8008/v1/instant_answer?q=1 Avenue des Champs-Élysées Paris
```

## Running the tests

`apistar test`
