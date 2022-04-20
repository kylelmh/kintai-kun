# Kintai-kun
Kintai-kun is a lightweight digital timecard web app written in Django.
The production uses an nginx reverse proxy for processing static files.

It is currently in beta and Japanese localization is hard coded.

SASS files are currently unsupported due to long build times for docker images.
Please compile SASS files locally.

Requirements:
docker
docker-compose

To start the development server, create a `.env` file following `.env.sample` and use

```
docker-compose build
docker-compose up
```

To deploy the server,

```
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up -d
```

# 勤怠管理ウェブサーバー　きんたいくん
Django をベースにした勤怠管理ウェブサーバーです。

# 立ち上げ
`.env.sample` ファイルを参考にし、ローカルで`.env`を作成してから
```
docker-compose build
docker-compose up
```
実行してください。
