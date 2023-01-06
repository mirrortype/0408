f = open("test.txt", "w", encoding = "UTF-8")
# 파일을 새로 만들거나, 있는 파일을 새로 덮어쓸 때는 "w"
# 기존 파일에서 내용을 덧붙일 때는 "a"
# 기존 파일에서 내용을 읽어오기만 할 때는 "r"

f.write("바부"+"\n")
f.write("바부"+"\n")
f.write("바부"+"\n")
# w나, a로 파일에 쓰기가 가능할 때 wirte 매서드로 내용을 적을 수 있음.
f.close()

f = open("test.txt", "r", encoding = "UTF-8")

line = f.readline()
lines = f.readlines()
print(line)
print(lines)

f.close()
# 불러온 파일을 닫아줌

