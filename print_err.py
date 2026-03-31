import pathlib
p = pathlib.Path('server_stderr.txt')
print(p.read_bytes()[:200])
try:
    print(p.read_text('utf-16le'))
except:
    try:
        print(p.read_text('utf-8'))
    except:
        pass
