import sys
from typing import List, Optional, TextIO


def read_file(file_name: str) -> str:
    f: Optional[TextIO] = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        data = f.read()
        return data
    finally:
        if f is not None:
            try:
                f.close()
                print(f"File '{file_name}' closed.\n")
            except Exception:
                pass


def write_file(new_file_to_save: str, new_lines: List[str]) -> None:
    f: Optional[TextIO] = None
    try:
        f = open(new_file_to_save, "w", encoding="utf-8")
        for n in new_lines:
            f.write(n + "\n")
    finally:
        if f is not None:
            try:
                f.close()
                print(f"File '{new_file_to_save}' closed.\n")
            except Exception:
                pass


def transform_lines(lines: List[str]) -> List[str]:
    return [line + "#" for line in lines]


def print_data(data: str, suffix: str = "") -> None:
    print("---\n")
    for index, line in enumerate(data.splitlines(), start=1):
        print(f"[FRAGMENT {index:03d}] {line}{suffix}")
    print("\n---")


def ft_archive_creation() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    file_name = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")

    try:
        print(f"Accessing file '{file_name}'")
        data = read_file(file_name)
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    print("Original data:")
    print_data(data)

    lines = data.splitlines()
    new_lines = transform_lines(lines)

    print("Transformed data preview:")
    print_data("\n".join(new_lines))

    print("Enter new file name (or empty):", end="")
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
