import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1024, 1024)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("다음 이미지로 넘어가기")

# 이미지 파일 리스트
image_paths = ["path/to/image1.jpg", "path/to/image2.jpg", "path/to/image3.jpg"]
images = [pygame.image.load(path) for path in image_paths]
num_images = len(images)

# 현재 이미지 인덱스
current_index = 0

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 시 다음 이미지로 넘어가기
            current_index = (current_index + 1) % num_images

    # 현재 이미지 표시
    screen.blit(images[current_index], (0, 0))

    # 화면 업데이트
    pygame.display.flip()
