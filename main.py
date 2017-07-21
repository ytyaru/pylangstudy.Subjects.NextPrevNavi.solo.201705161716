#!python3
#encoding: utf-8
class MyClass(object):
    def __init__(self):
        self.__name = 'NAME'
    def Show(self):
        print('Name is {0}'.format(self.__name))


if __name__ == '__main__':
    c = MyClass()
    c.Show()
