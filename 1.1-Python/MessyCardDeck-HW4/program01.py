def most_frequent_chars(filename: str) -> str:
    return wordlist_to_count(files_to_wordlist(filename))

# def files_to_wordlist(filename):
#     w_list = []
#     nxname = filename
#     while True:
#         curr_list = []
#         opened = open(nxname, 'r', encoding="utf-8")
#         curr_list.extend(opened.read().split())
#         nxname = curr_list.pop(0)
#         w_list.extend(curr_list)
#         if nxname == filename:
#             break
#     return w_list

def files_to_wordlist(filename):
    content = ''
    nxname = filename
    while True:
        with open(nxname, 'r', encoding="utf-8") as file:
            nxname = file.readline().split()[0]
            content += file.read()
        if nxname == filename:
            break
    return content.split()

def wordlist_to_count(w_list):
    final = []
    counts = [{} for x in range(max(len(w) for w in w_list))]
    for word in w_list:
        for i, c in enumerate(word):
                counts[i][c] = counts[i].get(c, 0) + 1

    for count in counts:
        max_value = max(count.items(), key=lambda x: x[1])[1]
        key_list = [k for k, v in count.items() if v == max_value]
        final.append(min(key_list))
    return ''.join(final)
