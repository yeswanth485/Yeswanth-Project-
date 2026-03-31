import traceback
try:
    with open('server.py', 'r', encoding='utf-8') as f:
        source = f.read()
    compile(source, 'server.py', 'exec')
    print("SUCCESS")
except SyntaxError as e:
    print(f"SYNTAX ERROR: {e.msg} at line {e.lineno}")
    traceback.print_exc()
except Exception as e:
    print(f"OTHER ERROR: {e}")
    traceback.print_exc()
