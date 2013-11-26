#!/usr/bin/env python
# -*-coding: utf-8 -*-

from PyNLPIR import *
import sys
import locale

reload(sys)
sys.setdefaultencoding('UTF-8')

def p(f):
    print '%s.%s(): %s' % (f.__module__, f.__name__, f())

# 返回使用UCS-2还是UCS-4
print sys.maxunicode

# 检查标准输出流的编码
print sys.stdout.encoding

# 返回当前系统所使用的默认字符编码
p(sys.getdefaultencoding)

# 返回用于转换Unicode文件名至系统文件名所使用的编码
p(sys.getfilesystemencoding)

# 获取默认的区域设置并返回元祖(语言, 编码)
p(locale.getdefaultlocale)

# 返回用户设定的文本数据编码
# 文档提到this function only returns a guess
p(locale.getpreferredencoding)

if __name__ == '__main__':

    nlpir_init('.', 'UTF-8')

    firstTest = nlpir_paragraph_process(u'你好中国，我亲爱的祖国！GBK， GB2312, GB18030是中文的三种字符集，UCS是万国字符集！'.encode('gbk'))
    print type(firstTest)
    print repr(firstTest)
    print firstTest

    print

    secondTest = nlpir_paragraph_process(u'编码真是但疼啊！'.encode('gbk'), True)
    print type(secondTest)
    print repr(secondTest)
    print secondTest

    nlpir_exit()
