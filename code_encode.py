import string

all_chars=string.printable

#1.引入一个字符串
st='''Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.'''
print len(st)

#2.转换成为编码的List
encode_list=[]
for i in st:
    ii=all_chars.find(i)
    encode_list.append(ii)

print encode_list,'\n'
    
#3.转换完了加一个key
key=10
encode_list_key=[i+key for i in encode_list]#这个是一个循环数组的高级写法
print encode_list_key,'\n'

#4.加上key在这个数组之后
encode_list_key.append(key)

#5
print encode_list_key,'\n'

#6.decode阶段
decode_list=[]
for i in encode_list_key[:-1]:#不带最后一个元素
    i=i-key
    ii=all_chars[i]
    decode_list.append(ii)
print decode_list

#7.不知道key
for key in range(100):#假定key是0-100之间的数字
    key_list=[]
    for i in encode_list_key[:-1]:#不带最后一个元素
        try:
            i=i-key
            ii=all_chars[i]
            key_list.append(ii)
        except:
            pass
    st_decode=''.join(key_list)

    if 'the' in st_decode or 'have' in st_decode:
        break
    real_key=key
print 'The real key is:',real_key

#8.
print 'The decoded string is:',st_decode,'\n'

#9.
a=2.71
def encode_arbitrary(st,all_chars,a):
    encode_list=[]
    for i in st:
        ii=all_chars.find(i)
        encode_list.append(ii)
    encode_list=[i**a for i in encode_list]
    return encode_list

def decode_arbitrary(encode_list,all_chars,a):
    decode_list=[]
    for i in encode_list:
        i=i**(1/a)
        ii=all_chars[int(round(i))]
        decode_list.append(ii)
    return decode_list

aa=encode_arbitrary(st,all_chars,a)
print aa
result_decode=decode_arbitrary(aa,all_chars,a)
print ''.join(result_decode)

#10. 回答：以上这种方法当a是整数的时候会出错，因为1/a会被认为是python的整数间的处罚自动进行取整。解决方法是1/a在程序里换成1.0/a就好了。

#11  回答：可以大致通过encode之后数组的范围和all_chars的长度判断出来a具体是在一个比较小的整数范围内，然后用一个小的数量级比如0.01开始穷举法破译，再用7中的方式来验证是否正确。
