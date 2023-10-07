
try:
  fh=open("helloworld.py",mode="w+" ,encoding="utf-8")
#   writeline("hello world")
  fh.write("hello this is line 1\n")
  fh.write("LINE 2")
  fh.flush()
  fh.close
except  Exception as e:
    print(e)
remaining_lines=["line 3","line4","line5"]
for eachline in remaining_lines:
   fh.write(eachline)



# fh.write("hello this is line 21\n")
# fh.write("LINE 22")
print(vars(fh))
fh.writelines(remaining_lines)
# fh.flush()
fh2=open("helloworld.py",mode="r" ,encoding="utf-8")
# print(vars(fh2))
file_content=fh2.read(100)
print(f"{file_content=}")
fh2.seek(11)
# print(fh2.tell())
file_content2=fh2.read()
print(f"{file_content2=}")
fh2.close
# print(vars(fh2))
# print(fh2.readable())
# print(fh2.writable())
# print(dir(fh))