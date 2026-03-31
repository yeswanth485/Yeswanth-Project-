import traceback
try:
    with open('server.py', 'r', encoding='utf-8') as f:
        source = f.read()
    compile(source, 'server.py', 'exec')
    with open('compile_result.txt', 'w', encoding='utf-8') as f:
        f.write('SUCCESS')
except Exception as e:
    with open('compile_result.txt', 'w', encoding='utf-8') as f:
        traceback.print_exc(file=f)
    print('ERROR CAUGHT')
