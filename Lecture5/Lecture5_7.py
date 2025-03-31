# UPRM CIIC 3015 Spring 2025
# Lecture 5: Strings and Lists

# Live Coding Example 7
# Multi-dimensional lists


songs = [
  ['Circles', 'Post Malone', 2019, 'Psychedelic Pop'],
  ['Ransom', 'Lil Tecca', 2019, 'Hip Hop/Rap'],
  ['BOP', 'DaBaby', 2019, 'Hip Hop/Rap'],
  ['Truth Hurts', 'Lizzo', 2019, 'Pop'],
  ['223\'s (feat. 9lokknine)', 'YNW Melly', 2019, 'Hip Hop/Rap'],
]

# Retrieve the titles and artists of all 2019 songs in the Hip Hop/Rap category
def songs_by_year_genre(db, year, genre):
  result = []
  for song in db:
    if year == song[2] and genre == song[3]:
      result.extend([song[0], song[1]])
  return result


print(songs_by_year_genre(songs, 2019, 'Hip Hop/Rap'))

print("Done testing")