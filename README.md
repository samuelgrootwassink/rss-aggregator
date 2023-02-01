<h1> RSS Aggrgator</h1>
Small library with example in main.py that aggregates rss & atom feeds into into objects that can be further used to for other purposes. 

<hr>
<h2>Usage</h2>
You can add rss/atom feeds in the provided:

`files/rss_feeds.txt`

And any blacklisted words in:

`files/ignored_words.txt`

<hr>
Included are two methods that calculate the most used nouns:

`popular_words(news_orgs, amount)`

Which can then be used to filter articles that contain an amount of these previous prevoided popular words:

`popular_entries(news_orgs, filters, treshold)`

<hr>
Before use make sure you run Poetry to install all dependencies:

`poetry install && poetry run python3 main.py`
