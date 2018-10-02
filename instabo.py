#!/usr/bin/env python
#!/usr/bin/python

# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

from firebase import firebase

firebase = firebase.FirebaseApplication('https://instagrambot-49b72.firebaseio.com/', None)

reseteo = firebase.get('/user2', 'reseteo')
       
nombre = firebase.get('/user2', 'nombre')
passes = firebase.get('/user2', 'password')
hashs = firebase.get('/user2', 'Hashs')
locs = firebase.get('/user2', 'Locs')
comment = firebase.get('/user2', 'Comment')
hashssplit = hashs.split(',');

print nombre,passes,hashs,locs,comment,reseteo

bot = InstaBot(
    login=nombre,
    password=passes,
    like_per_day=1500,
    comments_per_day=500,
    tag_list=[hashssplit[0],hashssplit[1],hashssplit[2],hashssplit[3],hashssplit[4],hashssplit[5],hashssplit[6],hashssplit[7],hashssplit[8],hashssplit[9],
              hashssplit[10],hashssplit[11],hashssplit[12],hashssplit[13],hashssplit[14],hashssplit[15],hashssplit[16],hashssplit[17],hashssplit[18],hashssplit[19],
              hashssplit[20],hashssplit[21],hashssplit[22],hashssplit[23],hashssplit[24],hashssplit[25]],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=300,
    follow_time=1 * 60,
    unfollow_per_day=300,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[["Hola! que buen perfil, te ayudamos a posicionarte en el mundo digital a tu alcance (Redes Sociales, Aplicaciones Moviles, Pagina WEB, entre otros) Contactanos WhatsApp 316 2773185",
                   "Hola! que buen perfil, te ayudamos a posicionarte en el mundo digital a tu alcance (Redes Sociales, Aplicaciones Moviles, Pagina WEB, entre otros) Contactanos WhatsApp 316 2773185",
                   "Hola! que buen perfil, te ayudamos a posicionarte en el mundo digital a tu alcance (Redes Sociales, Aplicaciones Moviles, Pagina WEB, entre otros) Contactanos WhatsApp 316 2773185"],
                  [".", "..", "...", "!", "!!", "!!!"]],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

   
    if mode == 0:
        bot.new_auto_mod()
        print reseteo
        
    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
