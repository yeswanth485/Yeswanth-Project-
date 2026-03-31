import io
try:
    with open('server.py', 'rb') as f:
        data = f.read()
    
    # Check if it starts with UTF-16 LE BOM (FF FE)
    if data.startswith(b'\xff\xfe'):
        text = data.decode('utf-16')
        with open('server.py', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Converted server.py from UTF-16 to UTF-8")
    else:
        # Maybe it's missing BOM but still UTF-16
        if b'\x00' in data[:100]:
            text = data.decode('utf-16le')
            with open('server.py', 'w', encoding='utf-8') as f:
                f.write(text)
            print("Converted server.py from UTF-16LE (no BOM) to UTF-8")
        else:
            print("File is already UTF-8 or not UTF-16")
except Exception as e:
    print(f"Error: {e}")
