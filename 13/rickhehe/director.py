import csv
from operator import itemgetter
from collections import defaultdict


#drop entries with title_year before 1960 or left blank; create dictioanary with director_name as keys, while their movies as nest lists.  Then keep directors with at least 4 movies.

def data_cleanse(file):
    d = defaultdict(list)
    with open(file, 'r', newline = '') as movies:
        reader = csv.DictReader(movies)
        for row in reader:
            if row['title_year'] !='' and int(row['title_year']) >= 1960:
                d[row['director_name']].append([row['title_year'], row['movie_title'], float(row['imdb_score'])])
    return {key: value for key, value in d.items() if len(value) >= 4}

def avg(lst):
    return sum(lst)/len(lst)


def get_score(director_movies):
    return [(director, avg([movie[2] for movie in movies])) for director, movies in director_movies.items()]

def desc(sth):
    sd = sorted(sth, key = itemgetter(1), reverse = True)
    return [(k, round(v, 1)) for (k, v) in sd[:20]]
    
def movies(name):
    pass

data = data_cleanse('..\movie_metadata.csv')
scores = get_score(data)
sorted_scores_20 = desc(scores)
