with open('1.txt', encoding='utf-8') as f:
    list_file1 = f.readlines()

with open('2.txt', encoding='utf-8') as f:
    list_file2 = f.readlines()

with open('3.txt', encoding='utf-8') as f:
    list_file3 = f.readlines()

full_text = {
len(list_file1):['1.txt',list_file1],
len(list_file2):['2.txt',list_file2],
len(list_file3):['3.txt',list_file3],
}

sorted_text = sorted(full_text.items())
with open('result.txt', "a", encoding='utf-8') as f:
    for v in sorted_text:
        f.write(f'{list(v[1])[0]} \n')
        f.write(f'{str(v[0])} \n')
        for vv in list(v[1])[1]:
            f.write(f'{vv.strip()}\n')