import sys
from typing import TextIO


def read_file(file_name: str) -> str:
    f: TextIO | None = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        data = f.read()
        return data
    finally:
        if f is not None:
            f.close()


def write_file(new_file_to_save: str, new_lines: list[str]) -> None:
    f: TextIO | None = None
    try:
        f = open(new_file_to_save, "w", encoding="utf-8")
        for n in new_lines:
            f.write(n + '\n')
    finally:
        if f is not None:
            f.close()


def transform_lines(lines: list[str]) -> list[str]:
    return [line + '#' for line in lines]


def ft_archive_creation() -> None:
    path, *args = sys.argv

    if not args:
        print(f"Usage: {path} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")

    file_name = args[0]

    new_lines: list[str] = []
    lines: list[str] = []

    try:
        print(f"Accessing file '{file_name}'")
        data = read_file(file_name)
        print("---\n")
        print(data)
        print("\n---")
        print(f"File '{file_name}' closed.\n")

        lines = data.splitlines()
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}", file=sys.stderr)
        return

    print("Transform data:")
    new_lines = transform_lines(lines)
    print("---\n")
    for n in new_lines:
        print(f"{n}")
    print("\n---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    line_input = sys.stdin.readline().rstrip("\n")
    if line_input == "":
        print("Not saving data.")
        return
    else:
        new_file_to_save = line_input

    try:
        print(f"Saving data to '{new_file_to_save}'")
        write_file(new_file_to_save, new_lines)
        print(f"Data saved in file '{new_file_to_save}'.")
    except OSError as e:
        print(f"Error opening file '{new_file_to_save}': {e}", file=sys.stderr)
        print("Data not saved.")
        return


if __name__ == "__main__":
    ft_archive_creation()
