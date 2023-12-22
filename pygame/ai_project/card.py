import pygame
import sys

# pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_SIZE = (800, 800)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("800x800 바탕에 이미지 사용하기")

# 이미지 로드
background_image = pygame.image.load('c:/Users/CODEPLAY_VIVO1/Downloads/christmarrs.png')
background_image = pygame.transform.scale(background_image, SCREEN_SIZE)  # 이미지 크기 조정

# 음악 로드 및 재생
pygame.mixer.music.load('c:/Users/CODEPLAY_VIVO1/Downloads/enchanted-chimes-177906.mp3')
pygame.mixer.music.play(-1)  # -1은 음악을 무한 반복 재생하라는 의미


# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 화면에 이미지 그리기
    screen.blit(background_image, (0, 0))

    # 화면 업데이트
    pygame.display.flip()

    # 초당 프레임 수 설정 (여기서는 60FPS)
    pygame.time.Clock().tick(60)

