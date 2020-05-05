import pyxel

class App:
    def __init__(self):
        # 初期化
        pyxel.init(160, 120)
        self.x = 0
        #画像の読み込み
        pyxel.image(0).load(0,0,"cat.png")
        # 実行
        pyxel.run(self.update, self.draw)

    def update(self):
        # 更新
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        # 描画
        # 画面を消去
        pyxel.cls(0)
        # 矩形を描画
        pyxel.rect(self.x , 0, 7, 7, 9)

        #マウスカーソルに追従させる
        px = pyxel.mouse_x
        py = pyxel.mouse_y
        image_no = 0
        u = 0
        v = 0
        w = 16
        h = 16
        pyxel.blt(px, py, image_no, u, v, w, h, 5)

App()