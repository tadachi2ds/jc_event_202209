import pygame
import sys
import os
# import yaml
# import argparse

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
    msg_x = 600
    msg_y = 900

    screen_obj = {
        'bg' : {
            'img' : load_image("img/N_BackGrand_1920_1080.png")
        },
        'team' : {
            'img'   : {
                'imgs'  : [ load_image("img/N_0_256_340.png", 150, 250),
                            load_image("img/N_1.png", 150, 250), 
                            load_image("img/N_2_256_340.png", 150, 250), 
                            load_image("img/N_3_256_340.png", 150, 250), 
                            load_image("img/N_4_256_340.png", 150, 250), 
                            load_image("img/N_5_256_340.png", 150, 250), 
                            load_image("img/N_6_256_340.png", 150, 250), 
                            load_image("img/N_7_256_340.png", 150, 250), 
                            load_image("img/N_8_256_340.png", 150, 250), 
                            load_image("img/N_9_256_340.png", 150, 250),
                            load_image("img/N_0_256_340.png", 150, 250),
                            load_image("img/N_1.png", 150, 250), 
                            load_image("img/N_2_256_340.png", 150, 250), 
                            load_image("img/N_3_256_340.png", 150, 250), 
                            load_image("img/N_4_256_340.png", 150, 250), 
                            load_image("img/N_5_256_340.png", 150, 250), 
                        ],
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
                'imgs'  : [ load_image("img/N_0_256_340.png"),
                            load_image("img/N_1.png"), 
                            load_image("img/N_2_256_340.png"), 
                            load_image("img/N_3_256_340.png"), 
                            load_image("img/N_4_256_340.png"), 
                            load_image("img/N_5_256_340.png"), 
                            load_image("img/N_6_256_340.png"), 
                            load_image("img/N_7_256_340.png"), 
                            load_image("img/N_8_256_340.png"), 
                            load_image("img/N_9_256_340.png")
                        ],
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
                'imgs'  : [ load_image("img/N_0_256_340.png"),
                            load_image("img/N_1.png"), 
                            load_image("img/N_2_256_340.png"), 
                            load_image("img/N_3_256_340.png"), 
                            load_image("img/N_4_256_340.png"), 
                            load_image("img/N_5_256_340.png"), 
                            load_image("img/N_6_256_340.png"), 
                            load_image("img/N_7_256_340.png"), 
                            load_image("img/N_8_256_340.png"), 
                            load_image("img/N_9_256_340.png")
                        ],
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
                'imgs'  : [ load_image("img/N_0_256_340.png"),
                            load_image("img/N_1.png"), 
                            load_image("img/N_2_256_340.png"), 
                            load_image("img/N_3_256_340.png"), 
                            load_image("img/N_4_256_340.png"), 
                            load_image("img/N_5_256_340.png"), 
                            load_image("img/N_6_256_340.png"), 
                            load_image("img/N_7_256_340.png"), 
                            load_image("img/N_8_256_340.png"), 
                            load_image("img/N_9_256_340.png")
                        ],
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
            },
            'waiting' :{
                'img'    :  load_image("img/connectin_bar.gif"),
                'x' :   sbm_x,
                'y' :   sbm_y
            }
        },
        'success' : {
            'img'    :  load_image("img/N_Win_1920_1080.png"),
        },
        'wrong' : {
            'img'    :  load_image("img/N_WrongAnswer_1920_1080.png"),
        }
    }

    return screen_obj


