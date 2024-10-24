#!/usr/bin/python3
#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    arg_count = len(argv) - 1

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print(f"{arg_count} arguments:")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
