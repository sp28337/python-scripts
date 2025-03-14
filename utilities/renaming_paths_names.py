import os


def rename(path: str, to_del: str, max_depth: int, curr_depth=0) -> None:
    try:
        if curr_depth > max_depth:
            return
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                rename(entry_path, to_del, max_depth, curr_depth + 1)
            else:
                if to_del in entry:
                    new_name = entry.replace(to_del, '')
                    old_path = os.path.join(path, entry)
                    new_path = os.path.join(path, new_name)
                    os.rename(old_path, new_path)

    except Exception as e:
        print(e)


def main():
    directory = input('Enter directory to start renaming: ')
    text_to_del = 'MEGASLIV.BIZ' # input('Enter text that you want to delete from names: ')
    depth = int(input('Enter max recursion depth: '))
    rename(directory, text_to_del, depth)


if __name__ == '__main__':
    main()
