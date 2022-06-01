import re


def get_js_args(src):
    args = re.findall("[\\[](.+?)[\\]]", src)
    args = list(set(args))
    for arg in args:
        if bool(re.search('[a-z]', arg)):
            args.remove(arg)
            break
    args = str(args[0])
    return args.split(',')


if __name__ == '__main__':
    a = get_js_args(
        """_showDynClickBatch(['dynclicks_u8_6463','dynclicks_u8_6371','dynclicks_u8_6259','dynclicks_u8_6257','dynclicks_u8_6256','dynclicks_u8_6253'],[6463,6371,6259,6257,6256,6253],"wbnews", 1538200623)""")
    for b in a:
        print(b)
