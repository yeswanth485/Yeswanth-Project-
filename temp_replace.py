import codecs
with codecs.open('d:/Final-year-project-main/server.py', 'r', 'utf-8') as f:
    lines = f.readlines()

# Note: Python lines are 0-indexed.
lines[724] = '    append_log(session_id, "=== GITHUB REPOSITORY AUDIT INITIATED ===", level="INFO")\n'
lines[773] = '    append_log(session_id, "=== GITHUB SCAN COMPLETE ===", level="SUCCESS")\n'
lines[1130] = '    append_log(session_id, "=== EXECUTIVE SECURITY AUDIT INITIATED ===", level="INFO")\n'
lines[1170] = '    append_log(session_id, "=== SCAN COMPLETE ===", level="SUCCESS")\n'
lines[1167] = '            append_log(session_id, f"[SCAN]   X Error: {site[\'name\']} | {str(e)}", level="WARNING")\n'
lines[1029] = '    pipeline_paused = True  # Restored pause\n'

with codecs.open('d:/Final-year-project-main/server.py', 'w', 'utf-8') as f:
    f.writelines(lines)
print("SUCCESS")
