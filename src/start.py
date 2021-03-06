from flask import Flask
from flask import request
import redis
import string

app = Flask(__name__)

def clean_word(word):
  return word.translate(str.maketrans('', '', string.punctuation))

@app.route('/')
def hello_world():

  r = redis.Redis(host='localhost', port=6379, db=0)

  my_text = request.args.get('my_text')

  if my_text is None:
    return "Please, provide a query param 'my_text'"

    text_list = my_text.split()

  cleared = []

  for i, word in enumerate(text_list):
    word_ = clean_word(word)
    cleared.append(word_)

  hits = r.mget(cleared)

  for i, word in enumerate(text_list):
    word_ = clean_word(word)
    hit = hits[i]
    if hit is not None:
      text_list[i] = ''.join(['*' for letter in word])

  return ' '.join(text_list))