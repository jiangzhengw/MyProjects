"# MyHogwartsProjects"
知识点积累：
一、
    # 反斜杠转义
    print('C:\\some\\name')
    # r表示原生
    print(r'C:\some\name')
    # python的自动拼接
    print('Py' + 'thon')

二、python字符串引号前面的字母修饰符作用(r, u, f, b)
    1. u’这是一个字符串’
    解释:将引号中字符串按照unicode(万国码)编码, 这也是python3默认的编码方式.有关unicode编码问题, 我另一篇博客mark了一位大神一篇非常好的文章, 可以自行查看.
    https://www.cnblogs.com/vipchenwei/p/6993788.html

    2. r’这个字符串不会处理转义字符\n’
    解释:将引号中字符串中转义字符忽略, 例如上边print(r’\n’)会原封不动输出’\n’而不是换行.

    3. b’这是一个bytes类型’
    解释:字节, 即8bit, 网络编程中数据传输都是按照bytes类型.

    4. f’这个字符串中用大括号括起来的{1+1}会被执行’
    print('C:\\some\\name{x}\\{y}'.format(y=x, x=123))
    print(f'C:\\some\\name{x}')

三、
    # os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表,不包含./ ../
    # os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError，在Unix, Windows中有效
    # os.system() 理解：https://www.cnblogs.com/cwp-bg/p/8465566.html
    # os.system() 方法将字符串转化成命令在服务器上运行
    # __file__表示显示文件当前的位置