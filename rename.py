import re
import sys
from os import listdir, rename
from os.path import isfile, join

# this script removes all japanese characters from filenames in
# your given directory, given that there are more than
# "minimum_english_chars" english characters in the filename (default 10)
# i.e. ベタベタされたことある A girl from my Japanese cram school
# did this behind my back _ easy Japanese storytime.mp3 
# gets renamed to A girl from my Japanese cram school 
# did this behind my back _ easy Japanese storytime.mp3
#
# however, 竹とんぼ知ってるÎõどんどんとだんだんはÎõ.mp3
# does not get renamed as it doesn't have enough english characters

directory_path = '.' # put a relative path to the directory with your
                     # files here. The default is '.', which
                     # means the same directory as the script

extensions = ['mp3'] # add all extensions you want to rename here

minimum_english_chars = 10

def check_filename(filename):
    return (any(ext in filename for ext in extensions)
           and isfile(join(directory_path, filename)))

file_names = list(filter(check_filename, listdir(directory_path)))

new_file_names = []

# magic regex to check for japanese characters in string
# found it here: https://gist.github.com/ryanmcgrath/982242
# don't change unless you know what you are doing
regex = '[\u3000-\u303F]|[\u3040-\u309F]|[\u30A0-\u30FF]|[\uFF00-\uFFEF]|[\u4E00-\u9FAF]|[\u2605-\u2606]|[\u2190-\u2195]|\u203B'

count = 0
for file_name in file_names:
    new_file_name = file_name
    subbed = re.sub(regex, '', new_file_name)
    if len(subbed) >= 10:
        new_file_name = subbed
        count += 1
    new_file_names.append(new_file_name)

for i, file_name in enumerate(file_names):
    new_file_name = new_file_names[i]
    rename(file_name, new_file_name)
    print(f'renamed {file_name} to {new_file_name}')

print(f'renamed {count} files')
