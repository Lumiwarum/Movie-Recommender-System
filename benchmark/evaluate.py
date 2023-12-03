import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

overall_stats = pd.read_csv('../data/ml-100k/u.info', header=None)


column_names1 = ['user id','movie id','rating','timestamp']
dataset = pd.read_csv('../data/ml-100k/u.data', sep='\t',header=None,names=column_names1)

d = 'movie id | movie title | release date | video release date | IMDb URL | unknown | Action | Adventure | Animation | Children | Comedy | Crime | Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi | Thriller | War | Western'
column_names2 = d.split(' | ')

items_dataset = pd.read_csv('../data/ml-100k/u.item', sep='|',header=None,names=column_names2,encoding='latin-1')
movie_dataset = items_dataset[['movie id','movie title']]
merged_dataset = pd.merge(dataset, movie_dataset, how='inner', on='movie id')

refined_dataset = merged_dataset.groupby(by=['user id','movie title'], as_index=False).agg({"rating":"mean"})

#list of all users
unique_users = refined_dataset['user id'].unique()
#creating a list of all movie names in it
unique_movies = refined_dataset['movie title'].unique()

users_list = refined_dataset['user id'].tolist()
movie_list = refined_dataset['movie title'].tolist()

ratings_list = refined_dataset['rating'].tolist()
movies_dict = {unique_movies[i] : i for i in range(len(unique_movies))}

## creating a utility matrix for the available data

## Creating an empty array with (number of rows = number of movies) and (number of columns = number of users) rows as movies, columns as users

utility_matrix = np.asarray([[np.nan for j in range(len(unique_users))] for i in range(len(unique_movies))])

for i in range(len(ratings_list)):

  ## ith entry in users list and subtract 1 to get the index, we do the same for movies but we already defined a dictionary to get the index.
  utility_matrix[movies_dict[movie_list[i]]][users_list[i]-1] = ratings_list[i]

mask = np.isnan(utility_matrix)
masked_arr = np.ma.masked_array(utility_matrix, mask)
temp_mask = masked_arr.T
rating_means = np.mean(temp_mask, axis=0)

filled_matrix = temp_mask.filled(rating_means)
filled_matrix = filled_matrix.T
filled_matrix = filled_matrix - rating_means.data[:,np.newaxis]
filled_matrix = filled_matrix.T / np.sqrt(len(movies_dict)-1)

U, S, V = np.linalg.svd(filled_matrix)

case_insensitive_movies_list = [i.lower() for i in unique_movies]

#Function to calculate the cosine similarity (sorting by most similar and returning the top N)
def top_cosine_similarity(data, movie_id, top_n=10):
  index = movie_id
  movie_row = data[index, :]
  magnitude = np.sqrt(np.einsum('ij, ij -> i', data, data))
  magnitude = np.array([mag if mag != 0 else 0.1 for mag in magnitude])
  similarity = np.dot(movie_row, data.T) / (magnitude[index] * magnitude)
  sort_indexes = np.argsort(-similarity)
  return sort_indexes[:top_n+1]
  
#k-principal components to represent movies, movie_id to find recommendations, top_n print n results
def get_similar_movies(movie_name,top_n,k = 50):
  # k = 50
  # movie_id = 1
  # top_n = 10

  sliced = V.T[:, :k] # representative data
  movie_id = movies_dict[movie_name]
  indexes = top_cosine_similarity(sliced, movie_id, top_n)
  print(" ")
  print("Top",top_n,"movies which are very much similar to the Movie-",movie_name, "are: ")
  print(" ")
  for i in indexes[1:]:
    print(unique_movies[i])
    
    
# function which takes input and returns suggestions for the user

def get_possible_movies(movie):

    temp = ''
    possible_movies = case_insensitive_movies_list.copy()
    for i in movie :
      out = []
      temp += i
      for j in possible_movies:
        if temp in j:
          out.append(j)
      if len(out) == 0:
          return possible_movies
      out.sort()
      possible_movies = out.copy()

    return possible_movies
    
class invalid(Exception):
    pass

def recommender():

    try:

      movie_name = input("Enter the Movie name: ")
      movie_name_lower = movie_name.lower()
      if movie_name_lower not in case_insensitive_movies_list :
        raise invalid
      else :
        # movies_list[case_insensitive_country_names.index(movie_name_lower)]
        num_recom = int(input("Enter Number of movie recommendations needed: "))
        get_similar_movies(unique_movies[case_insensitive_movies_list.index(movie_name_lower)],num_recom)

    except invalid:

      possible_movies = get_possible_movies(movie_name_lower)

      if len(possible_movies) == len(unique_movies) :
        print("Movie name entered is does not exist in the list ")
      else :
        indices = [case_insensitive_movies_list.index(i) for i in possible_movies]
        print("Entered Movie name is not matching with any movie from the dataset . Please check the below suggestions :\n",[unique_movies[i] for i in indices])
        print("")
        recommender()
        
        
if __name__ == '__main__':
    recommender()
    
    
