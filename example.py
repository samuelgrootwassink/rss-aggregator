import time
from feed_parsing_lib import FeedAggregator, FileHandler


Agg = FeedAggregator()
feed_amount = len(Agg.feed_list)
start = time.time()
entries = Agg.popular_entries(entry_treshold=.5)
end = time.time()
for entry in entries:
    print(entry.title + ':')
    print(entry.summary)
    print('\n')
    
print(f"The time of execution of the sorting/filtering algorithm for a total of {feed_amount} feeds: {(end-start) * 10**3} ms")