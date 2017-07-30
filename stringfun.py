Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=['she', 'sells' ,'sea', 'shells', 'by', 'the', 'sea', 'shore']
>>> b="selfish shellfise"
>>> c=[1,1,2,3,5,8,13]
>>> b[3:4]
'f'
>>> c[5]
8
>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[2:4]
['sea', 'shells']
>>> b=[8:13]
SyntaxError: invalid syntax
>>> b[8:13]
'shell'
>>> c[1]
1
>>> c[2]
2
>>> c[1]+c[2]
3
>>> a*3
['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore', 'she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
>>> 'self' in b
True
>>> a[2] == a[6]
True
>>> 'by' in a
True
>>> [1,2,3] in c
False
>>> [1,2,5] in c
False
>>> [1,1,2] in c
False
>>> [1] in c
False
>>> (1) in c
True
>>> a[3] == b[8:13]
False
>>> dog='dalmatian'
>>> len(dog)
9
>>> dogs=[dog,'poodle','boxer']
>>> len(dogs)
3
>>> def string_test(s)
SyntaxError: invalid syntax
>>> 
======= RESTART: /home/student/mor19_lab5/meet2017y1lab5/stringfun.py =======
>>> string_test(mor)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    string_test(mor)
NameError: name 'mor' is not defined
>>> 
======= RESTART: /home/student/mor19_lab5/meet2017y1lab5/stringfun.py =======
>>> 
======= RESTART: /home/student/mor19_lab5/meet2017y1lab5/stringfun.py =======
>>> string_test
<function string_test at 0x7f8a2719c488>
>>> mor
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    mor
NameError: name 'mor' is not defined
>>> 
======= RESTART: /home/student/mor19_lab5/meet2017y1lab5/stringfun.py =======
 
>>> string_test(s)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    string_test(s)
NameError: name 's' is not defined
>>> 
======= RESTART: /home/student/mor19_lab5/meet2017y1lab5/stringfun.py =======
 
>>> string_test(mor)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    string_test(mor)
NameError: name 'mor' is not defined
>>> 
