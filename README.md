# Sources

[How to format inputs to ChatGPT models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb)

[A Simple Guide to The (New) ChatGPT API with Python](https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28)

[Покупка виртуальных карт](https://wanttopay.net/)

[Как оплатить ChatGPT](https://dzen.ru/a/ZBmbwIEH5UfGiHbR)

[OpenAI Python Library](https://github.com/openai/openai-python)

[OpenAI Cookbook](https://github.com/openai/openai-cookbook/)

[pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

[Использование screen для сеансов в linux](https://wiki.merionet.ru/articles/kak-polzovatsya-utilitoj-screen-v-linux)


# Backog
1. + Сброс сессии при достижении максимальной длины промта
2. Сделать автоматическое отслеживание количества токенов. Сессия должна запрашивать максимальное количество токенов для модели. Когда промт приближается к максимальному количеству выводить сообщение об этом
3. + Мониторинг количества токенов 
4. + Команда - Выбор различных сетей
5. + Команда - Создание системного промта для бота
6. + Команда - Создание информационного сообщения
7. Сделать deploy бота через docker и github actions. Для docker использовать безопасную передачу секретов в контейнер
8. Сделать автоматический перезапуск бота при отключении
9. Сделать набор системных промтов для перевода моделей в нужный режим (например, промт для режима переводчика)
10. Добавить возможность использования моделей не openai



# Version history

| Версия | Описание изменений                                                                                                                                                                                                              |    Дата    |
| :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :--------: |
|  1.0   | Простой бот. Ошибки не обрабатываются. Выводятся в чат                                                                                                                                                                          | 2023-07-08 |
|  1.1   | Добавлена команда /info, которая выводит версию бота и список моделей                                                                                                                                                           | 2023-07-08 |
|  1.2   | Добавлено:<br>- для каждого пользователя создается сессия<br>- команда /t для запроса количества токенов в текущей сессии<br>- команда /clear для сброса сессии                                                                 | 2023-07-09 |
|  1.3   | Добавлено:<br>- команда /model выбора модели<br>- команда /system для установки системного промта<br>- команда /sessions для вывода списка сессий<br>Доработано:<br>- команда /info выводит список команд и информацию о сессии | 2023-07-17 |
| 1.3.1  | Доработано:<br>- улучшено разделение на классы                                                                                                                                                                                  | 2023-07-17 |