toRenpy.py helps a non-progammer to transfer a story written in Chinese to renpy script format.
toRenpy.py可以帮助非程序员把中文写成的故事转化成Renpy script格式。

=================================

EXAMPLE:
使用效果：

> text.txt （input file）

CG02
【黑场】【前景：手机表示无信号的UI图片】
电话，赶快，可恶，这里没有信号！怎么办，怎么办，出去的话绝对会死的，这个女人已经疯了！

【模糊背景：女生身形，非常模糊，逆光】
女：Pete，别躲了，你逃不掉的。

> script.rpy （output file）

    scene cg02
    with dissolve

    "电话，赶快，可恶，这里没有信号！"

    "怎么办，怎么办，出去的话绝对会死的，这个女人已经疯了！"

    n "Pete，别躲了，你逃不掉的。"


HOW TO USE:

*** Currently only working on Chinese txt file ***
*** Written in Python 2.7.8 ***

1. Set directories of input file(UTF-8) and output file on Line 10&11
2. Set the person who is talking and relevant renpy name on Line 14
3. Open terminal and type "Python toRenpy.py"
4. For advanced use please customize the list "sentence_customize"
5. Any question, dont's hesitate to ask qili@tcd.ie

使用方法：

－－－ 目前只支持中文txt文件 －－－
－－－ 版本：Python 2.7.8 －－－

1. 在第10行和第11行，设定来源文件（.txt UTF-8）和目标文件（.rpy）的文件地址
2. 在第14行， 设定剧本中的人名和对应的Renpy脚本名字
3. 打开terminal，输入"Python toRenpy.py" 即可进行转换
4. 高级用法请修改list "sentence_customize"
5. 任何问题请致信 qili@tcd.ie