def screen_object_draw(screen, font, scrn_obj, idx, submit_flg) :
    obj_list = ['team', 'num1', 'num2', 'num3' ]
    scrn_obj_rect = { obj : {'up' : None, 'down' : None}  for obj in obj_list }
    idx_max = {
        'team' : 16, 
        'num1' : 10, 
        'num2' : 10, 
        'num3' : 10
    }

    if submit_flg :
        submit_process(screen, scrn_obj, idx)
        submit_flg = False
    else :


        # 背景描画
        screen.blit(scrn_obj['bg']['img'], (0,0))

        # print(scrn_obj_rect )

        for obj in obj_list :
            # インデックスの調整
            if idx[obj] > len(scrn_obj[obj]['img']['imgs']) :
                idx[obj] = idx[obj] - idx_max[obj]
            elif idx[obj] < 0 :
                idx[obj] = idx[obj] + idx_max[obj]

            idx[obj] = idx[obj] % idx_max[obj]

            screen.blit(scrn_obj[obj]['img']['imgs'][idx[obj]], (scrn_obj[obj]['img']['x'],         scrn_obj[obj]['img']['y']))
            screen.blit(scrn_obj[obj]['btn']['up']['img'],      (scrn_obj[obj]['btn']['up']['x'],   scrn_obj[obj]['btn']['up']['y']))
            screen.blit(scrn_obj[obj]['btn']['down']['img'],    (scrn_obj[obj]['btn']['down']['x'], scrn_obj[obj]['btn']['down']['y']))

            scrn_obj_rect[obj]['up'] = scrn_obj[obj]['btn']['up']['img'].get_rect()
            scrn_obj_rect[obj]['up'].topleft = (scrn_obj[obj]['btn']['up']['x'],   scrn_obj[obj]['btn']['up']['y'])

            scrn_obj_rect[obj]['down'] = scrn_obj[obj]['btn']['down']['img'].get_rect()
            scrn_obj_rect[obj]['down'].topleft = (scrn_obj[obj]['btn']['down']['x'], scrn_obj[obj]['btn']['down']['y'])


        # サブミットボタン設定
        screen.blit(scrn_obj['submit']['btn']['img'], (scrn_obj['submit']['btn']['x'], scrn_obj['submit']['btn']['y']))
        scrn_obj_rect['submit'] = scrn_obj['submit']['btn']['img'].get_rect()
        scrn_obj_rect['submit'].topleft = (scrn_obj['submit']['btn']['x'], scrn_obj['submit']['btn']['y'])

        # チーム名用の枠
        pygame.draw.rect(screen, (0,0,0), (280,180,300,600), width = 10)
        pygame.draw.rect(screen, (0,0,0), (280,130,300,100), width = 0)
        team_text = font.render("チーム名", True, (255,255,255)) 
        screen.blit(team_text, [300, 160])

    return scrn_obj_rect, submit_flg


def submit_process(screen, scrn_obj, idx) :
    screen.blit(scrn_obj['submit']['waiting']['img'], (0,0))
    pygame.time.wait(1000)


    if idx['num1'] == 1 and idx['num2'] == 1 and idx['num3'] == 1 :
        screen.blit(scrn_obj['success']['img'], (0,0))
        # タイマー ＆ 音
        pygame.time.wait(3000)

    else :
        screen.blit(scrn_obj['wrong']['img'], (0,0))
        # タイマー ＆ 音
        pygame.time.wait(3000)


# ----------------------------------------------------
# メイン
# ----------------------------------------------------
def main() :
    # menber_list = parse_member_list()
    prm = set_parameter()

    # 初期座標設定
    # width, height = 1920, 1080
    width, height = 740, 640

    pygame.init()
    screen = pygame.display.set_mode((prm['width'], prm['height']), pygame.FULLSCREEN, 32) 
    pygame.display.set_caption("NumberCheck") 

    pygame.mixer.init() #初期化
    pygame.mixer.music.load("img/N_gacya.mp3") #読み込み

    scrn_obj = screen_object_setting()

    font = pygame.font.Font('img/CICA-REGULAR.TTF', 60) 

    idx = { 'team' : 1 , 'num1' : 1, 'num2' : 1, 'num3' : 1  }
    fullscreen_flg = True
    submit_flg = False
    running = True
    while running :
        pygame.time.wait(30)

        for event in pygame.event.get():
             # 終了用のイベント処理
            if event.type == pygame.QUIT:
                running = False

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

            # マウスクリックのイベント処理
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 変更パネル部分
                for obj in scrn_obj_rect.keys() :
                    if obj in idx.keys() :
                        if scrn_obj_rect[obj]['up'].collidepoint(event.pos):
                            pygame.mixer.music.play(1)
                            idx[obj] += 1
                        elif scrn_obj_rect[obj]['down'].collidepoint(event.pos):
                            pygame.mixer.music.play(1)
                            idx[obj] -= 1

                # submitボタン処理
                if scrn_obj_rect['submit'].collidepoint(event.pos):
                    pygame.mixer.music.play(1)
                    submit_flg = True

        scrn_obj_rect, submit_flg = screen_object_draw(screen, font, scrn_obj, idx, submit_flg)

        # screen.fill((0, 20, 0, 0))


        pygame.display.update()


if __name__ == '__main__' :
    main()       

