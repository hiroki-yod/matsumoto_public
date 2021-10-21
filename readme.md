# アプリケーション名
**松本家通信 &emsp;The Matsumoto’s House Newsletter**  
URL : https://katsurao-diary.com
<br>
<br>

# 説明 &emsp;Description
「松本家通信」という私が初めて制作したWebアプリケーションです。原発被災地である福島県葛尾村にて展示会などの活動を行っている松本家計画のホームページとして制作しました。作品等の情報公開機能およびメンバー限定の掲示板機能を有しています。

"The Matsumoto’s House Newsletter" is the first web application I have created. This is the website of "The Matsumoto House Project" which hold exhibitions and other activities in Katsurao Village, Fukushima Prefecture, a nuclear power plant affected area. It has a function for publishing information on works, etc. and a members-only bulletin board function.
<br>
<br>

# 機能一覧
- ユーザー情報
    1. ユーザー登録
    2. ログイン/ログアウト
    3. プロフィール登録/修正
- 情報公開
    1. データベース登録
    2. YouTubeデータ取得
- 掲示板
    1. 投稿
    2. コメント
    3. リアクション
    4. メール通知
<br>
<br>

# 機能紹介
## 1. ユーザー登録
1. 「会員限定ページ」➡「会員登録」からユーザー登録をする
2. 登録したユーザー名/パスワードでログインする
3. プロフィール情報を登録する
4. 会員限定ページに移動する
![function1](https://user-images.githubusercontent.com/77391181/138307239-f3cfe657-0880-47ce-a967-ba497398d05b.gif)

## 2. データベース登録
1. スーパーユーザーで管理サイトにログインする
2. NEWS/WORKS/ESSAY を登録する
3. NEWS/WORKS/ESSAYページに反映される
![function2](https://user-images.githubusercontent.com/77391181/138310045-ba7e3e65-42a3-49d1-b1cc-25c9d29a4cc3.gif)
## 3. YouTubeデータ取得
1. 一般ユーザーで /manage にログインする
2. 「YouTube更新」ボタンを押す
3. 取得された動画がMOVIEページに反映される
![function3](https://user-images.githubusercontent.com/77391181/138308752-d225eeeb-6875-4733-9576-1cec862d764c.gif)

## 4. BBS
1. 一般ユーザーで「会員限定ページ」にログインする
2. 「通知設定」からメール通知を設定をする
3. 掲示板（メイン）から投稿する
4. 各投稿をクリックし掲示板（コメント）に移動する
5. 任意の投稿にリアクションをつける
6. 任意の投稿にコメントをつける
7. 投稿/コメント/リアクション は設定に応じて通知される
![function4](https://user-images.githubusercontent.com/77391181/138312395-b36a0c6d-aae6-4c1c-9e8d-979fe3dca6d9.gif)

<br>
<br>

# 実行手順（Django開発用サーバー）
## 1. 動作環境
以下の実行環境での動作を確認しています。
- Ubuntu 16.04 LTS
- Python 3.9.1

## 2. プロジェクトリポジトリの取得
アプリケーションを配置したいディレクトリにて「git clone」コマンドを実行してください。
```console
$ git clone git@github.com:hiroki-yod/matsumoto_public.git
```

## 3. パッケージのインストール
次のパッケージをインストールしてください。
```console
pip install Django
pip install django-environ                #環境変数
pip install django_bootstrap5             #CSS
pip install django-widget-tweaks          #CSS
pip install google-api-python-client      #YouTube Data API
pip install Pillow                        #画像
pip install isodate                       #時間
```

## 4. 環境変数の設定
matsumoto_public（magage.pyがあるフォルダ）に .env という名前のファイルを作成し、次の内容を記入てください。
```.env
#matsumoto > settigs.py

#GitHub公開用の適当なSECRET_KEYです（本番環境で使用しないでください）
SECRET_KEY='%710m*zic)#0u((qugw#1@e^ty!c)9j04956v@ly(_86n$rg)h'
DEBUG=True
ALLOWED_HOSTS='localhost'
DATABASE_URL=sqlite:///db.sqlite3

#通知設定を使用しない場合は不要
EMAIL_HOST_USER='任意のGmailアドレス'
EMAIL_HOST_PASSWORD='設定したGmailのパスワード'
DEFAULT_FROM_EMAIL='任意のGmailアドレス'

#bbs > views.py
#Googleドライブを使用しない場合は不要
GOOGLE_DRIVE_URL='会員限定ページのGoogleドライブURL'

#main > modules > youtube.py
#動画取得を使用しない場合は不要
API_KEY='Youtube Data API の API_KEY'
CHANNEL_ID='動画を取得するチャンネルのCHANNEL_ID'
```

## 5. データベースの生成
データベースを生成します。
```console
$ python manage.py migrate
```

## 6. 開発用サーバーの立ち上げ
Django開発用サーバーを立ち上げてアクセスする。
```console
$ python manage.py runserver
```
仮想環境でサーバーを起動し、ローカル環境からアクセスする場合は、次のようにサーバーを立ち上げる。
```console
$ python manage.py runserver 0:8000
```

