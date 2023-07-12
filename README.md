# AnythingGPT
A fediverse bot for posting about anything (randomly)

## Usage
Run ```login.py```, and give it your bot's account info, so it can generate the token files. Once you've ran that, you can run ```post.py``` each time you want the bot to post, using something like cron.

To change the word list, simply edit ```words.csv``` to have the words you want. If you want to repeat the last letter(s) of some words a random amount of time, the format is as follows:  
```word, character to repeat after, max number of repeats```

You should enable the ```DryRun``` option if you want to test your word list. Make sure to disable it to start actually posting!

You can change the amount of words per post by changing the ```PostLength``` option. A random amount of fuzzing is applied to the post length, which can be changed in range via the ```LengthFuzz``` option.