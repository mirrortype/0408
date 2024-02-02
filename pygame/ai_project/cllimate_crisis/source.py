# -*- coding:utf-8 -*-

import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 1600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1600x800 파이게임 화면")

# 추가 이미지 로드 (화면에 꽉 차는 이미지)
full_screen_image = pygame.image.load("pygame/ai_project/cllimate_crisis/image/tatle.png")  # 이미지 경로를 지정하세요
full_screen_image = pygame.transform.scale(full_screen_image, (WIDTH, HEIGHT))

# 배경 이미지 로드
background_image = pygame.image.load("pygame/ai_project/cllimate_crisis/image/sea.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# 첫 번째 추가 이미지 로드 (중앙 위에 위치)
example_image1 = pygame.image.load("pygame/ai_project/cllimate_crisis/image/blue.png")
example_image1 = pygame.transform.scale(example_image1, (1550, 240))

x_position1 = (WIDTH - 1550) // 2
y_position1 = HEIGHT - 260  # 이미지를 약간 위로 이동

# 두 번째 추가 이미지 로드 (화면 오른쪽에 위치)
example_image2 = pygame.image.load("pygame/ai_project/cllimate_crisis/image/SEACAT-removebg-preview.png")
example_image2 = pygame.transform.scale(example_image2, (700, 450))  # 크기 조절
x_position2 = WIDTH - 700  # 오른쪽 끝에서 50px 왼쪽으로
y_position2 = 150  # 화면 상단에서 50px 아래로

# 한글 폰트 설정 (폰트 파일이 프로젝트 디렉토리에 있어야 합니다.)
font_path = "pygame/ai_project/cllimate_crisis/HakgyoansimWoojuR.ttf"  # 여기에 폰트 파일 경로를 지정하세요.
font = pygame.font.Font(font_path, 48)  # 한글 폰트, 크기 48

# 텍스트 리스트
texts = ['흠...', '룰루루.' ,'응? 뭐야 저거.', '아, 아. 지금 눈 뜬 거야? 그런 거야?', '들려? 몸은 좀 어떻고?', '나는 해냥이야!', '응? 여기는...',
         '그야! 망망대해지.', '네가 왜 여기에 있냐고?', '그건 나도 모르지! 나는 물에 빠져 있는 너를 건져올렸을 뿐이야.',
         '그러고 보니!' , '너는 사람이야?', '나! 보다시피 고양이지.', '응? 푸른색 고양이를 몰라?', '헉... 그게 무슨 소리야? 진짜? 정말??',
         '너, 혹시.. 100년동안 심해 속에서 살고 그랬던 거야?', '우리 오셔니야족을 모른다고 말한 거야?', '이런... 안되겠군. 우리를 한 번도 본 적이 없나 봐?',
         '이 몸이 소개해주지!', '윤기가 자르르 흐르는 푸른 털!','영롱하고 산뜻한 자태!', '고양이의 모습을 한!','짜잔~ 우리는 오셔니야족이야!',"'그 날' 이후로 환경에 맞게 적응하게 된 종족이지.",
         "으응? 설마 너 지금,", "'그 날'이 뭔지도 모른다는 건 아니겠지?", "뭐? 정말이야?", "......." , "그래" , '그럴수잇지' "'그 날'." , '해수면이 급격히 상승해버려 마지막 도시까지도 물에 잠기게 된 날이야.',
         '뭐? 왜냐니! 당연히 지구 온난화 때문이지!', '그래서 이렇게 표류생활 하는 거 안 보여?','그래도 그 전에는 거처가 있었는데...', '이제는 없어!', "응, 없어.", "그래서... 거처를 찾고 있지.", '그러던 중에 널 마주친 거고!',
         '새 육지를 찾아야 해.', "아이고, 그 전에 배고파 죽겠네.", "금강산도 식후경이라지!", '일단 밥부터 먹을래?', '아, 근데 문제가 하나 있어!', '밥을...',"'사냥해야 해.'", '그러니까, 물고기를 잡아야 한다구.',
         '바다에는 쓰레기가 많은 건 너도 봐서 알지?', '자! 그물 줄테니까 물고기 한 번 잡아봐.', "쓰레기 안 건지게 조심하고!"]
current_text_index = 0  # 현재 텍스트 인덱스

# 보이지 않게 할 이미지를 표시하는 변수
show_full_screen_image = True

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 키가 눌렸을 때
            if event.key == pygame.K_SPACE:  # 스페이스바를 눌렀을 때
                current_text_index = (current_text_index + 1) % len(texts)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭했을 때
            if show_full_screen_image:
                # 이미지를 클릭하면 보이지 않게 설정
                show_full_screen_image = False
            else:
                current_text_index = (current_text_index + 1) % len(texts)

    # 배경 그리기
    screen.blit(background_image, (0, 0))

    # 두 번째 추가 이미지 그리기 (화면 오른쪽 상단)
    screen.blit(example_image2, (x_position2, y_position2))

    # 첫 번째 추가 이미지 그리기 (중앙 위)
    screen.blit(example_image1, (x_position1, y_position1))


    # 텍스트 렌더링
    text_surface = font.render(texts[current_text_index], True, (255, 255, 255))
    text_rect = text_surface.get_rect(bottomleft=(90, HEIGHT - 160))

    # 텍스트 그리기
    screen.blit(text_surface, text_rect)

    # 추가 이미지 그리기 (화면에 꽉 차는 이미지)
    if show_full_screen_image:
        screen.blit(full_screen_image, (0, 0))

    # 화면 업데이트
    pygame.display.flip()
