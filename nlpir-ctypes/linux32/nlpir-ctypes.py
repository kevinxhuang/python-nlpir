#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *
import codecs
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')
print sys.getdefaultencoding()

nlpir = CDLL('../../linux32/libNLPIR.so')

print type(nlpir)
print nlpir



def fillprototype(f, restype, argtypes):
    f.restype = restype
    f.argtypes = argtypes

MY_NLPIR_Init = getattr(nlpir, '_Z10NLPIR_InitPKciS0_')
MY_NLPIR_Exit = getattr(nlpir, '_Z10NLPIR_Exitv')
MY_NLPIR_ParagraphProcess = getattr(nlpir, '_Z22NLPIR_ParagraphProcessPKci')
MY_NLPIR_ImportUserDict = getattr(nlpir, '_Z20NLPIR_ImportUserDictPKc')
MY_NLPIR_FileProcess = getattr(nlpir, '_ZN6CNLPIR11FileProcessEPKcS1_i')
MY_NLPIR_AddUserWord = getattr(nlpir, '_Z17NLPIR_AddUserWordPKc')
MY_NLPIR_SaveTheUsrDic = getattr(nlpir, '_Z19NLPIR_SaveTheUsrDicv')
MY_NLPIR_DelUsrWord = getattr(nlpir, '_Z16NLPIR_DelUsrWordPKc')
MY_NLPIR_GetKeyWords = getattr(nlpir, '_Z17NLPIR_GetKeyWordsPKcib')
MY_NLPIR_GetFileKeyWords = getattr(nlpir, '_Z21NLPIR_GetFileKeyWordsPKcib')
MY_NLPIR_GetNewWords = getattr(nlpir, '_Z17NLPIR_GetNewWordsPKcib')
MY_NLPIR_GetFileNewWords = getattr(nlpir, '_ZN6CNLPIR15GetFileNewWordsEPKcib')
MY_NLPIR_SetPOSmap = getattr(nlpir, '_Z15NLPIR_SetPOSmapi')
MY_NLPIR_FingerPrint = getattr(nlpir, '_Z17NLPIR_FingerPrintPKc')
# New Word Identification
MY_NLPIR_NWI_Start = getattr(nlpir, '_Z15NLPIR_NWI_Startv')
MY_NLPIR_NWI_AddFile = getattr(nlpir, '_Z17NLPIR_NWI_AddFilePKc')
MY_NLPIR_NWI_AddMem = getattr(nlpir, '_Z16NLPIR_NWI_AddMemPKc')
MY_NLPIR_NWI_Complete = getattr(nlpir, '_Z18NLPIR_NWI_Completev')
MY_NLPIR_NWI_GetResult = getattr(nlpir, '_Z19NLPIR_NWI_GetResultb')
MY_NLPIR_NWI_Result2UserDict = getattr(nlpir, '_Z25NLPIR_NWI_Result2UserDictv')

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
