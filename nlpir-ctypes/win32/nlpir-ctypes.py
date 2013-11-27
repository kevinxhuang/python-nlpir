#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *
import codecs
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')
print sys.getdefaultencoding()

nlpir = CDLL('../../win32/NLPIR.dll')

print type(nlpir)
print nlpir



def fillprototype(f, restype, argtypes):
    f.restype = restype
    f.argtypes = argtypes

MY_NLPIR_Init = getattr(dll, '?NLPIR_Init@@YA_NPBDH@Z')
MY_NLPIR_Exit = getattr(dll, '?NLPIR_Exit@@YA_NXZ')
MY_NLPIR_ParagraphProcess = getattr(dll, '?NLPIR_ParagraphProcess@@YAPBDPBDH@Z')
MY_NLPIR_ImportUserDict = getattr(dll, '?NLPIR_ImportUserDict@@YAIPBD@Z')
MY_NLPIR_FileProcess = getattr(dll, '?NLPIR_FileProcess@@YANPBD0H@Z')
MY_NLPIR_AddUserWord = getattr(dll, '?NLPIR_AddUserWord@@YAHPBD@Z')
MY_NLPIR_SaveTheUsrDic = getattr(dll, '?NLPIR_SaveTheUsrDic@@YAHXZ')
MY_NLPIR_DelUsrWord = getattr(dll, '?NLPIR_DelUsrWord@@YAHPBD@Z')
MY_NLPIR_GetKeyWords = getattr(dll, '?NLPIR_GetKeyWords@@YAPBDPBDH_N@Z')
MY_NLPIR_GetFileKeyWords = getattr(dll, '?NLPIR_GetFileKeyWords@@YAPBDPBDH_N@Z')
MY_NLPIR_GetNewWords = getattr(dll, '?NLPIR_GetNewWords@@YAPBDPBDH_N@Z')
MY_NLPIR_GetFileNewWords = getattr(dll, '?NLPIR_GetFileNewWords@@YAPBDPBDH_N@Z')
MY_NLPIR_SetPOSmap = getattr(dll, '?NLPIR_SetPOSmap@@YAHH@Z')
MY_NLPIR_FingerPrint = getattr(dll, '?NLPIR_FingerPrint@@YAKPBD@Z')
# New Word Identification
MY_NLPIR_NWI_Start = getattr(dll, '?NLPIR_NWI_Start@@YA_NXZ')
MY_NLPIR_NWI_AddFile = getattr(dll, '?NLPIR_NWI_AddFile@@YAHPBD@Z')
MY_NLPIR_NWI_AddMem = getattr(dll, '?NLPIR_NWI_AddMem@@YA_NPBD@Z')
MY_NLPIR_NWI_Complete = getattr(dll, '?NLPIR_NWI_Complete@@YA_NXZ')
MY_NLPIR_NWI_GetResult = getattr(dll, '?NLPIR_NWI_GetResult@@YAPBD_N@Z')
MY_NLPIR_NWI_Result2UserDict = getattr(dll, '?NLPIR_NWI_Result2UserDict@@YAIXZ')

fillprototype(MY_NLPIR_Init, c_bool, [c_char_p, c_int])
fillprototype(MY_NLPIR_Exit, c_bool, None)
fillprototype(MY_NLPIR_ParagraphProcess, c_char_p, [c_char_p, c_int])
fillprototype(MY_NLPIR_ImportUserDict, c_uint, [c_char_p])
fillprototype(MY_NLPIR_FileProcess, c_double, [c_char_p, c_char_p, c_int])
fillprototype(MY_NLPIR_AddUserWord, c_int, [c_char_p])
fillprototype(MY_NLPIR_SaveTheUsrDic, c_int, None)
fillprototype(MY_NLPIR_DelUsrWord, c_int, [c_char_p])
fillprototype(MY_NLPIR_GetKeyWords, c_char_p, [c_char_p, c_int, c_bool])
fillprototype(MY_NLPIR_GetFileKeyWords, c_char_p, [c_char_p, c_int, c_bool])
fillprototype(MY_NLPIR_GetNewWords, c_char_p, [c_char_p, c_int, c_bool])
fillprototype(MY_NLPIR_GetFileNewWords, c_char_p, [c_char_p, c_int, c_bool])
fillprototype(MY_NLPIR_SetPOSmap, c_int, [c_int])
fillprototype(MY_NLPIR_FingerPrint, c_ulong, [c_char_p])
# New Word Identification
fillprototype(MY_NLPIR_NWI_Start, c_bool, None)
fillprototype(MY_NLPIR_NWI_AddFile, c_bool, [c_char_p])
fillprototype(MY_NLPIR_NWI_AddMem, c_bool, [c_char_p])
fillprototype(MY_NLPIR_NWI_Complete, c_bool, None)
fillprototype(MY_NLPIR_NWI_GetResult, c_char_p, [c_int])
fillprototype(MY_NLPIR_NWI_Result2UserDict, c_uint, None)

look_gb = codecs.lookup('gb2312')
look_utf = codecs.lookup('utf-8')

if not MY_NLPIR_Init('../../', 1):
    print 'NLPIR Initial failed!'
    exit()

sentence = u"我爱我的祖国，亲爱的祖国！"
print type(sentence)
print sentence

result = MY_NLPIR_ParagraphProcess(sentence.encode('gb2312'), c_int(1))
print result

result_unicode = look_utf.decode(result)[0]
print result_unicode

result_gb2312 = look_gb.encode(result_unicode)[0]
print result_gb2312

result_gbk = look_gb.decode(result_gb2312)[0]
print result_gbk

MY_NLPIR_Exit()

print 'Goodbye!'
