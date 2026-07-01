def secure_archive(
        name_file: str,
        action: str = "read",
        content: str = "") -> tuple[bool, str]:
    try:
        if action == "write":
            with open(name_file, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
        elif action == "read":
            with open(name_file, "r") as file:
                data = file.read()
                return (True, data)
        else:
            print("That action doesn't exist, please choice between "
                  "read or write")
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not.txt", "read"))
    print()

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("text.txt", "write", "hola"))


if __name__ == "__main__":
    main()
