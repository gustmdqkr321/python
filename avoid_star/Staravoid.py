import pygame, random, sys
from pygame.locals import *
from Object import Object

WINDOWWIDTH = 700
WINDOWHEIGHT = 800
TEXTCOLOR = (255, 255, 150)
temp = pygame.image.load("/home/user/PycharmProjects/StarAvoid/avoid/BackGround.jpeg")
BACKGROUND = pygame.image.load("/home/user/PycharmProjects/StarAvoid/avoid/BackGround.jpeg")
BACKGROUND2 = pygame.image.load("/home/user/PycharmProjects/StarAvoid/avoid/background2.png")
BACKGROUNDSMALL = pygame.image.load("/home/user/PycharmProjects/StarAvoid/avoid/Small22.jpeg")
BACKGROUND2SMALL = pygame.image.load("/home/user/PycharmProjects/StarAvoid/avoid/background2small.png")
FPS = 40
STARMINSIZE = 10
STARMAXSIZE = 40
STARMINSPEED = 1
STARMAXSPEED = 8
ADDNEWSTARRATE = 8
ADDNEWSTARRATELEVEL = [5, 12, 24]
ADDNEWHEARTRATE = 300
PLAYERMOVERATE = 5
FULL_HITPOINT = 4
FULL_Skill = 200
FULL_SkillLevel = [200, 400, 600]


def terminate():
    pygame.quit()
    sys.exit()


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def waitStart():
    global BACKGROUND
    global BACKGROUND2
    global temp
    global ADDNEWSTARRATE
    global ADDNEWSTARRATELEVEL
    global FULL_Skill
    global FULL_SkillLevel
    global player1
    global player2
    global playerImageSelect
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:  # ESC 키를 눌러 종료한다
                    terminate()
                elif event.key == pygame.K_1:
                    BACKGROUND = temp
                elif event.key == pygame.K_2:
                    BACKGROUND = BACKGROUND2
                elif event.key == pygame.K_e:
                    ADDNEWSTARRATE = ADDNEWSTARRATELEVEL[2]
                    FULL_Skill = FULL_SkillLevel[0]
                elif event.key == pygame.K_n:
                    ADDNEWSTARRATE = ADDNEWSTARRATELEVEL[1]
                    FULL_Skill = FULL_SkillLevel[1]
                elif event.key == pygame.K_h:
                    ADDNEWSTARRATE = ADDNEWSTARRATELEVEL[0]
                    FULL_Skill = FULL_SkillLevel[2]
                elif event.key == pygame.K_l:
                    playerImageSelect = player1
                elif event.key == pygame.K_r:
                    playerImageSelect = player2
                return


# Pygame, 윈도우, 마우스 커서를 설정한다.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.mouse.set_visible(False)

# 폰트를 설정한다.
font = pygame.font.SysFont(None, 48)

# 사운드를 설정한다.
SkillSound = pygame.mixer.Sound(
    '/home/user/PycharmProjects/StarAvoid/avoid/SkillSound (online-audio-converter.com).wav')
HeartGetSound = pygame.mixer.Sound("/home/user/PycharmProjects/StarAvoid/avoid/HeartGetsound.wav")
GameMusic = pygame.mixer.Sound("/home/user/PycharmProjects/StarAvoid/avoid/GameMusic.wav")
FirstMusic = pygame.mixer.Sound("/home/user/PycharmProjects/StarAvoid/avoid/FirstMusic.wav")

# 이미지를 설정한다.
playerImage = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/People1.png')
playerImageSelect = None
playerRect = playerImage.get_rect()
playerImage1 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/People1.png')
playerImage2 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/People2.png')
playerImage3 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/People3.png')
playerImage4 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/People4.png')
playerImage5 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/forward.png')
playerImage6 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/back.png')
playerImage7 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/left.png')
playerImage8 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/right.png')
player1 = [playerImage1, playerImage2, playerImage3, playerImage4]
player2 = [playerImage5, playerImage6, playerImage7, playerImage8]
starImage = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/star.png')
moonImage1 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/moon1.png')
moonImage2 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/moon2.png')
moonImage3 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/moon3.png')
moonImage4 = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/moon4.png')
heartImage = pygame.image.load('/home/user/PycharmProjects/StarAvoid/avoid/Heart.png')

