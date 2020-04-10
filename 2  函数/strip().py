#------------------------------------------------
#注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。strip()脱光

stra = '00000000000032100000000123000000000'

stra.strip('0')  #建立副本
# '32100000000123'
stra
# '00000000000032100000000123000000000'  #原str没变


stra = '        32100000000123        '
stra.strip()  #建立副本
# '32100000000123'

strb = 'ab00000ba'
strb.strip('ab')
#'00000' 去除ab的任意组合


strb = 'abc00000bca'
strb.strip('abc')
#'00000'  去除abc的任意组合

#None 和异常的 and 返回None
print(None and None.strip())
bool(None and None.strip())

