#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from keys import token
from keys import apikey
from keys import apisecret
from keys import lastfmu
from keys import lastfmp
import telebot
import argparse
import pylast
import sys

from mylast import (
    lastfm_network,
    lastfm_username,
    print_it,
    print_track,
    split_artist_track,
    TRACK_SEPARATOR,
    unicode_track_and_timestamp)

bot = telebot.TeleBot(token)
API_KEY = apikey
API_SECRET = apisecret

username = lastfmu
password_hash = pylast.md5(lastfmp)

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

#code

print ("porcoddio");

bot.polling()
