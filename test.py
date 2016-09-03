#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

# async def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = await connect
#     print('[READER]',reader)
#     print('[WRITER]', writer)
#     header = 'GET / HTTP/1.0\r\nHOST: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     await writer.drain()
#     while True:
#         line = await reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        for k, v in attrs.items():
            print(type(v))
            print(k, v)

        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    id = 5

# L = MyList()
# L.add(1)
# L.add(2)
# print(L)
import logging
logging.basicConfig(level=logging.INFO)

logging.debug('debug xuwenping message')
logging.info('info xuwenping message')
logging.warn('warn xuwenping message')
logging.error('error xuwenping message')
logging.critical('critical xuwenping message')