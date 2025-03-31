# UPRM CIIC 3015 Spring 2025
# Lecture 6: Dictionaries and Sets

# Live Coding Example 5
# Combining Dictionaries and Sets


songs_db_list = [
  [1, 'Circles', 'Post Malone', 2019, 'Psychedelic Pop'],
  [2, 'Ransom', 'Lil Tecca', 2019, 'Hip Hop/Rap'],
  [3, 'BOP', 'DaBaby', 2019, 'Hip Hop/Rap'],
  [4, 'Truth Hurts', 'Lizzo', 2020, 'Pop'],
  [5, '223\'s (feat. 9lokknine)', 'YNW Melly', 2021, 'Hip Hop/Rap'],
]
songs_columns_names = ["UID", "Title", "Author", "Year", "Genre"]

# Returns a dictionary for a single row mapping column name to value
def build_row_dict(row, column_names):
    row_dict = {}



    return row_dict

print(build_row_dict(songs_db_list[0], songs_columns_names))

# Returns a dictionary for entire db mapping unique id to row dictionary
def build_db_dict(column_names, uid_column_name, db_list):
    db_dict = {}




    return db_dict


print(build_db_dict(songs_columns_names, "UID", songs_db_list))


# Returns a dictionary mapping each distinct column value for the given column name
# to a set of unique ids of rows with than value in that column
# This is what in database systems is called an INDEX
def build_db_index(db, column_name, uid_name):
    index = {}





    return index

songs_db_dict = build_db_dict(songs_columns_names, "UID", songs_db_list)
songs_year_index = build_db_index(songs_db_dict, "Year", "UID")

# Returns a set with all song titles in the given year
def song_titles_by_year(db_dict, year_index, year):
    result = set()




    return result


print(f"Song titles in 2019 {song_titles_by_year(songs_db_dict, songs_year_index, 2019)}")
print(f"Song titles in 2018 {song_titles_by_year(songs_db_dict, songs_year_index, 2018)}")


print("Done")