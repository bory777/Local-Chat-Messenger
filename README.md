# UDP Chat Messenger

このプロジェクトは、UNIXドメインソケットを使用してUDPを介してメッセージを送受信するシンプルなチャットアプリケーションです。Fakerライブラリを使用してランダムな文字列を生成し、サーバーからクライアントに送信します。

## 概要

このプロジェクトには、サーバーとクライアントの2つのPythonスクリプトが含まれています。

- `udp_server.py`: メッセージを受信し、ランダムな文字列をクライアントに送信するサーバースクリプト。
- `udp_client.py`: メッセージを入力してサーバーに送信し、サーバーからの応答を受信するクライアントスクリプト。

## 必要な依存関係

- Python 3.x
- Faker ライブラリ

## 使用方法

### サーバーの実行

まず、サーバースクリプトを実行します。これにより、サーバーが起動し、クライアントからのメッセージを待機します。

```bash
python udp_server.py
```

### クライアントの実行

別のターミナルでクライアントスクリプトを実行し、サーバーにメッセージを送信します。

```bash
python udp_client.py
```

クライアントが実行されると、メッセージを入力するプロンプトが表示されます。メッセージを入力してEnterキーを押すと、メッセージがサーバーに送信され、サーバーからの応答が表示されます。"exit" と入力すると、クライアントおよびサーバーが終了します。
