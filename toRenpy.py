# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
import sys
import re
import zhon
#import replace
from zhon import hanzi

# replace all english names with chinese names
indir = '/Users/linqi/Projects/game/test_s.txt'
outdir = '/Users/linqi/Projects/game/test_test.txt'

# 由于中英文混杂的分句问题结局，不再需要replace
#replace.replace('Pete', '培特', indir, outdir)
#replace.replace('Lily', '莉莉', indir, outdir)
#replace.replace('Anna', '安娜', indir, outdir)

#f = open(outdir, 'rU')
#source = f.read().decode('utf-8')

# customize zhon.hanzi.sentence pattern, to match a sentence contains english words, chinese words and more than one chinese stops.

sentence_customize = u'[\u0041-\u005a\u0061-\u007a]*[\u3007\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\u2f00-\u2fd5\u2e80-\u2ef3\uff02\uff03\uff04\uff05\uff06\uff07\uff08\uff09\uff0a\uff0b\uff0c\uff0d\uff0f\uff1a\uff1b\uff1c\uff1d\uff1e\uff20\uff3b\uff3c\uff3d\uff3e\uff3f\uff40\uff5b\uff5c\uff5d\uff5e\uff5f\uff60\uff62\uff63\uff64\u3000\u3001\u3003\u300b\u300c\u300d\u300e\u300f\u3010\u3011\u3014\u3015\u3016\u3017\u3018\u3019\u301a\u301b\u301c\u301d\u301e\u301f\u3030\u303e\u303f\u2013\u2014\u2018\u2019\u201b\u201c\u201d\u201e\u201f\u2026\u2027\ufe4f]*[\uff01\uff1f\uff61\u3002\u2026\u002e]+'

# test if a sentence contains english characters
fn = open(indir, 'rU')
source = fn.read().decode('utf-8')

talks = re.findall(sentence_customize, source)

for talk in talks:
	print talk.encode('utf-8')

fn.close()
f.close()

"""
测试结果：
Lins-MacBook-Pro:game linqi$ python temp.py
女：你在哪里，快出来啊？
！
不行，绝对不能出去，这个女人，她已经疯了。
女：老老实实出来好不好？
电话，赶快，可恶，这里没有信号！
怎么办，怎么办，出去的话绝对会死的，这个女人已经疯了！
女：培特，别躲了，你逃不掉的。
噢噢噢！
这里有一格信号！
女声：培特，别躲了，你为什么总是要从我的身边逃走呢？
自己做的事情就要自己负责，不是么。
可恶！
！
！
如果当初……如果当初没有被她发现的话，就不会变成现在这样了。
如果，时间能够重来一次就好了！

问题：
1. 如何把多余的“！”等去掉；√
2. 把人名前缀（如“女：”）等替换掉；
3. 遇到关于CG的指示，替换成cg script；
4. 将全部对话做成renpy script格式；
5. 解决句中中英文混杂的分句问题；√

"""