#!/usr/bin/env python3
# -*- coding:utf-8 -*-

moudle_name = 'handlers.py'
n = moudle_name.rfind('.')
print(n)
mod = getattr(__import__(moudle_name[:n], globals(), locals()))
#for attr in dir(mod):
#    print(attr)

