# coding:utf-8
from janome.tokenizer import Tokenizer
t = Tokenizer()
#malist = t.tokenize("This is a pen")
malist = t.tokenize(unicode("これは庭です。",'utf-8'))
for n in malist:
	print(n)