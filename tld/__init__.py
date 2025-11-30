from tldextract.tldextract import TLD_EXTRACTOR

all_items = TLD_EXTRACTOR.tlds


def get_full_info():
    result = {}
    for item in all_items:
        count = item.count('.')
        if count not in result:
            result[count] = []
        result[count].append(item)
    return {k: sorted(v) for k, v in result.items()}


def get_lines(full=True, sep=False):
    result = ''
    info = get_full_info()
    for k in sorted(info):
        if not full and k == 0:
            continue
        if sep and result:
            result += '\n'
        for item in info[k]:
            if result:
                result += '\n' + item
            else:
                result += item
    return result
