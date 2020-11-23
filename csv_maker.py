import csv 

def csv_creator(emoji_file, output="emojis.csv"):
    '''Makes a legit csv file out of a given file'''
    emoji_list = open(emoji_file)
    emoji_list = emoji_list.readlines() 
    emoji_list = emoji_list[0]

    emoji_list_functional = [] 

    for emoji_char in emoji_list:
        emoji_list_functional.append(emoji_char)

    with open(output, mode='w') as output_file:
        output_writer = csv.writer(output_file, delimiter=',', quotechar='"')
        output_writer.writerow(emoji_list_functional) 


csv_creator("emojis_strong.txt")
