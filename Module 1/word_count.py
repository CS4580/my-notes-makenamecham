""" Read file from web and do analysis of data
"""

from urllib.request import urlopen

def count_words_from_web_file(url_address):
    
    words = 0
    words = 0
    # TODO: Read file from Web
    with urlopen(url_address) as data:
        for line in data:
            print(line, type(line))
            line = line.decode('utf-8') # converts bytes to string
            print(line, type(line))
            line_words = line.split()
            for word in line_words:
                #TODO: Count number of words
                words+= 1
    return words


def main():
    """Driven Function
    """

    # TODO: Read file from Web
    file_address = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    total_words = count_words_from_web_file(file_address)
    print(f'There area a total of {total_words} words in the file')

    #TODO: Count number of words

    if __name__ == '__main__':
        main()