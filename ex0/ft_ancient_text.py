import sys
from typing import TextIO


def ft_ancient_text():
    path, *args = sys.argv

    if not args:
        print(f"Usage: {path} <file>")
        return
    print("=== Cyber Archives Recovery ===")

    file_name = args[0]
    f: TextIO | None = None
    
    try:
        print(f"Accessing file '{file_name}'")
        f: TextIO = open(file_name, "r", encoding="utf-8")
        data = f.read()
        print("---\n")
        print(data)
        print("\n---")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
