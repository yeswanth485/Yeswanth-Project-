import traceback, sys
try:
    with open('server.py', 'r', encoding='utf-8') as f:
        code = f.read()
    compile(code, 'server.py', 'exec')
except Exception as e:
    with open('error_py.txt', 'w', encoding='utf-8') as f:
        traceback.print_exc(file=f)
