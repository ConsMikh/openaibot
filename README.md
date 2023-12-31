# Переменные среды для работы
OPENAI_API_KEY - ключ к API Open-AI
CMIKH_OPENAI_CHAT_BOT - ключ для доступа к боту телеграм


# Backog
1.  [x] Сброс сессии при достижении максимальной длины промта
2.  [ ] Сделать автоматическое отслеживание количества токенов. Сессия должна запрашивать максимальное количество токенов для модели. Когда промт приближается к максимальному количеству выводить сообщение об этом
3.  [x] Мониторинг количества токенов 
4.  [x] Команда - Выбор различных моделей
5.  [x] Команда - Создание системного промта для бота
6.  [x] Команда - Создание информационного сообщения
7.  [x] Сделать deploy бота через docker
8.  [x] Сделать автоматический перезапуск бота при перезагрузке сервера
9.  [ ] Сделать набор системных промтов для перевода моделей в нужный режим (например, промт для режима переводчика)
    1.  [ ] Автоматический переводчик
    2.  [ ] Краткое содержание текста
    3.  [ ] Расшифровка аудиосообщений и изложение краткого содержания
10. [ ] Добавить возможность использования моделей не openai



# Version history

| Версия | Описание изменений                                                                                                                                                                                                              |    Дата    |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------: |
|  1.0   | Простой бот. Ошибки не обрабатываются. Выводятся в чат                                                                                                                                                                          | 2023-07-08 |
|  1.1   | Добавлена команда /info, которая выводит версию бота и список моделей                                                                                                                                                           | 2023-07-08 |
|  1.2   | Добавлено:<br>- для каждого пользователя создается сессия<br>- команда /t для запроса количества токенов в текущей сессии<br>- команда /clear для сброса сессии                                                                 | 2023-07-09 |
|  1.3   | Добавлено:<br>- команда /model выбора модели<br>- команда /system для установки системного промта<br>- команда /sessions для вывода списка сессий<br>Доработано:<br>- команда /info выводит список команд и информацию о сессии | 2023-07-17 |
| 1.3.1  | Доработано:<br>- улучшено разделение на классы                                                                                                                                                                                  | 2023-07-17 |
| 1.3.2  | Сделал развертывание через docker-контейнер, добавил автозапуск контейнера на сервере                                                                                                                                           | 2023-07-20 |
| 1.3.3  | Добавил поддержку GPT-4                                                                                                                                                                                                         | 2024-01-02 |


# Sources

## Use-case

### Summarize Text

[35 Best ChatGPT Prompts to Summarize Text](https://nerdschalk.com/chatgpt-prompts-to-summarize-text/)

“Could you please provide a concise and comprehensive summary of the given text? The summary should capture the main points and key details of the text while conveying the author's intended meaning accurately. Please ensure that the summary is well-organized and easy to read, with clear headings and subheadings to guide the reader through each section. The length of the summary should be appropriate to capture the main points and key details of the text, without including unnecessary information or becoming overly long.”

“Can you provide a comprehensive summary of the given text? The summary should cover all the key points and main ideas presented in the original text, while also condensing the information into a concise and easy-to-understand format. Please ensure that the summary includes relevant details and examples that support the main ideas, while avoiding any unnecessary information or repetition. The length of the summary should be appropriate for the length and complexity of the original text, providing a clear and accurate overview without omitting any important information.”

“Could you please provide a summary of the given text, including all key points and supporting details? The summary should be comprehensive and accurately reflect the main message and arguments presented in the original text, while also being concise and easy to understand. To ensure accuracy, please read the text carefully and pay attention to any nuances or complexities in the language. Additionally, the summary should avoid any personal biases or interpretations and remain objective and factual throughout.

## Сети

### OpenAI

[Документация OpenAI API](https://platform.openai.com/docs/guides/gpt)

[How to format inputs to ChatGPT models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)

[A Simple Guide to The (New) ChatGPT API with Python](https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28)

[OpenAI Python Library](https://github.com/openai/openai-python)

[OpenAI Cookbook](https://github.com/openai/openai-cookbook/)

### Other

[YaLM 100B](https://github.com/yandex/YaLM-100B)

### Review

[Transformer models: an introduction and catalog — 2023 Edition](https://amatriain.net/blog/transformer-models-an-introduction-and-catalog-2d1e9039f376/)

[Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)

[Зоопарк трансформеров: большой обзор моделей от BERT до Alpaca](https://habr.com/ru/companies/just_ai/articles/733110/)

## Tools

[LangСhain](https://python.langchain.com/docs/get_started/introduction.html)

## Идеи для использования

[Пишем Telegram бота для распознавания голосовых сообщений и их обработки с помощью AI](https://habr.com/ru/articles/739868/)

BookGraph, агент, который делает визуальное представление всех тем и их связей из любой книги

## Misc

[Покупка виртуальных карт](https://wanttopay.net/)

[Как оплатить ChatGPT](https://dzen.ru/a/ZBmbwIEH5UfGiHbR)

[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

[Использование screen для сеансов в linux](https://wiki.merionet.ru/articles/kak-polzovatsya-utilitoj-screen-v-linux)

[Автозапуск скриптов в Debian](https://linuxhint.com/run-script-debian-11-boot-up/)
<br>Не забыть выставить права на выполнение для скрипта
