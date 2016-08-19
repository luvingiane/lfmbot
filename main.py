#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from keys import (
    token,
    apikey,
    apisecret,
    lastfmu,
    lastfmp)
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

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Ciao, questo è un bot che ti invia lo scrobbling attuale. (è la versione 0.1,non c'è un cazzo in pratica :S)")

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Bot scritto da mattia")

@bot.message_handler(commands=['gaipa'])
def send_welcome(message):
    bot.reply_to(message, "PHP MERDAAAAAAAAA")

@bot.message_handler(commands=['traccia'])
def send_welcome(message):
    bot.reply_to(message, print_track)


bot.polling()
