from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return
    '''
    absolute path
    /usr/lib/../bin/./gcc
    stack = [usr, bin, gcc]
    - .. -> pop if stack isn't empty
    - .. -> if top equals ".", continue
    - . -> don't do anything -> continue
    - if empty -> continue

    relative path
    ./../../hi/../
    stack = [.., ]
    - .. -> if stack is empty, append it
    - .. -> if top of stack has .., append.
    - .. -> else, pop from stack
    '''
    isAbsolutePath = path[0] == "/"
    stack = []
    tokens = filter(lambda token: not (token == "" or token == "."), path.split("/"))
    if isAbsolutePath:
        stack.append("/")
    for token in tokens:
        if token == "..":
            if not stack or stack[-1] == "..":
                stack.append("..")
            else:
                stack.pop()
        else:
            stack.append(token)
    res = "/".join(stack)
    return res[res.startswith('//'):]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
