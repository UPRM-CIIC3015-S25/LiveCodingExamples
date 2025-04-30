# UPRM CIIC 3015 Spring 2025
# Lecture 8: Files and Exceptions

# Live Coding Example 8_2


# Copy a File
def copy_file(source, destination):
    pass

# copy_file('song_db.txt', 'song_db.copy')


# Concatenate two files
def concat_files(source1, source2, destination):
    pass

# concat_files('song_db.txt', 'song_db.copy', 'song_db_double.txt')


# Replace all occurrences of a word in a file
def replace_word_in_file(filename, word, replacement):
    with open(filename, 'r') as file:
        lines = file.readlines()
    replaced_lines = []
    for line in lines:
        new_line = line.replace(word, replacement)
        replaced_lines.append(new_line)
    with open(filename, 'w') as file:
        file.writelines(replaced_lines)

replace_word_in_file('song_db.copy', 'Bienve', 'Bienvenido')



# Load comma-separated DB into dictionary DB
def load_song_db_into_uid_dict(filename):
    pass


