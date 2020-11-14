# import keyword
# print(keyword.kwlist)#输出关键词表，不可以用作文件名或者函数变量名
#标识符就是变量、函数、类、模块和其他对象起的名字，不能以数字作为开头，大小写区分
#变量
name="玛利亚"
print(name)
#变量有三个部分组成，分别是标识、类型、值
#标识标识对象所存储的内存地址，可以通过内置函数id(obj)来获得
print('标识',id(name))
print('类型',type(name))
#当进行多次赋值之后
name='奥特曼'
print(name)
print('标识',id(name))#那么之前的内存地址就是一个内存垃圾，现在指向一个新的空间