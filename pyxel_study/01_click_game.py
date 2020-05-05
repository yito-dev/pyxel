import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, fps=60)
        pyxel.image(0).load(0, 0, "cat.png") # 画像読み込み
        #変数初期化
        self.x = 0
        self.y = 0
        self.vx = 1
        self.vy = 1
        self.exists = True
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            left = self.x
            top = self.y
            right = self.x + 16
            bottom = self.y + 16

            if left <= pyxel.mouse_x <= right:
                if top <= pyxel.mouse_y <= bottom:
                    self.exists = False 

            # 左クリックしたら猫消滅
            self.exists = False

        if self.exists == False:
            return

        self.x += self.vx
        self.y += self.vy
        if self.x <0:
            self.x = 0
            self.vx *= -1
        if self.y <0:
            self.y = 0
            self.vy *= -1
        if self.x > (pyxel.width-16):
            self.x = pyxel.width -16
            self.vx *= -1
        if self.y > (pyxel.height-16):
            self.y = pyxel.height -16
            self.vy *= -1

    def draw(self):
        pyxel.cls(0) # 画面をクリアする

        if self.exists == False:
            pyxel.text(60 , 50, "GAME CLEAR", 9)
            return

        pyxel.blt(self.x, self.y, 0, 0, 0, 16, 16, 5) # ニャンコ様を描画する

App()