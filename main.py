
リファレンス


アイデア


API


プロジェクト


変数
変化するデータの保持

ディスプレイ
micro:bitのLEDディスプレイへの出力

ボタン
コード中でボタン入力を使用する

ループ
数え上げと繰り返しの命令セット

条件文
コード内で判断する

加速度センサー
ジェスチャーや動きの検出

コメント
Pythonコードを説明する

算術演算
Pythonにおける基本的な算術演算

リスト（配列）
リストでのデータを管理

関数
プログラムの効率化

無線
micro:bit間のメッセージ送信

照度レベル
micro:bitを照らす光の照度を測定

温度
micro:bitの温度測定

コンパス
磁場の方向と強度を測定する

音
ミュージック、スピーチ、その他のサウンドを再生します

マイク
V2
サウンドレベルの測定と応答

タッチロゴ
V2
金色のロゴを追加ボタンとして使う

データロギング
V2
micro:bitにセンサーデータを記録

端子
micro:bitを拡張

データ型
Pythonでさまざまなデータを格納する方法

文字列操作
Pythonでのテキスト処理

テキストの入出力
micro:bitプログラムでコンピューターのキーボードと画面を使う方法

高度な算術演算
より多くの数学関数をPythonに追加する
パラシュート

from microbit import *

# 定数の設定
GRAVITY = 1  # 重力加速度を1Gとする

# 加速度を計測する関数
def measure_acceleration():
    reading = accelerometer.get_z() / 1000  # z方向の加速度を取得（単位はm/s^2）
    acceleration = (reading / GRAVITY) - 1  # 重力加速度を引くことで実際の加速度を求め、単位をGに変換する
    return acceleration

# メインのプログラム
while True:
    if button_b.is_pressed():  # Bボタンが押されたら
        display.show("START")  # "START"を表示する
        sleep(1000)  # 1秒待つ（測定開始までの待ち時間）
        acceleration = measure_acceleration()  # 加速度を計測する
        while True:
            current_acceleration = measure_acceleration()  # 現在の加速度を計測する
            if current_acceleration > acceleration:  # 加速度が上昇し始めたら
                break  # 測定を終了する
            acceleration = current_acceleration  # 加速度を更新する
        display.scroll("Landing Accel: {:.2f}G".format(acceleration))  # 着地時の加速度を表示する
        while not button_a.is_pressed():  # Aボタンが押されるまで続ける
            display.scroll("Landing Accel: {:.2f}G".format(acceleration))  # 着地時の加速度を表示する
    display.clear()  # ディスプレイをクリアする



ゆさぶられた (shake)
無線メッセージ
ログに記録された行がありません

hex ファイルまたは Python ファイルを開くか、他のファイルを追加する
パラシュート.hex を読み込みました
