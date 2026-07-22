#!/usr/bin/env python3


def secure_archive(
    filename: str,
    action: str = "read",
    content: str | None = None,
) -> tuple[bool, str]:
    try:
        if action == "write":
            with open(filename, "w") as file:
                file.write(content if content is not None else "")
            return (True, "Content successfully written to file")
        with open(filename, "r") as file:
            return (True, file.read())
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    success: bool
    data: str
    success, data = secure_archive("ancient_fragment.txt", "read")
    print((success, data))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    if success:
        print(secure_archive("new_fragment.txt", "write", data))


if __name__ == "__main__":
    main()
