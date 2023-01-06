

#단어입력

def word_in():
    kor = open("wordKor.txt", "a", encoding = "UTF-8")
    eng = open("wordEng.txt", "a", encoding = "UTF-8")

    while True:
        kor_in = input("한글뜻을 입력하세요 (입력종료 : 꺼져) : ")
        if kor_in == "꺼져":
            break
        else:
            kor.write(kor_in + "\n")
        eng_in = input("영어뜻을 입력하세요 (입력종료 : 꺼져) : ")
        if eng_in == "꺼져":
            break
        else:
            eng.write(eng_in + "\n")
    kor.close()
    eng.close()

#단어출력
def eng_exam():
    kor = open("wordKor.txt", "r", encoding = "UTF-8")
    eng = open("wordEng.txt", "r", encoding = "UTF-8")

    kor_Q = kor.readlines()
    eng_A = eng.readlines()
    score = 0

    for i in range(len(kor_Q)):
        answer = input(f"{kor_Q[i].strip()}의 영어단어를 쓰시오 (종료 : 꺼져) : ")
        if answer == "꺼져":
            break
        elif answer == eng_A[i].strip():
            print("정답입니다!")
            score += 1
        else:
            print(f"틀렸습니다. 정답 : {eng_A[i].strip()}")

    print("수고하셨습ㅣ다.")
    print(f"{len(kor_Q)}문제중 {score}문제를 맞추셨습니다.")
    kor.close()
    eng.close()


while True:
    selct = int(input("1. 단어입력 / 2.단어시험 / 3.종료 "))
    if selct == 1:
        word_in()
    elif selct == 2:
        eng_exam()
    elif selct == 3:
        break
    else:
        print("잘못 입력하셨스빈다.")