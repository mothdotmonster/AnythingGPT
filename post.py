#!/usr/bin/env python3

from mastodon import Mastodon
import csv, random, configparser

config = configparser.ConfigParser()
config.read('config.ini')

mastodon = Mastodon(access_token = 'pytooter_usercred.secret')

numWords = random.randint(int(config['Bot']['PostLength']) - int(config['Bot']['LengthFuzz']) , int(config['Bot']['PostLength']) + int(config['Bot']['LengthFuzz'])) # decide how many words to post

post = [] # initialize empty list

with open(config['Bot']['Words'], newline='') as csvfile:
  words = list(csv.DictReader(csvfile)) # turn csv file into a nice list of dicts
  for i in range(numWords):
    word = words[random.randint(0, len(words) - 1)]
    if word['numRepeats'] != None: # check if we're supposed to repeat on this word
      post.append(word['word'] + ( word['word'][int(word['repeatAt'])-1:] * random.randint(1,int(word['numRepeats']))) ) # if yes, repeat as requested
    else:
      post.append(word['word']) # if no, just add the word

if config['Bot'].getboolean('DryRun'):
  print(' '.join(post))
else:
  mastodon.toot(' '.join(post))
