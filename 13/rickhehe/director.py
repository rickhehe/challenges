import csv
from collections import defaultdict, Counter

d = defaultdict(list)

with open('..\movie_metadata.csv', 'r', newline = '') as movies:
    reader = csv.DictReader(movies)
    for row in reader:
        if row['title_year'] !='' and int(row['title_year']) >= 1960:
            d[row['director_name']].append([row['title_year'], row['movie_title'], row['imdb_score']])

d = {key: value for key, value in d.items() if len(value) >= 4}
print(d)
