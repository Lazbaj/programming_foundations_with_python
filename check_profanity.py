import urllib

def read_text(text_file):
    quotes = open(text_file)
    contents = quotes.read()
    print contents
    quotes.close()
    return contents

def check_profanity(text):
    webpage = urllib.urlopen('http://www.wdylike.appspot.com/?q='+text)
    output = webpage.read()
    webpage.close()
    return output

print check_profanity(read_text('movie_quotes.txt'))

