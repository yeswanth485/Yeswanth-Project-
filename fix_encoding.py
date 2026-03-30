import os

files_to_fix = ['server.py', 'index.html', 'seed_data.py', 'docker-compose.yml']

for f in files_to_fix:
    path = os.path.join(r'd:\Final-year-project-main', f)
    if not os.path.exists(path):
        continue
    
    with open(path, 'rb') as fd:
        content = fd.read()
    
    try:
        # Check for BOMs
        if content.startswith(b'\xff\xfe'):
            text = content.decode('utf-16le')
            # remove BOM
            if text.startswith('\ufeff'):
                text = text[1:]
        elif content.startswith(b'\xfe\xff'):
            text = content.decode('utf-16be')
            if text.startswith('\ufeff'):
                text = text[1:]
        elif content.startswith(b'\xef\xbb\xbf'):
            text = content[3:].decode('utf-8')
        else:
            text = content.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error decoding {f}: {e}")
        continue
        
    with open(path, 'w', encoding='utf-8', newline='') as fw:
        fw.write(text)
        
    print(f"Sanitized and replaced {f} with pure UTF-8 encoding.")
