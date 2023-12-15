def tlq(word_in):


    wp = []
    words = word_in

    for w in words :
        while True:
            print(w)
            poem = input(" =>")
            if w == poem[0]:
                wp.append(poem)
                break
            else:
                print("첫 번쨰 글자를 잘못 적으셨습니다.")
                continue

    for i in wp:
        print(f"{i[0]} : {i}") 



tlq(input("삼행시를 지을 단어를 입력하세요 :"))

