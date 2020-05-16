# -*- coding: utf-8 -*-

name = 'ninja'

version = '1.10.0'

authors = [
    'philip.luk'
]

requires = [
]

build_requires = [
]

variants = [
    ['platform-windows'],
    ['platform-linux'],
]

def commands():
    env.PATH.append('{root}/bin')

