import redis

def get_words_from_dict():

  with open('dictionaries/demo.txt') as word_file:
    valid_words = set(word_file.read().split())

  return valid_words

def cache_words(words):

  r = redis.Redis(host='localhost', port=6379, db=0)

  r.flushdb()

  for key in words:
    r.set(key, 0)

if __name__ == '__main__':
  english_words = get_words_from_dict()
  cache_words(english_words)