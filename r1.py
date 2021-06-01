# 寫讀取檔案 function，read_file()， append()讀取
# 寫 main function，main()
# 文字檔內容讀取有怪符號，可用 encoding = 'utf-8-sig'
# 去除換行符號\n，使用 strip()
# 寫 conver function，人名+:+對話紀錄
# None 無值
# 寫入檔案 function，wite_file()， write()寫入

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person == 'Tom'
            continue
        
        if person:
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output_r1.txt', lines)

main()