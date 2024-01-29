# Yesterday's News
I like to keep up to date with what’s trending on Hacker News, but not *too* up to date. This is a little script that makes a [JSON feed](https://www.jsonfeed.org/) with yesterday's top thirty stories, complete with links to the original item *and* to the comments section. I read it in [NetNewsWire](https://netnewswire.com/).

# Dependencies
I use `pipenv` to install and manage Python libraries. In this case, it will install:

- [Requests](https://requests.readthedocs.io/en/latest/)
- [BeautifulSoup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Usage
## Installation
```sh
git clone https://github.com/samnunn/hackernews-scraper
cd hackernews-scraper
pipenv install
```

## Setup
You need to provide the script with a URL where you intend to host your feed on the Web and an output path where you intend to save the feed on your machine. Do this by setting environment variables, which Pipenv automatically loads from a `.env`. You can create one with your own details like so:

```sh
echo HN_FEED_BASEURL="https://example.com/feeds" >.env  # where you plan to serve the feed from, no trailing slash
echo HN_FEED_BASEPATH="/var/www/feeds/" >> .env         # where on this machine you intend to save the .json file
```

## Running It
```sh
~/.pyenv/shims/pipenv run python hackernews-scraper.py
```

You can trigger this however you like. If your server is a Mac, consider using a simple Keyboard Maestro macro with the [do shell script](https://wiki.keyboardmaestro.com/action/Execute_a_Shell_Script) action on a [time of day trigger](https://wiki.keyboardmaestro.com/trigger/Time_of_Day). For the brave, there's always [launchd](https://www.launchd.info/).