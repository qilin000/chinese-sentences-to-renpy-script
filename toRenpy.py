# -*- coding: utf-8 -*-
import sys
import re
#import zhon
#from zhon import hanzi

# set dir of source file and output file.
indir = '/Users/linqi/Projects/renpygame/test_s.txt'
outdir = '/Users/linqi/Projects/renpygame/test_test.txt'

# customize zhon.hanzi.sentence pattern, to match a sentence contains english words, chinese words and more than one chinese stops.
# also match the no. of CG, eg. Cg00 
sentence_customize = u'[\u0041-\u005a\u0061-\u007a]*[\u3007\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\u2f00-\u2fd5\u2e80-\u2ef3\uff02\uff03\uff04\uff05\uff06\uff07\uff08\uff09\uff0a\uff0b\uff0c\uff0d\uff0f\uff1a\uff1b\uff1c\uff1d\uff1e\uff20\uff3b\uff3c\uff3d\uff3e\uff3f\uff40\uff5b\uff5c\uff5d\uff5e\uff5f\uff60\uff62\uff63\uff64\u3000\u3001\u3003\u300b\u300c\u300d\u300e\u300f\u3010\u3011\u3014\u3015\u3016\u3017\u3018\u3019\u301a\u301b\u301c\u301d\u301e\u301f\u3030\u303e\u303f\u2013\u2014\u2018\u2019\u201b\u201c\u201d\u201e\u201f\u2026\u2027\ufe4f]*[\uff01\uff1f\uff61\u3002\u2026\u002e]+|[Cc][Gg][01][0-9]'

# get a source file and an output file. decode chinese words.
infile = open(indir, 'rU')
source = infile.read().decode('utf-8')
outfile = open(outdir, 'w')

# filter chinese sentences out of the source file. talks is a list.
talks = re.findall(sentence_customize, source)

# render all conversations to renpy script format
# eg.    a "Welcome to the sample game!" 
# (four spaces + character code + one space + conversation inside double quotes)
# render all cg notes to renpy script format
# eg.    scene bg02
#        with dissolve
# (four spaces + background code and "with dissolve" on second line with same indentation)

# a list of names needs to be converted
name_tuples = [(u'女：', 'n'), (u'女声：', 'n'), (u'Lily：', 'l'), (u'服务生：', 'w'), (u'Anna：', 'a'), (u'警察：', 'p'), (u'警察A：', 'p_a'), (u'警察B：', 'p_b')]


def conversation(talk):
	for name in name_tuples:
		if(name[0] in talk):
			index = talks.index(talk)
			conversation = talk.split(u'\uff1a')
			talk_new = '    ' + name[1] + ' ' + r'"' + conversation[-1] + r'"'
			talks[index] = talk_new
			talks.insert(index+1, '\n')
	if(u'\uff1a' not in talk):
		index = talks.index(talk)
		talk_new = '    ' + r'"' + talk + r'"'
		talks[index] = talk_new
		talks.insert(index+1, '\n')		

for talk in talks:
	if(re.search(r'[Cc][Gg][01][0-9]', talk)):
		index = talks.index(talk)
		talk_new = '    ' + 'scene ' + talk.lower()
		talks[index] = talk_new
		with_dissolve = '    ' + 'with dissolve'
		talks.insert(index+1, with_dissolve)
		talks.insert(index+2, '\n')
	for name in name_tuples:
		if(name[0] in talk):
			index = talks.index(talk)
			conversation = talk.split(u'\uff1a')
			talk_new = '    ' + name[1] + ' ' + r'"' + conversation[-1] + r'"'
			talks[index] = talk_new
			talks.insert(index+1, '\n')


	"""
	if(u'女：' in talk):
		index = talks.index(talk)
		conversation = talk.split(u'\uff1a')
		talk_new = '    ' + 'n ' + r'"' + conversation[-1] + r'"'
		talks[index] = talk_new
		talks.insert(index+1, '\n')
	if(u'女声：' in talk):
		index = talks.index(talk)
		conversation = talk.split(u'\uff1a')
		talk_new = '    ' + 'n ' + r'"' + conversation[-1] + r'"'
		talks[index] = talk_new
		talks.insert(index+1, '\n')
	"""





# encode conversations and write them into the output file.
for talk in talks:
	talk = talk.encode('utf-8')
	outfile.write(talk + '\n')
	print talk
	
# close input and output streams.
infile.close()
outfile.close()

"""
测试结果：
Lins-MacBook-Pro:renpygame linqi$ python toRenpy.py
    scene cg00
    with dissolve


    scene cg01
    with dissolve


女：你在哪里，快出来啊？！
不行，绝对不能出去，这个女人，她已经疯了。
女：老老实实出来好不好？
    scene cg02
    with dissolve


电话，赶快，可恶，这里没有信号！
怎么办，怎么办，出去的话绝对会死的，这个女人已经疯了！
Pete，别躲了，你逃不掉的。
呼…..
呼….
噢噢噢！
这里有一格信号！
Pete，别躲了，你为什么总是要从我的身边逃走呢？
自己做的事情就要自己负责，不是么。
可恶！！！
如果当初……如果当初没有被她发现的话，就不会变成现在这样了。
如果，时间能够重来一次就好了！

问题：
1. 如何把多余的“！”等去掉；√
2. 把人名前缀（如“女：”）等替换掉；
3. 遇到关于CG的指示，替换成cg script；√
4. 将全部对话做成renpy script格式；
5. 解决句中中英文混杂的分句问题；√

"""