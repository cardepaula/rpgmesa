#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Any

from controles.dados import DadoControle
from controles.zoeira import ZoeiraControle


class Controle:
    command = ...  # type: str

    def __init__(self, msg):
        self.objeto = ZoeiraControle()
        self.msg = msg
        self.chat_id = msg['chat']['id']
        self.command = msg['text'].lower()

    def comando(self):
        dados = self.command.split()[1:]
        comando = self.command.split()[0]
        dados.insert(0, self.msg['from']['first_name'] +
                     " " + self.msg['from']["last_name"])
############################
        if comando in ["/d", "/dice", "/dado", "/d20", "/roll", "/r"]:
            self.objeto = DadoControle()
            try:
                ret = self.objeto.rolarDado(dados)
                self.retorna(ret)
            except:
                self.retorna(
                    'Erro de escrita, tente: 2d20+1.\n (quantidade: 2, dado: 20 faces, bonus: 1)')

        elif self.busca_comando(["jogo", "jogar", "cs", "rb6", "lolzim", "lol"]) :
            self.objeto = ZoeiraControle()
            return self.objeto.jogo()

        elif self.busca_comando(["teco", "jadson","big","owl","doug", "douglas", "bw",":owl:"]):
            self.objeto = ZoeiraControle()
            return self.objeto.teco()

    def busca_comando(self, palavras):
        for p in palavras:
            if p in self.command:
                return True
        return False

    def retorna(self, ret):
        return ret

