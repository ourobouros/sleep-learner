from flask import render_template
from flask import Blueprint
from flask import jsonify
from flask import request

import csv
import json

from util.database import get_db_connection

quiz_app = Blueprint('quiz', __name__)


@quiz_app.route('/quiz/words')
def get_words():
  db = get_db_connection()

  wordlist = []
  for _, word, defin,know in db.execute('SELECT * FROM dictionary_entry'):
    wordlist.append({
      'word': word,
      'defin': defin,
      'know': know,
    })

  return jsonify(results=wordlist)

@quiz_app.route('/quiz/reply',methods=['GET', 'POST'])
def record():
    data = request.data
    #data = '{"first_name": "Guido", "last_name":"Rossum"}'
    print(data)
    data = json.loads(data,'utf-8')
    #print(data['know'])
    return jsonify(**data)

    #update value in database
    