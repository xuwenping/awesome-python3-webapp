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

#class ListMetaclass(type):
#    def __new__(cls, name, bases, attrs):
#        for k, v in attrs.items():
#            print(type(v))
#            print(k, v)
#
#        attrs['add'] = lambda self, value: self.append(value)
#        return type.__new__(cls, name, bases, attrs)
#
#class MyList(list, metaclass=ListMetaclass):
#    id = 5

# L = MyList()
# L.add(1)
# L.add(2)
# print(L)
#import logging
#logging.basicConfig(level=logging.INFO)
#
#logging.debug('debug xuwenping message')
#logging.info('info xuwenping message')
#logging.warn('warn xuwenping message')
#logging.error('error xuwenping message')
#logging.critical('critical xuwenping message')

#import functools
#def get(path):
#    '''
#    Define decorator @get('/path')
#    '''
#    def decorator(func):
#        @functools.wraps(func)
#        def wrapper(*args, **kw):
#            print('path [%s]' % path)
#            return func(*args, **kw)
#        wrapper.__method__ = 'GET'
#        wrapper.__route__ = path
#        return wrapper
#    return decorator
#
#@get('/path')
#def test():
#    print('test')
#
#
#
##print(test.__method__)
#def test(module_name):
#    mod = __import__(module_name, globals(), locals())
#    print(type(mod))
#    for attr in dir(mod):
#        print(attr)

#test('testORM')
#staticimport os
#from jinja2 import Environment, FileSystemLoader
#import logging
#
#def init_jinja2(app, **kw):
#    options = dict(
#        autoescape = kw.get('autoescape', True),
#        block_start_string = kw.get('block_start_string', '{%'),
#        block_end_string = kw.get('block_end_string', '%}'),
#        variable_start_string = kw.get('variable_start_string', '{{'),
#        variable_end_string = kw.get('variable_end_string', '}}'),
#        auto_reload = kw.get('auto_reload', True)
#    )
#
#    path = kw.get('path', None)
#    if path is None:
#        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
#    logging.info('set jinja2 template path: %s' % path)
#    env = Environment(loader=FileSystemLoader(path), **options)
#    print(env)
#    filters = kw.get('filters', None)
#    if filters is not None:
#        for name, f in filters.items():
#            env.filters[name] = f
#    app['__templating__'] = env

#r = {'gdsfsd': 1, 'reer':2}
#print(**r)


