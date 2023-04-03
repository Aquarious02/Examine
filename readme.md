# Тестовое задание
В этом задании Вам предстоит показать свои умения:
* в анализе онлайн документации
* чтения кода
* написания тестов

## Что нужно сделать?
Необходимо протестировать функционал прибора.

## Что понадобится?
* Pycharm
* Python 3 (рекомендуется 3.10)
* poetry

## Что уже есть?
* API прибора. Это тот самый функционал, который нужно протестировать.
В условиях данного задания это единственная документация на прибор.
* Имитатор прибора. Он будет отвечать на запросы.

## На что мы обратим внимание:
* Покрытие проверками. Вы должны быть уверены, что сможете уловить ошибку.
* Читаемость кода. Написанный единожды код будут многократно читать разные люди.


# Начало работы
В проекте используется менеджер зависимостей poetry. Подробнее [здесь](https://python-poetry.org/).
Достаточно установить poetry в системный Python
```shell
pip install poetry==1.2
```
После чего настроить работу с окружением в PyCharm.
[Set up poetry environment in PyCharm](https://www.jetbrains.com/help/pycharm/poetry.html#poetry-env)
После проделанных действий нужно установить необходимые пакеты
```shell
poetry install
```
И выбрать интерпретатор (`python.exe`) из только что созданного виртуального окружения

# Вводная информация


# Полезные ссылки
* [pytest doc](https://docs.pytest.org/en/7.1.x/contents.html)
* [poetry doc](https://python-poetry.org/docs/)
* [pytest in pycharm](https://www.jetbrains.com/help/pycharm/pytest.html)