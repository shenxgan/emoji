#!/usr/bin/env python
# encoding: utf-8

import urllib2
import re
import json


class GetEmoji():
    def __init__(self, url):
        self.url = url

    def get_page_data(self):
        r = urllib2.urlopen(self.url)
        data = r.read()
        return data

    def get_emoji_data(self):
        emoji = {}
        data = self.get_page_data()
        data = data.split('\n')
        for line in data:
            rs = r'<span id="e_(\d+)" class="emoji" data-src="graphics/emojis/\S+.png"></span>:<span.*>(\S+)</span>'
            res = re.findall(rs, line)
            if res:
                id, name = res[0]
                id = int(id)
                name = name.join([':', ':'])
                xvalue = -(id - 1) * 32 - 5
                emoji[name] = xvalue
        return emoji

    def write_to_file(self, emoji):
        with open('emoji.py', 'w') as f:
            f.write(emoji)

    def run(self):
        emoji = self.get_emoji_data()
        emoji_str = 'emoji = %s' % json.dumps(emoji, indent=4, separators=(',', ': '))
        self.write_to_file(emoji_str)
        self.test()

    def test(self):
        from emoji import emoji
        print emoji[':bowtie:']     # -5
        print emoji[':smile:']      # -37
        print emoji[':laughing:']   # -69


if __name__ == '__main__':
    url = 'http://www.emoji-cheat-sheet.com/'
    getemoji = GetEmoji(url)
    getemoji.run()
