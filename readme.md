# Django サンプル

## ■ Python環境（PipEnv）

```shell
# PipEnv環境作成
pipenv --python 3.6

# パッケージ
pipenv install django
pipenv install psycopg2

# 開発用パッケージ
pipenv install autopep8 --dev
pipenv install pylint --dev
pipenv install flake8 --dev
pipenv install mypy --dev
pipenv install rope --dev
```

## ■ Djangoプロジェクト作成

```shell
pipenv shell
django-admin startproject djangosample .
```
