import pygame
import sys
import os
import yaml
import argparse

image_dir = ""




def main() :
    menber_list = parse_member_list()

    pygame.init()
    screen = pygame.display.set_mode((1920, 1080)) # FHD
    pygame.displaly.set_caption("NumberCheck")

    fullscreen_flg = True
    running = True
    while running :
        pygame.time.wait(30)
        screen.fill((0, 20, 0, 0))
        screen.blit(bg_img, (0,0))

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
                    fullscreen_flag = not fullscreen_flag
                    if fullscreen_flag:
                        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, 32) 
                    else:
                        screen = pygame.display.set_mode((width, height), 0, 32) 





        pygame.display.update()


if __name__ == '__main__' :
    main()       


