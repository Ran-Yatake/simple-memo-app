# ベースイメージ（DebianベースでPythonとNode.jsを両方サポート）
FROM mcr.microsoft.com/vscode/devcontainers/python:3.11

# Node.jsのバージョンを指定してインストール（例: 20.x）
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs \
    && npm install -g npm

# 必要なら追加ツール
RUN apt-get install -y git

# Pythonパッケージのインストール
RUN pip install --no-cache-dir flask flask-cors pymysql

# 作業ユーザー
USER vscode
