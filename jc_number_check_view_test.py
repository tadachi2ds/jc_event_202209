import pygame
import sys
import os
# import yaml
import argparse

image_dir = ""

def set_parameter() :
    # 最終的には、argparse にする
    prm = {
        'width'     : 1920,
        'height'    : 1080,
        'team_num'  : 16
    }
    return prm


def load_image(file, width = 0, height = 0):
    # file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)

        if width > 0 and height > 0 :
            surface = pygame.transform.scale(surface, (width, height))

    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    # return surface.convert()
    return surface


def screen_object_setting() :
    screen_obj = {
        'bg' : {
            'img' : load_image("img/N_BackGrand_1920_1080.png")
        },
        'team' : {
            'imgs' : [ load_image("img/N_9_256_340.png", 150, 250) ],

        },
        'num1' : {
            'imgs'  : [ load_image("img/N_1.png") ],
            'btn'   : {
                'up' : {
                    'img'    :  load_image("img/N_Button_Up.png"),
                    'x' : 0,
                    'y' : 0
                }, 
                'down' : {
                    'img'    :  load_image("img/N_Button_Down.png"),
                    'x' : 0,
                    'y' : 0
                }, 
            }
        },



    }


    btn_up0 = load_image("img/N_Button_Up.png", 80, 80)
    btn_up1 = load_image("img/N_Button_Up.png")
    btn_up2 = load_image("img/N_Button_Up.png")
    btn_up3 = load_image("img/N_Button_Up.png")
    btn_dwn0 = load_image("img/N_Button_Down.png", 80, 80)
    btn_dwn1 = load_image("img/N_Button_Down.png")
    btn_dwn2 = load_image("img/N_Button_Down.png")
    btn_dwn3 = load_image("img/N_Button_Down.png")
    btn_sbmt = load_image("img/N_Button_AnswerCheck_Normal_850_180.png")

    btn_up_y = 100
    btn_dwn_y = 700
    num_y = 300

    team_x = 350
    num1_x = 700
    num2_x = 1000
    num3_x = 1300
    team_adg_x = 35
    team_adg_up_y = 150
    team_adg_down_y = 80
    btn_adg = 50

    font = pygame.font.Font('img/CICA-REGULAR.TTF', 60) 

    return screen_obj


def screen_object_draw() :
    pass


# ----------------------------------------------------
# メイン
# ----------------------------------------------------
def main() :
    # menber_list = parse_member_list()
    prm = set_parameter()

    # 初期座標設定
    # width, height = 1920, 1080
    width, height = 7400, 6400
    # team = button_set()
    # num1 = button_set()
    # num2 = button_set()
    # num3 = button_set()


    pygame.init()
    screen = pygame.display.set_mode((prm['width'], prm['height']), pygame.FULLSCREEN, 32) 
    pygame.display.set_caption("NumberCheck") 

    # screen_object_setting()

    bg_img = load_image("img/N_BackGrand_1920_1080.png")

    team = load_image("img/N_9_256_340.png", 150, 250)    
    num1 = load_image("img/N_1.png")
    num2 = load_image("img/N_1.png")
    num3 = load_image("img/N_1.png")
    
    btn_up0 = load_image("img/N_Button_Up.png", 80, 80)
    btn_up1 = load_image("img/N_Button_Up.png")
    btn_up2 = load_image("img/N_Button_Up.png")
    btn_up3 = load_image("img/N_Button_Up.png")
    btn_dwn0 = load_image("img/N_Button_Down.png", 80, 80)
    btn_dwn1 = load_image("img/N_Button_Down.png")
    btn_dwn2 = load_image("img/N_Button_Down.png")
    btn_dwn3 = load_image("img/N_Button_Down.png")
    btn_sbmt = load_image("img/N_Button_AnswerCheck_Normal_850_180.png")

    btn_up_y = 100
    btn_dwn_y = 700
    num_y = 300

    team_x = 350
    num1_x = 700
    num2_x = 1000
    num3_x = 1300
    team_adg_x = 35
    team_adg_up_y = 150
    team_adg_down_y = 80
    btn_adg = 50

    font = pygame.font.Font('img/CICA-REGULAR.TTF', 60) 



    fullscreen_flg = True
    running = True
    while running :
        pygame.time.wait(30)

        # screen_object_draw()
        # screen.fill((0, 20, 0, 0))
        screen.blit(bg_img, (0,0))

        screen.blit(team, (team_x, num_y + 50))
        screen.blit(num1, (num1_x, num_y))
        screen.blit(num2, (num2_x, num_y))
        screen.blit(num3, (num3_x, num_y))
        screen.blit(btn_up0, (team_x + team_adg_x, btn_up_y + team_adg_up_y ))
        screen.blit(btn_up1, (num1_x + btn_adg, btn_up_y))
        screen.blit(btn_up2, (num2_x + btn_adg, btn_up_y))
        screen.blit(btn_up3, (num3_x + btn_adg, btn_up_y))
        screen.blit(btn_dwn0, (team_x + team_adg_x, btn_dwn_y - team_adg_down_y))
        screen.blit(btn_dwn1, (num1_x + btn_adg, btn_dwn_y))
        screen.blit(btn_dwn2, (num2_x + btn_adg, btn_dwn_y))
        screen.blit(btn_dwn3, (num3_x + btn_adg, btn_dwn_y))
        screen.blit(btn_sbmt, (600, 900))

        pygame.draw.rect(screen, (0,0,0), (280,180,300,600), width = 10)
        pygame.draw.rect(screen, (0,0,0), (280,130,300,100), width = 0)
        team_text = font.render("チーム名", True, (255,255,255)) 
        screen.blit(team_text, [300, 160])

        for event in pygame.event.get():
             # 終了用のイベント処理
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                kamerobo_x_change, kamerobo_y_change = 0, 0

            # キー入力のイベント処理
            if event.type == pygame.KEYDOWN:
                 # ESCキー：終了用のイベント処理
                if event.key == pygame.K_ESCAPE : 
                    running = False

                if event.key == pygame.K_F2:
                    # F2キーでフルスクリーンモードへの切り替え
                    fullscreen_flg = not fullscreen_flg
                    if fullscreen_flg:
                        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32) 
                    else:
                        screen = pygame.display.set_mode((width, height), 0, 32) 






        pygame.display.update()


if __name__ == '__main__' :
    main()       

