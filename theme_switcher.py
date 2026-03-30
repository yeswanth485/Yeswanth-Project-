import sys

def main():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            text = f.read()
            
        replacements = {
            "from-blue-": "from-emerald-",
            "via-indigo-": "via-teal-",
            "to-violet-": "to-cyan-",
            "text-blue-": "text-emerald-",
            "bg-blue-": "bg-emerald-",
            "border-blue-": "border-emerald-",
            "shadow-[0_8px_25px_rgba(59,130,246": "shadow-[0_8px_25px_rgba(16,185,129",
            "shadow-[0_0_100px_rgba(59,130,246": "shadow-[0_0_100px_rgba(16,185,129",
            "shadow-[0_10px_40px_rgba(59,130,246": "shadow-[0_10px_40px_rgba(16,185,129",
            "shadow-[0_0_30px_rgba(59,130,246": "shadow-[0_0_30px_rgba(16,185,129",
            "border-blue-500/30": "border-emerald-500/30",
            "shadow-blue-": "shadow-emerald-",
            "decoration-blue-": "decoration-emerald-",
            "seclab-toast": "aegiscore-toast"
        }
        
        for k, v in replacements.items():
            text = text.replace(k, v)
            
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully updated colors in index.html to Emerald theme.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
