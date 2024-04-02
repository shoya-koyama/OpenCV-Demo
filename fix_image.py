import cv2

# 画像を読み込む
image = cv2.imread('brockBreak.png')  # 'your_image.jpg'の部分を読み込む画像のファイル名に置き換えてください

# 画像を表示する
cv2.imshow('Previous Image', image)
cv2.waitKey(0)  # キーボードから何かキーが押されるまで画像を表示

# グレースケールに変換
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)

# 画像のリサイズ
# ここでは幅と高さを半分に設定しています
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
cv2.imshow('Resized Image', resized_image)
cv2.waitKey(0)

# 画像の回転
# ここでは中心を軸に90度回転させています
height, width = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)

# すべてのウィンドウを閉じる
cv2.destroyAllWindows()
