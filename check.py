try:
    import server
    print("SUCCESS: server.py imported correctly.")
except Exception as e:
    import traceback
    traceback.print_exc()
