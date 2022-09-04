#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""EX021: Faça um programa em Python que abra e reproduza
o audio de um arquivo MP3.  """
print('\n{:=^30}'.format('Exercicio:021'))
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
