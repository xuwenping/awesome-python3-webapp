#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import asyncio
import sys
from models import User, Blog
import os

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='123456', db='awesome')

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    await u.save()
    await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
