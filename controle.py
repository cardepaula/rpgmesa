#!/usr/bin/python3
# -*- coding: utf-8 -*-
from emoji import emojize
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from controles.dados import DadoControle

 
class Controle(object):
    def __init__(self, bot):
        self.bot = bot
        self.chat_id = any
        self.command = any
        self.objeto = any

    def comando(self, msg):
        self.chat_id = msg['chat']['id']
        self.command = msg['text'].lower()
        dados = self.command.split()
        comando = self.command.split()[0]
        dados = dados[1:]
        dados.insert(0, msg['from']['first_name'] + " " + msg['from']["last_name"])
        if comando in ["/d", "/dice","/dado","/d20","/roll"]:
            self.objeto = DadoControle()
            ret = self.objeto.rolarDado(dados)
            self.retorna(ret)
    def retorna(self, ret):
        self.bot.sendMessage(self.chat_id, emojize("%s" %ret, use_aliases=True))
    def teclado(self,dados):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                       InlineKeyboardButton(text='Personagem', callback_data="/ajuda"),
                       InlineKeyboardButton(text='Mestre', callback_data="/ajudam"),
                    ]])
        self.bot.sendMessage(self.chat_id, 
                        text="Ajuda:", 
                        reply_markup=keyboard)