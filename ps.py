from traceback import print_exc
from re import match
from os import system as sys
sys("")
arg_0 = arg_1 = 0
try:
    import functions.print as print_func
    import functions.if_c as if_func
    import functions.open as open_func
    class FuncDefs:  # noqa
        @staticmethod
        def funcReader(_line, func_):
            return _line.replace(' ', '').startswith(func_)
    class Err:  # noqa
        @staticmethod
        def err01():
            print_func.func('\033[31mERR\033[0m> Invalid args for args 0, 1 aren\'t the same value type.')
        @staticmethod  # noqa
        def err02():
            print_func.func('\033[31mERR\033[0m> Invalid args for [\'read\'/\'run\']')
        @staticmethod  # noqa
        def err03():
            print_func.func('\033[31mERR\033[0m> Nesting invalid for functions, \'open\'')

    def fileReader(file_, allow_nst_):  # noqa
        with open(file_, 'r') as _rfile:
            _rfile = _rfile.read()
            _split = _rfile.split('\n')
            for i in _split:
                if FuncDefs.funcReader(i, 'print'):
                    try:
                        print_func.func(i.split(' ', 1)[1])
                    except:
                        print_exc()
                elif FuncDefs.funcReader(i, 'if'):
                    try:
                        _args = (i.split(' ', 1)[1]).split(':', 1)[0]
                        if _args.split(' ')[1] == '==':
                            __arg0 = __arg1 = False
                            if _args.split(' ')[0].isnumeric() or match('^[0-9 /*\-+]*$', _args.split(' ')[0]):
                                exec('arg_0 = ' + str(eval(_args.split(' ')[0])), globals())
                                __arg0 = True
                            if _args.split(' ')[2].isnumeric() or match('^[0-9 /*\-+]*$', _args.split(' ')[2]):
                                exec('arg_1 = ' + str(eval(_args.split(' ')[2])), globals())
                                __arg1 = True
                            if __arg0 is True and __arg1 is True:
                                print(str(arg_0))
                                print(str(arg_1))
                                if_func.func(arg_0, arg_1, i, 'execDef()')
                            elif __arg1:
                                Err.err01()
                            elif __arg0:
                                Err.err01()
                            else:
                                if_func.func(_args.split(' ')[0], _args.split(' ')[2], i, 'execDef()')
                    except:
                        print_exc()
                elif FuncDefs.funcReader(i, 'open'):
                    try:
                        _args = i.split(' ', 1)[1].rsplit(' | ', 1)
                        if _args[1] == 'read':
                            _path = _args[0].replace('(', '', 1).replace(')', '', -1)
                            open_func.func(_path, 'read')
                        elif _args[1] == 'run':
                            if allow_nst_:
                                _path = _args[0].replace('(', '', 1).replace(')', '', -1)
                                fileReader(_path, False)
                            else:
                                Err.err03()
                        else:
                            Err.err02()
                    except:
                        print_exc()


    fileReader('pythonscript_script.txt', True)
except:
    print_exc()
""" 
print_func.func('Test')
_var = True
if_func.func(_var, True, "print('raw python code')")
if_func.func(_var, False, "print('more raw python code')")
"""
while 1:
    pass
