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
    # 共通座標
    btn_up_y = 100
    btn_dwn_y = 700
    num_y = 300

    team_x = 350
    num1_x = 700
    num2_x = 1000
    num3_x = 1300
    team_adg_x = 35
    team_adg_y = 250    
    team_adg_up_y = 150
    team_adg_down_y = 80
    btn_adg = 50
    sbm_x = 600
    sbm_y = 900

    screen_obj = {
        'bg' : {
            'img' : load_image("img/N_BackGrand_1920_1080.png")
        },
        'team' : {
            'img'   : {
                'imgs' : [ load_image("img/N_9_256_340.png", 150, 250) ],
                'x' : team_x,
                'y' : btn_up_y + team_adg_y
            },
            'btn'   : {
                'up' : {
                    'img'    :  load_image("img/N_Button_Up.png", 80, 80),
                    'x' : team_x + team_adg_x,
                    'y' : btn_up_y + team_adg_up_y 
                }, 
                'down' : {
                    'img'    :  load_image("img/N_Button_Down.png", 80, 80),
                    'x' : team_x + team_adg_x,
                    'y' : btn_dwn_y - team_adg_down_y
                }, 
            }
        },
        'num1' : {
            'img'   : {
                'imgs'  : [ load_image("img/N_1.png") ],
                'x'     : num1_x,
                'y'     : num_y 
            },
            'btn'   : {
                'up' : {
                    'img'    :  load_image("img/N_Button_Up.png"),
                    'x' : num1_x + btn_adg,
                    'y' : btn_up_y
                }, 
                'down' : {
                    'img'    :  load_image("img/N_Button_Down.png"),
                    'x' : num1_x + btn_adg,
                    'y' : btn_dwn_y 
                }, 
            }
        },
        'num2' : {
            'img'   : {
                'imgs'  : [ load_image("img/N_1.png") ],
                'x'     : num2_x,
                'y'     : num_y 
            },

            'btn'   : {
                'up' : {
                    'img'    :  load_image("img/N_Button_Up.png"),
                    'x' : num2_x + btn_adg,
                    'y' : btn_up_y
                }, 
                'down' : {
                    'img'    :  load_image("img/N_Button_Down.png"),
                    'x' : num2_x + btn_adg,
                    'y' : btn_dwn_y
                }, 
            }
        },
        'num3' : {
            'img'   : {
                'imgs'  : [ load_image("img/N_1.png") ],
                'x'     : num3_x,
                'y'     : num_y 
            },
            'btn'   : {
                'up' : {
                    'img'    :  load_image("img/N_Button_Up.png"),
                    'x' : num3_x + btn_adg,
                    'y' : btn_up_y
                }, 
                'down' : {
                    'img'    :  load_image("img/N_Button_Down.png"),
                    'x' : num3_x + btn_adg,
                    'y' : btn_dwn_y 
                }, 
            }
        },
        'submit' : {
            'btn'   : {
                'img'    :  load_image("img/N_Button_AnswerCheck_Normal_850_180.png"),
                'x' :   sbm_x,
                'y' :   sbm_y
            }
        }


    }



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


def screen_object_draw(screen, screen_obj) :
    screen.blit(screen_obj['bg']['img'], (0,0))

    screen.blit(screen_obj['team']['img']['imgs'][0], (screen_obj['team']['img']['x'], screen_obj['team']['img']['y']))
    screen.blit(screen_obj['num1']['img']['imgs'][0], (screen_obj['num1']['img']['x'], screen_obj['num1']['img']['y']))
    screen.blit(screen_obj['num2']['img']['imgs'][0], (screen_obj['num2']['img']['x'], screen_obj['num2']['img']['y']))
    screen.blit(screen_obj['num3']['img']['imgs'][0], (screen_obj['num3']['img']['x'], screen_obj['num3']['img']['y']))

    screen.blit(screen_obj['team']['btn']['up']['img'], (screen_obj['team']['btn']['up']['x'], screen_obj['team']['btn']['up']['y']))
    screen.blit(screen_obj['num1']['btn']['up']['img'], (screen_obj['num1']['btn']['up']['x'], screen_obj['num1']['btn']['up']['y']))
    screen.blit(screen_obj['num2']['btn']['up']['img'], (screen_obj['num2']['btn']['up']['x'], screen_obj['num2']['btn']['up']['y']))
    screen.blit(screen_obj['num3']['btn']['up']['img'], (screen_obj['num3']['btn']['up']['x'], screen_obj['num3']['btn']['up']['y']))

    screen.blit(screen_obj['team']['btn']['down']['img'], (screen_obj['team']['btn']['down']['x'], screen_obj['team']['btn']['down']['y']))
    screen.blit(screen_obj['num1']['btn']['down']['img'], (screen_obj['num1']['btn']['down']['x'], screen_obj['num1']['btn']['down']['y']))
    screen.blit(screen_obj['num2']['btn']['down']['img'], (screen_obj['num2']['btn']['down']['x'], screen_obj['num2']['btn']['down']['y']))
    screen.blit(screen_obj['num3']['btn']['down']['img'], (screen_obj['num3']['btn']['down']['x'], screen_obj['num3']['btn']['down']['y']))

    screen.blit(screen_obj['submit']['btn']['img'], (screen_obj['submit']['btn']['x'], screen_obj['submit']['btn']['y']))


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

    screen_obj = screen_object_setting()

    font = pygame.font.Font('img/CICA-REGULAR.TTF', 60) 

    fullscreen_flg = True
    running = True
    while running :
        pygame.time.wait(30)

        screen_object_draw(screen, screen_obj)

        # screen.fill((0, 20, 0, 0))
        # チーム名用の枠
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

