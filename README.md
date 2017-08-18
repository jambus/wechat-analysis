# wechat-analysis

### Use Guide
1.	For iphone users, extract the MM.sqlite and WCDB_Contact.sqlite from iphone backup with tool like 'IPhone Backup Extractor'. It can be found under:

`Application Domains/com.tencent.xin/Documents/[user hash value]/DB`

2. Put the 2 files into ./data folder if use default path.

3. It requires python3 to support run the script. Please download if python3 not yet installed.

4. Run script sample like below to do the anaylsis by search the wechat group name

`python3 main.py "XXX Wechat Group Name"`

Option command:
-o output.txt target output file path. Default, it will print in console
-m MM.sqlite target the path of MM.sqlite file. Default, it will read under ./data folder
-c WCDB_Contact.sqlite target the path of WCDB_Contact.sqlite file. Default it will read under ./data folder

### Current Feature Support
1.	Count the top 3 message senders in group
2. Count the top 3 welcome message senders in group
3. Count the top 3 happy birthday message senders in group
4. Count the top 3 thank boss message senders in group
5. Count the top 3 red package senders in group

### document Reference:

[https://daily.zhihu.com/story/8807166]()

[https://blog.naaln.com/2016/11/wechat-data-structure/]()
