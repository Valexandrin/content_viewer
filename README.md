# Content viewer

The service is designed for viewing content.
It's listening HTTP requests containing selection criteria, processing them by set of algorithms and generating response with HTML for showing relevant content via browser.

## Work steps description

The service split on two main parts: 'view' and 'client'.
'View' receives GET request, collect criteria and reaches out 'client' for image supply. After receiving answer 'view' renders template for browser.
'Client' has two main options for answer depending on request: image by categories and random image.
After start up 'client' collects data by reading 'config.csv' file, creates Image class instances and saves them into list sorted by amount_of_shows.
By each new request 'client' validates requested categories by comparing with avaliable, chooses all matching images, gets one from top, checks if it wasn't sent by previous responce and sends it back to 'view'. Data are being updated by decreasing amount_of_shows and changing position of Image instances in list according to this parameter. This approach allows to minimize amount_of_shows spending for instances with low value of it.
In case of request without categories 'client' answers by random image with all required activities in rest data.

### Configuration file

Add .env file by using .env.default.
Put 'config.csv' to 'data' folder. If you choose another location - put correct path in .env.

## Start up

### One-time action (if not poetry)

```bash
pip install poetry
poetry config virtualenvs.in-project true
source .env\Scripts\activate
```

### Install dependecies

```bash
poetry init
poetry install
```

## Usage

```bash
make run
```

## Resources used

```bash
Flask
pydantic - data validation and settings management
mypy - static types checker
wemake-python-styleguide - strictest and most opinionated Python linter
```
