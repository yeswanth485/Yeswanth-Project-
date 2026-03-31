import py_compile
try:
    py_compile.compile('server.py', doraise=True)
    print("SUCCESS")
except py_compile.PyCompileError as e:
    print(e.msg)
