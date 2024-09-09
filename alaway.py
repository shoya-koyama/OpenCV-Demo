import pygame  # Pygameライブラリをインポート
import random  # ランダム値を生成するためにrandomモジュールをインポート

# 初期設定
pygame.init()  # Pygameの初期化
screen_width = 800  # 画面幅を800に設定
screen_height = 600  # 画面高さを600に設定
screen = pygame.display.set_mode((screen_width, screen_height))  # 画面を設定
pygame.display.set_caption("Alaway")  # ウィンドウのタイトルを設定

# カラー定義
WHITE = (255, 255, 255)  # 白色の定義
BLACK = (0, 0, 0)  # 黒色の定義
RED = (255, 0, 0)  # 赤色の定義
BLUE = (0, 0, 255)  # 青色の定義

# パドルのクラス
class Paddle(pygame.sprite.Sprite):  # パドルを定義するクラス
    def __init__(self):
        super().__init__()  # 親クラスの初期化
        self.image = pygame.Surface([100, 10])  # パドルの画像サイズを100x10に設定
        self.image.fill(WHITE)  # パドルの色を白に設定
        self.rect = self.image.get_rect()  # パドルの矩形領域を取得
        self.rect.x = (screen_width // 2) - 50  # パドルの初期X位置を設定
        self.rect.y = screen_height - 30  # パドルの初期Y位置を設定

    def move_left(self, pixels):  # 左に移動するメソッド
        self.rect.x -= pixels  # 指定されたピクセル数だけ左へ移動
        if self.rect.x < 0:  # 画面の左端を超えたら位置を修正
            self.rect.x = 0

    def move_right(self, pixels):  # 右に移動するメソッド
        self.rect.x += pixels  # 指定されたピクセル数だけ右へ移動
        if self.rect.x > screen_width - 100:  # 画面の右端を超えたら位置を修正
            self.rect.x = screen_width - 100

# ボールのクラス
class Ball(pygame.sprite.Sprite):  # ボールを定義するクラス
    def __init__(self):
        super().__init__()  # 親クラスの初期化
        self.image = pygame.Surface([10, 10])  # ボールの画像サイズを10x10に設定
        self.image.fill(WHITE)  # ボールの色を白に設定
        self.rect = self.image.get_rect()  # ボールの矩形領域を取得
        self.rect.x = random.randint(0, screen_width - 10)  # ボールの初期X位置をランダムに設定
        self.rect.y = screen_height // 2  # ボールの初期Y位置を画面中央に設定
        self.speed_x = random.choice([-4, 4])  # ボールのX方向の速度をランダムに設定
        self.speed_y = -4  # ボールのY方向の速度を設定

    def update(self):  # ボールの位置を更新するメソッド
        self.rect.x += self.speed_x  # ボールのX方向の速度に従って移動
        self.rect.y += self.speed_y  # ボールのY方向の速度に従って移動

        if self.rect.x <= 0 or self.rect.x >= screen_width - 10:  # 左右の壁に当たったら反射
            self.speed_x = -self.speed_x

        if self.rect.y <= 0:  # 上の壁に当たったら反射
            self.speed_y = -self.speed_y

    def bounce(self):  # ボールが反射する際の処理
        self.speed_y = -self.speed_y  # Y方向の速度を反転

# ブロックのクラス
class Block(pygame.sprite.Sprite):  # ブロックを定義するクラス
    def __init__(self, x, y):
        super().__init__()  # 親クラスの初期化
        self.image = pygame.Surface([50, 20])  # ブロックの画像サイズを50x20に設定
        self.image.fill(RED)  # ブロックの色を赤に設定
        self.rect = self.image.get_rect()  # ブロックの矩形領域を取得
        self.rect.x = x  # ブロックのX位置を設定
        self.rect.y = y  # ブロックのY位置を設定

# スプライトグループ
all_sprites = pygame.sprite.Group()  # 全スプライトのグループを作成
blocks = pygame.sprite.Group()  # ブロックのスプライトグループを作成

# パドルとボールの生成
paddle = Paddle()  # パドルを生成
ball = Ball()  # ボールを生成

all_sprites.add(paddle)  # パドルをスプライトグループに追加
all_sprites.add(ball)  # ボールをスプライトグループに追加

# ブロックの生成
for i in range(6):  # 6列のブロックを生成
    for j in range(8):  # 8行のブロックを生成
        block = Block(50 + i * 100, 30 + j * 30)  # 各ブロックの位置を設定
        all_sprites.add(block)  # スプライトグループにブロックを追加
        blocks.add(block)  # ブロックグループにブロックを追加

# ゲームループ
clock = pygame.time.Clock()  # ゲームのフレーム管理用の時計を作成
running = True  # ゲームが実行中かどうかを管理するフラグ
while running:
    for event in pygame.event.get():  # イベントを取得
        if event.type == pygame.QUIT:  # 閉じるボタンが押されたらループを終了
            running = False

    # キー入力による操作
    keys = pygame.key.get_pressed()  # 押されているキーを取得
    if keys[pygame.K_LEFT]:  # 左キーが押されたらパドルを左に移動
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:  # 右キーが押されたらパドルを右に移動
        paddle.move_right(5)

    # ボールの動き
    ball.update()  # ボールの位置を更新

    # ボールとパドルの衝突判定
    if pygame.sprite.collide_rect(ball, paddle):  # ボールとパドルが衝突したかを確認
        ball.bounce()  # 衝突したらボールを反射させる

    # ボールとブロックの衝突判定
    block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)  # ボールがブロックに衝突したか確認
    for block in block_hit_list:  # 衝突したブロックのリストを処理
        ball.bounce()  # 衝突したらボールを反射させる

    # 画面リセット
    screen.fill(BLACK)  # 画面を黒でクリア
    all_sprites.draw(screen)  # 全てのスプライトを描画

    # ゲームオーバー判定
    if ball.rect.y > screen_height:  # ボールが画面下に出たらゲームオーバー
        running = False

    pygame.display.flip()  # 画面を更新
    clock.tick(60)  # フレームレートを60FPSに設定

pygame.quit()  # Pygameを終了