# "Start" 화면을 보여준다.
FirstMusic.play()
windowSurface.fill([0, 0, 0])
windowSurface.blit(BACKGROUNDSMALL, pygame.Rect(100, 375, 0, 0))
windowSurface.blit(BACKGROUND2SMALL, pygame.Rect(400, 400, 0, 0))
drawText('Avoid Star !!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press 1 or 2 choice BackGround', font, windowSurface, (WINDOWWIDTH / 8), (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitStart()
topScore = 0

# 난이도 선택 화면
windowSurface.fill([0, 0, 0])
drawText('Select Level E or N or H', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 3))
pygame.display.update()
waitStart()

# 캐릭터 선택 화면
windowSurface.fill([0, 0, 0])
drawText('Select Character L or R', font, windowSurface, (WINDOWWIDTH / 5), (WINDOWHEIGHT / 3))
pygame.display.update()
windowSurface.blit(playerImage1, pygame.Rect(200, 400, 0, 0))
windowSurface.blit(playerImage5, pygame.Rect(400, 390, 0, 0))
pygame.display.update()
waitStart()
FirstMusic.stop()

while True:
    # 게임의 시작 부분을 설정한다.
    GameMusic.play()
    star = []
    heart = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    game = False
    starAddCounter = 0
    heartAddCounter = 7
    hitPoint = FULL_HITPOINT
    SkillTimer = 0

    while True:  # 게임 부분을 수행하는 동안 게임 루프를 반복한다.
        score += 1  # 점수를 증가시킨다.
        if SkillTimer < FULL_Skill:
            SkillTimer += 1  # 스킬 게이지를 감소시킨다.
        for event in pygame.event.get():
            # 키 입력에 반응한다.
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == ord('q'):  # 키 입력에 반응하여 모든 별을 삭제
                    if SkillTimer == FULL_Skill:
                        SkillSound.play()
                        for b in star[:]:
                            star.remove(b)
                            SkillTimer = 0
                else:

                    if event.key == K_LEFT or event.key == ord('a'):
                        moveRight = False
                        moveLeft = True
                        playerImage = playerImageSelect[2]
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveLeft = False
                        moveRight = True
                        playerImage = playerImageSelect[3]
                    if event.key == K_UP or event.key == ord('w'):
                        moveDown = False
                        moveUp = True
                        playerImage = playerImageSelect[1]
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveUp = False
                        moveDown = True
                        playerImage = playerImageSelect[0]

            if event.type == KEYUP:

                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

        # 필요하면 화면 상단에 별과 하트를 새로 추가한다.
        if not game:
            starAddCounter += 1
            heartAddCounter += 1
        if starAddCounter == ADDNEWSTARRATE:
            starAddCounter = 0
            starSize = random.randint(STARMINSIZE, STARMAXSIZE)
            newstar = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - starSize), 0 - starSize, starSize,
                                           starSize),
                       'speed': random.randint(STARMINSPEED, STARMAXSPEED),
                       'surface': pygame.transform.scale(starImage, (starSize, starSize)),
                       }
            star.append(newstar)
        if heartAddCounter == ADDNEWHEARTRATE:
            heartAddCounter = 0
            heartSize = (40)
            newheart = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH - heartSize), 0 - heartSize, heartSize,
                                            heartSize),
                        'speed': (8),
                        'surface': pygame.transform.scale(heartImage, (heartSize, heartSize)),
                        }
            heart.append(newheart)
        # 플레이어를 움직인다.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)
        # 별을 아래로 내린다.
        for b in star:
            if not game:
                b['rect'].move_ip(0, b['speed'])
        # 바닥을 지나친 별은 삭제한다.
        for b in star[:]:
            if b['rect'].top > WINDOWHEIGHT:
                star.remove(b)
        # 하트를 아래로 내린다.
        for b in heart:
            if not game:
                b['rect'].move_ip(0, b['speed'])
        # 바닥을 지나친 하트 삭제한다.
        for b in heart[:]:
            if b['rect'].top > WINDOWHEIGHT:
                heart.remove(b)
        # 윈도우에 게임 월드를 그린다
        windowSurface.blit(BACKGROUND, (0, 0))
        # 점수와 탑스코어를 그린다.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)
        # 스킬 쿨 타임, HP을 그린다.
        drawText('Skill gauge: %s' % (SkillTimer), font, windowSurface, 10, 80)
        drawText('HP: %s' % (str(hitPoint)), font, windowSurface, 10, 120)

        # 플레이어 사각형을 그린다.
        windowSurface.blit(playerImage, playerRect)
        # HP에 따라 달의 다른 모양을 그린다.
        if hitPoint == 4:
            windowSurface.blit(moonImage4, (WINDOWWIDTH - 40, 40))
        elif hitPoint == 3:
            windowSurface.blit(moonImage3, (WINDOWWIDTH - 40, 40))
        elif hitPoint == 2:
            windowSurface.blit(moonImage2, (WINDOWWIDTH - 40, 40))
        elif hitPoint == 1:
            windowSurface.blit(moonImage1, (WINDOWWIDTH - 40, 40))
        # 별을 그린다.
        for b in star:
            windowSurface.blit(b['surface'], b['rect'])
        pygame.display.update()
        # 하트를 그린다
        for b in heart:
            windowSurface.blit(b['surface'], b['rect'])
        pygame.display.update()
        # 플레이어와 부딪힌 별이 있는지 검사한다.
        if Object.playerHasHitStar(playerRect, star):
            hitPoint -= 1
            if hitPoint == 0:
                pygame.display.update()
                if score > topScore:
                    topScore = score  # 탑스코어를 새로 설정한다.
                break
        elif Object.playerHasHitHeart(playerRect, heart):
            HeartGetSound.play()
            if hitPoint == 4:
                pass
            else:
                hitPoint += 1
        mainClock.tick(FPS)
    # 게임을 멈추고 'Game Over' 화면을 보여준다.
    GameMusic.stop()
    pygame.mixer.music.stop()
    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitStart()