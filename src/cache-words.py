import redis
import math
from pprint import pprint

def get_words_from_dict():

  with open('../dictionaries/words.txt') as word_file:
    valid_words = list(word_file.read().split())

  return valid_words # 466550 words

def cache_words(words):

  r = redis.Redis(host='localhost', port=6379, db=0)

  r.flushdb()

  word_count = len(words)
  chunk_size = 1000
  chunks = math.ceil(word_count / chunk_size)

  for i in range(chunks):
    chunk_start = i * chunk_size
    chunk = words[chunk_start:chunk_start + chunk_size]
    r.mset({word: 0 for word in chunk})

if __name__ == '__main__':
  english_words = get_words_from_dict()
  cache_words(english_words)