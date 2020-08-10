def func(_path, _intrpType):  # noqa
    if _intrpType == 'read':
        file = open(_path, 'r')
        print(file.read())
        file.close()