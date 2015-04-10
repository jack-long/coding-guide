Linux Advanced Commands
===========================
1) date
------------
```bash
date
# Sat Jan  3 17:54:11 CST 2015
date "+DATE: %Y-%m-%d%nTIME: %H:%M:%S"
# DATE: 2015-01-04
# TIME: 14:02:52
```

An operand with a leading plus (`+') sign signals a user-defined format
string which specifies the format in which to display the date and time.
The format string may contain any of the conversion specifications
described in the strftime(3) manual page, as well as any arbitrary text.
A newline (`\n') character is always output after the characters speci-
fied by the format string.  The format string for the default display is
``+%+''.

2) cd: Move
-------------
go home
```bash
cd
```
go back to the last directory
```bash
cd -   
```

3) Read your mail
-------------
$ mail
No mail for jack

4) To print file
$ pr {file}

5) Print or Check SHA-1 Checksums
$ shasum {file}
7cd4346d1983d960b22a8ca107ca345bf759703d  {filename}

6) MD5 Checksums
$ md5 {file}
MD5 (test) = c35bc44ac39ac3c8c636be7f3871782e

7) IO Control
与 Windows 系统下不同的是，Linux 系统下还有一个标准错误输出的概念。
为程序调试和系统维护，错误输出和标准输出分开可以让一些高级的错误信息不干扰正常的输出信息。
BASH 中一般将标准输出表示为 1，将标准错误输出表示为 2。

$ find /home -name lost* 2> err_result 
这个命令在 ">" 符号之前多了一个 "2"，"2>" 表示将标准错误输出重定向。
由于 /home 目录下有些目录由于权限限制不能访问，因此会产生一些标准错误输出被存放在
 err_result 文件中。

如果直接执行 find /home -name lost* > all_result
其结果是只有标准输出被存入 all_result 文件中，
要想让标准错误输出和标准输入一样都被存入到文件中，那该怎么办呢？

$ find /home -name lost* > all_result 2>& 1 
上面这个例子中将首先将标准错误输出也重定向到标准输出中，再将标准输出重定向到 
all_result 这个文件中。这样我们就可以将所有的输出都存储到文件中了。

为实现上述功能，还有一种简便的写法如下： 
$ find /home -name lost* >& all_result 
如果那些出错信息并不重要，下面这个命令可以让你避开众多无用出错信息的干扰： 
$ find /home -name lost* 2> /dev/null

试验一下如下几种重定向方式，看看会出什么结果，为什么？ 
$ find /home -name lost* > all_result 1>& 2 
$ find /home -name lost* 2> all_result 1>& 2 
$ find /home -name lost* 2>& 1 > all_result

下面还几种不常见的用法： n<&- 表示将 n 号输入关闭 
<&- 表示关闭标准输入（键盘） 
n>&- 表示将 n 号输出关闭 
>&- 表示将标准输出关闭

8) Background Jobs(Process) Management
Command &: run in background
CTRL+C: kill the current process (%1)
CTRL+Z: suspend foreground job in background
jobs: list background jobs.
fg [%jobnumber]: Returns the last paused job to the foreground.
bg [%jobnumber]: Run last paused background job.  (%2)
kill [%jobnumber | pid]: Abort job.
** $ fg 3 : bring job #3 to foreground (without %) ?? need checking

9) df: [display file system disk space usage]
df [option][disc|file]
option:
-h: human readable format (e.g., 1K 234M 2G)

10) du: [display file space usage]
du [option][file]
options:
-h: human readable format (e.g., 1K 234M 2G)
-s: (summarise) display only a total for each argument

11) file:
file filename
Check the type/format of file

12) find:
到指定的目录下寻找文件名
find [路径][语法]
find /bin -name ps*

