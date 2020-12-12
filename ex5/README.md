cat Single file
===============
```
>> python3 cat.py A.txt
This text is from A.txt
```
cat Multiple file
=================
```
>> python3 cat.py A.txt B.txt C.txt 
This text is from A.txt
This text is from B.txt
This text is from C.txt
```
cat Multiple file and write to another file
===========================================
```
>> python3 cat.py A.txt B.txt C.txt -w D.txt
>> cat D.txt
This text is from A.txt
This text is from B.txt
This text is from C.txt
```
cat Multiple file with line number
==================================
```
>> python3 cat.py A.txt B.txt C.txt -n
        1       This text is from A.txt
        2       This text is from B.txt
        3       This text is from C.txt
```
cat Multiple file with line number and write to another file
============================================================
```
>> python3 cat.py A.txt B.txt C.txt -n -w D.txt
>> cat D.txt
        1       This text is from A.txt
        2       This text is from B.txt
        3       This text is from C.txt
```
