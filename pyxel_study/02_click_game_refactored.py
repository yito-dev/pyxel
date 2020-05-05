import pyxel
import random

class Cat:
    def __init__(self):
        # 変数初期化
        self.x = 0
        self.y = 0
        self.vx = 1
        self.vy = 1
        self.exists = True # ニャンコ様存在フラグ

    def update(self):
        # 移動する
        self.x += self.vx
        self.y += self.vy
        # 画面外に出ないようにする
        if self.x < 0:
            self.x = 0
            self.vx *= -1 # 移動方向を反転する
        if self.y < 0:
            self.y = 0
            self.vy *= -1 # 移動方向を反転する
        if self.x > pyxel.width - 16:
            self.x = pyxel.width - 16
            self.vx *= -1 # 移動方向を反転する
        if self.y > pyxel.height - 16:
            self.y = pyxel.height - 16
            self.vy *= -1 # 移動方向を反転する
            
    def checkHit(self, x, y):
        # 当たり判定
        left   = self.x
        top    = self.y
        right  = self.x + 16
        bottom = self.y + 16
        if left <= x <= right:
            if top <= y <= bottom:
                return True # 当たり
        return False # 外れ

    def draw(self):
        # ニャンコ様を描画する
        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 5)

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=30)
        pyxel.image(0).load(0, 0, "cat.png") # 画像読み込み

        self.cat_list = []
        self.total_time = 0
        self.cat_num = 1000
        self.timeuptime = 500

        for i in range(self.cat_num):
            cat = Cat()
            cat.x = random.randint(0, pyxel.width)
            cat.y = random.randint(0, pyxel.height)
            cat.vx = random.randint(1,2)
            cat.vy = random.randint(1,2)
            self.cat_list.append(cat)

        pyxel.mouse(True) # マウスカーソルを表示する
        pyxel.run(self.update, self.draw)

    def update(self):
        self.total_time += 1
        for cat in self.cat_list:
            if cat.exists:
                if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
                    if cat.checkHit(pyxel.mouse_x, pyxel.mouse_y):
                        # 命中したので、ニャンコを消す
                        cat.exists = False
                if cat.exists:
                    # 生存している場合のみ更新
                    cat.update()

    def draw(self):
        pyxel.cls(0)
        self.cnt_cat = 0
        #pyxel.text(0, 0, "IF TIME IS OVER" + str(self.timeuptime) + ", GAME WILL BE END", 3)
        pyxel.text(0, 10, "TIME :" + str(self.total_time), 3)

        for cat in self.cat_list:
            if cat.exists:
              # 生存している場合のみ描画
                cat.draw()
            else:
                self.cnt_cat += 1
        #if self.total_time >= self.timeuptime:
            #pyxel.text(60,50, "GAME OVER", random.randint(2,10))
        
        if self.cnt_cat == self.cat_num:
            pyxel.text(0, 50, "YOU CATCH" + str(selt.cat_num) + "CATS! GREAT!!", random.randint(2,10))
        else:
            pyxel.text(0, 0 , "YOU CATCH "+str(self.cnt_cat)+" CATS!", random.randint(2,10))

App()