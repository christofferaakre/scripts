# this script will take a .json term bank (frequency list) and
# use the frequency ratings to add stars to each term
# It should work by just placing it in the same directory as the
# termbank file and running it, but if you run into problems let me know
# at https://github.com/christofferaakre/scripts or email me at
# christoffer.corfield@gmail.com
# I will be happy to help!

star = '★'

def freq_to_stars(freq: int) -> str:
    if 1 <= freq <= 1500:
        return 5 * star
    elif 1501 <= freq <= 5000:
        return 4 * star
    elif 5001 <= freq <= 15000:
        return 3 * star
    elif 15001 <= freq <= 30000:
        return 2 * star
    elif 30001 <= freq <= 60000:
        return 1 * star
    elif 60001 <= freq:
        return 0 * star
    
    else:
        raise ValueError('freq must be a positive integer')

# file that has the frequency list in it
# not the index.json file
input_file = 'term_meta_bank_1.json'

# name of file that the script will create
output_file = 'term_meta_bank_1.json_stars'

with open(input_file, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

lines_with_stars = []
for line in lines[1:-1]:
    trim = ['[', ']']
    trimmed = line
    for char in trim:
        trimmed = trimmed.replace(char, '')

    word, freq_token, freq, linebreak = trimmed.split(',')
    stars = freq_to_stars(int(freq))
    with_stars = f'[{word},{freq_token},"{stars} ({freq})"],\n'
    lines_with_stars.append(with_stars)

with open(output_file, 'w', encoding='utf-8') as file:
    file.write('[\n')
    for line in lines_with_stars:
        file.write(line)
    file.write(']')
