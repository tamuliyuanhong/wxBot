# -*- coding: utf-8 -*-

from setuptools import setup

version = 'v1.0.1'

setup(
    name = 'wxbot',
    version = version,
    packages = ['wxbot', 'plugins'],
    entry_points = {
        'console_scripts': [
            'wxbot = qqbot:RunBot',
            'wx = wxbot:QTerm'
        ]
    },
    install_requires = ['requests', 'certifi', 'apscheduler'],
    description = "WXBot: A conversation robot base on Tencent's Webweixin",
    author = 'cfn' ,
    author_email = 'cfn@leapy.cn',
    url = 'https://github.com/ileapy/wxbot',
    download_url = 'https://github.com/ileapy/wxbot/archive/%s.tar.gz' % version,
    keywords = ['WXBot', 'conversation robot', 'tencent', 'weixin',
                'web', 'network', 'python', 'http'],
    classifiers = [],
)