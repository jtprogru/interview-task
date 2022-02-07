# interview-task

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Testing](https://github.com/jtprogru/interview-task/actions/workflows/testing.yml/badge.svg)](https://github.com/jtprogru/interview-task/actions/workflows/testing.yml)
[![GitHub stars](https://img.shields.io/github/stars/jtprogru/interview-task.svg)](https://github.com/jtprogru/interview-task/stargazers)
[![GitHub issues](https://img.shields.io/github/issues-raw/jtprogru/interview-task)](https://github.com/jtprogru/interview-task/issues)
[![GitHub](https://img.shields.io/github/license/jtprogru/interview-task)](https://github.com/jtprogru/interview-task/blob/main/LICENSE)
[![Donate](https://img.shields.io/badge/-Donate-blue?logo=paypal)](https://paypal.me/jtprog)
[![Donate](https://img.shields.io/badge/-Donate-blue?logo=patreon)](https://patreon.com/jtprogru)

Задачки, которые мне задают на собеседованиях (решаю их на Python, т.к. пока ничего другого не знаю).


## Как запустить

```shell
# Создаем виртуальное окружение с дефолтным для системы python3
make venv
# Устанавливаем зависимости
make install-deps
# Запускаем все тесты (так же запускаются линтеры)
make test
# Запускаем только линтеры
make lint
```

## Добавить свою задачку

```shell
# Клонируем репозиторий
git clone https://github.com/jtprogru/interview-task.git
# Переходим в ветку dev
git checkout dev
# Создаем файлик с задачкой по аналогии с другими в директории 'tasks'
touch tasks/task9999.py  # 9999 - порядковый номер файла с задачей
# Создаем файлик с тестами для задачи
touch tests/test_task9999.py
# Пишем задачку и тесты для нее
# После чего прогоняем тесты и линтеры
make test
```

## Feedback

Если случилось так, что ты начал использовать сие поделие и у тебя появился фидбэк,
пожалуйста создай [issues](https://github.com/jtprogru/interview-task/issues) или 
обратись в Telegram-чат [jtprogru_chat](https://t.me/jtprogru_chat).


## Authors

- Michael Savin
  - :octocat: [@jtprogru](https://www.github.com/jtprogru)
  - :bird: [@jtprogru](https://www.twitter.com/jtprogru)
  - :moneybag: [savinmi.ru](https://savinmi.ru)


## License

[LICENSE](LICENSE)
