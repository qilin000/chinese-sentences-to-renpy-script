# -*- coding: utf-8 -*-
import sys
import re
#import zhon
#from zhon import hanzi

# -----------------get Chinese sentences(list) ready--------------------

# set dir of source file and output file.
indir = '/Users/linqi/Projects/renpygame/test_s.txt'
outdir = '/Users/linqi/Projects/renpygame/test_test.txt'

# get a source file and an output file. decode chinese words.
infile = open(indir, 'rU')
source = infile.read().decode('utf-8')
outfile = open(outdir, 'w')

# customize zhon.hanzi.sentence pattern, to match a sentence contains english words, chinese words and more than one chinese stops.
# this pattern will make sure only conversations are extracted.
# also match CG notes, for example: Cg00 
sentence_customize = u'[\u3007\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\u2f00-\u2fd5\u2e80-\u2ef3\uff02\uff03\uff04\uff05\uff06\uff07\uff08\uff09\uff0a\uff0b\uff0c\uff0d\uff0f\uff1a\uff1b\uff1c\uff1d\uff1e\uff20\uff3b\uff3c\uff3d\uff3e\uff3f\uff40\uff5b\uff5c\uff5d\uff5e\uff5f\uff60\uff62\uff63\uff64\u3000\u3001\u3003\u300b\u300c\u300d\u300e\u300f\u3010\u3011\u3014\u3015\u3016\u3017\u3018\u3019\u301a\u301b\u301c\u301d\u301e\u301f\u3030\u303e\u303f\u2013\u2014\u2018\u2019\u201b\u201c\u201d\u201e\u201f\u2026\u2027\ufe4f]*[\u0041-\u005a\u0061-\u007a]*[\u3007\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\u2f00-\u2fd5\u2e80-\u2ef3\uff02\uff03\uff04\uff05\uff06\uff07\uff08\uff09\uff0a\uff0b\uff0c\uff0d\uff0f\uff1a\uff1b\uff1c\uff1d\uff1e\uff20\uff3b\uff3c\uff3d\uff3e\uff3f\uff40\uff5b\uff5c\uff5d\uff5e\uff5f\uff60\uff62\uff63\uff64\u3000\u3001\u3003\u300b\u300c\u300d\u300e\u300f\u3010\u3011\u3014\u3015\u3016\u3017\u3018\u3019\u301a\u301b\u301c\u301d\u301e\u301f\u3030\u303e\u303f\u2013\u2014\u2018\u2019\u201b\u201c\u201d\u201e\u201f\u2026\u2027\ufe4f]*[\uff01\uff1f\uff61\u3002\u2026\u002e]+|[Cc][Gg][01][0-9]'

# filter chinese sentences out of the source file. talks is a list.
talks = re.findall(sentence_customize, source)

# -----------------start converting--------------------

# render all conversations to renpy script format
# (four spaces + character code + one space + conversation inside double quotes)
# for example:
# 		女：你在哪里，快出来啊？！
# will be rendered to:
# 		n "你在哪里，快出来啊？！"
# render all cg notes to renpy script format
# (four spaces + background code and "with dissolve" on second line with same indentation)
# eg.    scene bg02
#        with dissolve


# a list of names needs to be converted
name_tuples = [(u'女：', 'n'), (u'女声：', 'n'), (u'Lily：', 'l'), (u'服务生：', 'w'), (u'Anna：', 'a'), (u'警察：', 'p'), (u'警察A：', 'p_a'), (u'警察B：', 'p_b')]	

# capture cg notes and all the name titles and do the converting job
for talk in talks:
	if(re.search(r'[Cc][Gg][01][0-9]', talk)):
		index = talks.index(talk)
		talk_new = '    ' + 'scene ' + talk.lower()
		talks[index] = talk_new
		with_dissolve = '    ' + 'with dissolve' + '\n'
		talks.insert(index+1, with_dissolve)

	for name in name_tuples:
		if(name[0] in talk):
			index = talks.index(talk)
			conversation = talk.split(u'\uff1a')
			talk_new = '    ' + name[1] + ' ' + r'"' + conversation[-1] + r'"'
			talks[index] = talk_new + '\n'

# capture 'my conversations' and do the converting job

for talk in talks:
	if(re.search(r'^\s\s\s\s', talk)):
		continue
	else:
		index = talks.index(talk)
		talk_new = '    ' + r'"' + talk + r'"'
		talks[index] = talk_new + '\n'

# -----------------finish converting--------------------


# encode conversations and write them into the output file.
for talk in talks:
	talk = talk.encode('utf-8')
	outfile.write(talk + '\n' + '\n')
	print talk
	
# close input and output streams.
infile.close()
outfile.close()


"""
问题：
1. 如何把多余的“！”等去掉；√
2. 把人名前缀（如“女：”）等替换掉；√
3. 遇到关于CG的指示，替换成cg script；√
4. 将全部对话做成renpy script格式；√
5. 解决句中中英文混杂的分句问题；√

"""