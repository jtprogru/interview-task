# interview-task

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Testing](https://github.com/jtprogru/interview-task/actions/workflows/testing.yml/badge.svg)](https://github.com/jtprogru/interview-task/actions/workflows/testing.yml)
[![GitHub stars](https://img.shields.io/github/stars/jtprogru/interview-task.svg)](https://github.com/jtprogru/interview-task/stargazers)
[![GitHub issues](https://img.shields.io/github/issues-raw/jtprogru/interview-task)](https://github.com/jtprogru/interview-task/issues)
[![GitHub](https://img.shields.io/github/license/jtprogru/interview-task)](https://github.com/jtprogru/interview-task/blob/main/LICENSE)

Задачки с собеседований, LeetCode, CodeWars (решаю их на Python)

Зависимости и окружение управляются через [uv](https://docs.astral.sh/uv/). Установить uv можно по [инструкции](https://docs.astral.sh/uv/getting-started/installation/).

## Как запустить

```shell
# Создаём виртуальное окружение и ставим все зависимости из pyproject.toml/uv.lock
make install-deps
# Запускаем все тесты (так же запускаются линтеры)
make test
# Запускаем только линтеры
make lint
```

Можно работать с uv и напрямую, без make:

```shell
# Установить зависимости
uv sync
# Запустить тесты
uv run pytest
```

## Добавить свою задачку

```shell
# Клонируем репозиторий
git clone https://github.com/jtprogru/interview-task.git
# Переходим в ветку dev
git checkout dev
# Добавляем новую задачу вместе с тестами
make newtask
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
