#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('http://news.dbanotes.net')
print(r.text.decode('uft-8'))