

def adv_print(*text, start='', max_line=None, in_file=None):
    print(start)
    for text in text:
        if max_line is None:
                print(i)
        else:
            def chunks(text_s):
                for start in range(0, len(text_s), max_line):
                    yield text_s[start:start+max_line]
            if in_file is not None:
                file = open('text.txt', 'a', encoding="utf-8")
                file.writelines(str(start))
                file.writelines('\n')
            for chunk in chunks(text):
                print(chunk)
                file.writelines(chunk)
                file.writelines('\n')
        if max_line is None and in_file is not None:
            file = open('text.txt', 'a', encoding="utf-8")
            file.writelines(str(start))
            file.writelines('\n')
            file.writelines(text)
            file.writelines('\n')


adv_print('Нааа', 'вапвапв','sdfgsdfgsdfg','dfgdfgdfgd', in_file= 1, max_line= 5,)
