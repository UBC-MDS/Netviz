import pandas as pd

out_dir = "../data/processed/"

df = pd.read_csv('../data/raw/netflix_titles.csv')
df = df.query('type == "Movie"').drop(columns=['type'])
df = df.dropna()
df['duration'] = df['duration'].apply(lambda x: x.split(" ")[0]).astype(int)
df['release_year'] = df['release_year'].astype(int)

genre_df = df.copy()
genre_df['genre'] = genre_df['listed_in'].apply(lambda x: x.split(', '))
genre_df = genre_df.explode('genre')
genre_df = genre_df.drop(columns='listed_in')
genre_df.to_csv(out_dir+"netflix_movies_genres.csv")

URL = "https://raw.githubusercontent.com/KoGor/Map-Icons-Generator/master/data/world-110m-country-names.tsv"
country_id_df = pd.read_csv(URL, sep='\t')
country_id_df.to_csv(out_dir+"country_ids.csv")
