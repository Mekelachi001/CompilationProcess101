import sys
def __start__(path):
    file =open("code.asm","w")
    file.write("global _start\n")
    
    file.write("_start:\n")
    file.write("section .data\n")
    with open(path, 'r') as code:
        for lines in code:
            pass
    file.write("section .bss\n")
    with open(path, 'r') as code:
        for lines in code:
            if "int" in lines:
                for x in range(len(lines)):
                    if lines[x] == ' ':
                        break 
                for g in range(len(lines)):
                    if lines[g] == ';':
                        break

    file.write("section .text\n")
    with open(path, 'r') as code:
        for lines in code:
            if "show" in lines:
                # for a in range()
                for x in range(len(lines)):
                    if lines[x] == "(":
                        break
                for b in range(len(lines)):
                    if lines[b] == ")":
                        break
                
                text = lines[x+1:b]
                file.write("\n; Write a value to screen\n")
                file.write("\t mov eax, 4\n")
                file.write("\t mov ebx, 1\n")
                file.write(f"\t mov ecx, {text}\n")
                file.write(f"\t mov edx, {len(text)-2}\n")
                file.write(f"\t int 80h\n\n\n")
            elif "end" in lines:
                file.write("\t; Exit \n")
                file.write("\t mov eax, 1\n")
                file.write("\t mov ebx, 0\n")
                file.write(f"\t int 80h\n\n\n")
        
    
    file.close()
                



if __name__ == '__main__':
    _path_ =  sys.argv[1]
    __start__(_path_)