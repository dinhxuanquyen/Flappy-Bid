import pygame, sys
def draw_floor():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))


pygame.init()
screen= pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
gravity = 0.25
bird_movement = 0
# chèn backgroud
bg = pygame.image.load('assests//background-night.png').convert()
bg = pygame.transform.scale2x(bg)
# chèn sàn
floor = pygame.image.load('assests/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#tạo bird
bird = pygame.image.load('assests/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement =-11
    screen.blit(bg,(0,0))
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird,bird_rect)
    
    floor_x_pos -= 1
    draw_floor()

    if floor_x_pos <= -432:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