13) cat: [concatenate and print]
cat [option] [file]
option:
-n: (number) number all output lines
*cat    Concatenate standard input to standard output.
*显示文件内容: cat filename
*显示多个文件: cat file1 file2
*将file1,file2写入file3: cat file1 file2 > file3
*将标准输入端内容写入文件: cat > file  (执行此命令后输入内容，NewLine & Ctrl+D结束)

14) head:
head [option][file]
options:
-c: 以Byte为单位的数量
-n: 以行为单位的数量
默认显示文件前10行

15) tail:
similar with head，only count from the End.
tail -n 20 file
默认显示文件后10行
-f output appended data as the file grows, for example,
to monitor on the log file: 
$ tail -f log-file

16) less
全屏显示文件内容，并可搜索指定内容
less [option][file]
-N 显示行号
-s 连续的空白行仅显示一行
-S 过长的行不换行显示
-x n 将TAB用n个空格取代
搜索操作：/字符串, 'U' and 'N' for navigation
Example: $ ls | less
more: print contents at current screen    

17) tar （tape archive）
tar [option][archive name][target file]
option:
First option must be a mode specifier:
  -c Create  -r Add/Replace  -t List  -u Update  -x Extract
-k 打开包文件时不覆盖原有文件
-K 从指定文件开始还原
-t 列出包文件内容
-u (update)将较新文件放进包中
-v 显示过程
-x 解开包文件
-Z 通过compress处理
-z 通过gzip处理
—- delete 删除包文件中指定的文件
—- exclude=FILE 排除FILE

18) History
$ history
...
542  cd
543  pwd

$ history | grep "test"
...
461  cmp test test2
462  diff test test2
524  md5 test
525  shasum test

$ CTRL+R
It will display “reverse-i-search” and you can type any combination of letters. For example, “myarticle”.
This will display a match of the most recent command in your history containing “myarticle”. When you find what you were looking for, press Enter ⏎ to execute the suggested command.

I’ve seen that the history keeps only my 1000 previous commands. 
How to (de|in)crease this limit?
You can change this limit in your ~/.bashrc. Look at the line with HISTSIZE=1000 and update it to fit your needs.
If you’ve written some bad or shameful things in your history you can simply erase it with
history -c

19) Bang !
$ ![number]     # Execute the command in history.

** “bang bang” command **
I’ve typed a command that requires privileges but I’ve forgot to use sudo. 
Any advice?
Enter !! (known as “bang bang”) to run the previous command. 
$ apt-get update
$ sudo !!         # will run sudo apt-get update

** Exclamation point **
Ok, I have a super-awesome memory and I can remember every commands I’ve typed. How can I run what I’ve typed seven commands ago ?
Easy ! Use !-[number] 
$ !-7

I want to find the last command that started with a specific text (e.g. “ls”) Use ![expression]
$ !ls             # will run ls -la ~/Pictures

I want to get the previous command without the first word Use !*
$ cp article.txt ./blog/article.txt
$ mv !*         # will run mv article.txt ./blog/article.txt

I want to get the first argument of the previous command Use !^
$ cp article.txt ./blog/article.txt
$ nano !^         # will run nano article.txt

I want to get the last argument of the previous command Use !$
$ cp article.txt ./blog/article.txt
$ nano !$         # will run nano ./blog/article.txt

To go a little bit further you can use all the previous commands with the following syntax: [command]:p : It prints out the command instead of running it
$ !!:p             # prints (but don't execute) 
nano my-so-long-file-$ name.txt

20) Two Commands at Once
$ command1 ; command2       # Run 2 regardless of 1
$ command1 && command2      # Run 2 only if 1 Success
$ command1 || command2      # Run 2 only if 1 Failed

21) Edit Shortcuts
CTRL+U: Erase to Beginning
CTRL+W: Erase word by word
CTRL+K: Erase all to the right
CTRL+Y: Undo Erase
CTRL+A: Move to Biginning
CTRL+E: Move to End

22) alias
$ alias [alias-name]=[command]
If you want your alias to persist, you have to add it to your ~/.bashrc.

23) say (in OS X)
say Hello
