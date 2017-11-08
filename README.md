# alwilda
Alwilda is an API around Geo services.

For the moment it provides only one route `/v1/instant_answer` to check if a query is an address.

## Architecture

Alwilda has been made with [api star](https://github.com/encode/apistar)

The address caracterization uses [addr_detector](https://github.com/rdoume/addr_detector) for the adress detection.

## Installation

Alwilda depends on python 3.6 and [pipenv](https://docs.pipenv.org/).

To install the dependencies just run:
`pipenv install`

you also need libpostal and fasttext

#### Installation of Postal:
Before you install `Postal`, make sure you have the following prerequisites:

    sudo apt-get install curl autoconf automake libtool pkg-config

Then to install the C library:

    git clone https://github.com/openvenues/libpostal
    cd libpostal
    ./bootstrap.sh
    ./configure --datadir=[...some dir with a few GB of space...]
    make
    sudo make install

    # On Linux it's probably a good idea to run
    sudo ldconfig

#### Installation of FastText

In order to build `fastText`, use the following:

    git clone https://github.com/facebookresearch/fastText.git
    cd fastText
    make


## Running the API

`apistar run`

You can then query it:

```bash
curl 'http://localhost:8080/v1/instant_answer?q=1%20Avenue%20des%20Champs-Élysées%20Paris'

```

## Running the tests

`apistar test`
