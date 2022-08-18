import pygame
import sys
import os
import yaml
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
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)

        if width > 0 and height > 0 :
            surface = pygame.transform.scale(surface, (width, height))

    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface.convert()

# ----------------------------------------------------
# ボタン クラス
# ----------------------------------------------------

class Button():
    def __init__(self, name, pos, size, pad, image):
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.pad = pad
        self.image = image
        
        # self.color = color
        # self.font = pygame.font.SysFont(None, size)
        # self.text = self.font.render(text, True, txtcolor)
        # self.button = Rect(pos, (self.text.get_width() + pad, self.text.get_height() + pad))
        # self.button_bottom = Rect(pos, (self.button.width, self.button.height + 5))

    def update(self):
        self.button.top = self.y

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.button.top += 2
                    print(f"{ self.name }ボタンが押されました")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(self.text, (self.x + self.pad / 2, self.y + self.pad / 2))

# ----------------------------------------------------
# ナンバーパネル クラス
# ----------------------------------------------------
class NumberPanel(prm) :
    # コンストラクタ
    def __init__(self, name, pos, pad):
        self.name           = name
        self.x              = pos[0]
        self.y              = pos[1]
        self.pad            = pad
        self.images         = self.set_images()
        self.current_image  = None
        self.rect           = Rect(pos, (self.text.get_width() + pad, self.text.get_height() + pad))
        self.rect_bottom    = Rect(pos, (self.button.width, self.button.height + 5))

    def update(self):
        self.button.top = self.y

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button.collidepoint(event.pos):
                    self.button.top += 2
                    print(f"{ self.name }ボタンが押されました")

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(self.text, (self.x + self.pad / 2, self.y + self.pad / 2))




def button_set() :
    pass

# ----------------------------------------------------
# メイン
# ----------------------------------------------------
def main() :
    menber_list = parse_member_list()
    prm = set_parameter()

    # 初期座標設定
    width, height = 1280, 720
    # team = button_set()
    # num1 = button_set()
    # num2 = button_set()
    # num3 = button_set()

    bg_img = load_image()

    pygame.init()
    screen = pygame.display.set_mode((prm['width'], prm['height'])) # FHD
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


