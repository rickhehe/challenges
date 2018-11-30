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

#get the avg of a list of numbers, i.e. imdb_score
def avg(lst):
    return sum(lst)/len(lst)

#Gourp by director_name, take the mean of imdb_score.
def get_score(director_movies):
    return [(director, avg([movie[2] for movie in movies])) for director, movies in director_movies.items()]

def desc(sth):
    sd = sorted(sth, key = itemgetter(1), reverse = True)
    return [(k, round(v, 1)) for (k, v) in sd[:20]]
    
def movies(name):
    movies = sorted(data[name], key = itemgetter(2), reverse = True)
    return movies

data = data_cleanse('..\movie_metadata.csv')
scores = get_score(data)
sorted_scores_20 = desc(scores)

for i in sorted_scores_20:
    print(i[0], i[1])

    for movie in movies(i[0]):
        print(movie[0], movie[1], movie[2])
    
    print()
