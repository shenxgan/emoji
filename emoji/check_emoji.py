#!/usr/bin/env python
# encoding: utf-8


import re
from emoji import emoji


def check_emoji(text):
    text = text.replace('::', ': :')
    rs = '(\:\S+\:)'
    emoji_list = re.findall(rs, text)
    for name in emoji_list:
        position = emoji.get(name)
        if position:
            replace = '<span class="emoji" style="background-position: %spx 0;"></span>' % str(position)
            text = text.replace(name, replace)
    text = text.replace(': :', '::')
    return text


if __name__ == '__main__':
    text = ':smile:'
    text = ':smile: :+1:'
    text = ':smile::+1:'
    text = ':smile::+1::test: :-1: :-1 : '
    text = check_emoji(text)
    print text
