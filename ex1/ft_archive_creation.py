import sys
from typing import TextIO


def ft_archive_creation() -> None:
    path, *args = sys.argv

    if not args:
        print(f"Usage: {path} <file>")
        return
    print("=== Cyber Archives Recovery ===")

    file_name = args[0]
    f: TextIO | None = None

    new_lines: list[str] = []
    lines: list[str] = []

    try:
        print(f"Accessing file '{file_name}'")
        f = open(file_name, "r", encoding="utf-8")
        data = f.read()
        print("---\n")
        print(data)
        print("\n---")

        lines = data.splitlines()

    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    finally:
        if f is not None:
            f.close()
            print(f"File '{file_name}' closed.\n")

    for l in lines:
        new_lines.append(l + '#')

    print("Transform data:")
    print("---\n")
    for n in new_lines:
        print(f"{n}")
    print("\n---")

    new_file_to_save = input("Enter new file name (or empty):")

    if new_file_to_save == "":
        print("Not saving data.")
        return

    try:
        f = open(new_file_to_save, "w", encoding="utf-8")

        print(f"Saving data to '{new_file_to_save}'")
        for n in new_lines:
            f.write(n + '\n')

    except OSError as e:
        print(f"Error opening file '{new_file_to_save}': {e}")
        print("Data not saved.")
        return

    finally:
        if f is not None:
            f.close()
            print(f"Data saved in file '{new_file_to_save}'.")


if __name__ == "__main__":
    ft_archive_creation()
