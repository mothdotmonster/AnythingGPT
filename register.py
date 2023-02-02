#!/usr/bin/env python3

from mastodon import Mastodon
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

Mastodon.create_app(
    'AnythingGPT',
    api_base_url = config['Account']['BaseURL'],
    to_file = 'pytooter_clientcred.secret'
)

mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
mastodon.log_in(
    config['Account']['Email'],
    config['Account']['Password'],
    to_file = 'pytooter_usercred.secret'
)