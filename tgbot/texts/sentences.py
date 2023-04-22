# файл со всеми текстами для отправки ботом
start_user_message_text = '👋 Добро пожаловать!'
start_admin_message_text = '👋 Добро пожаловать, админ!'

make_poll_title_text = 'Отправьте текст опроса'
make_poll_chat_id_text = 'Отправьте id чата для отправки опроса. Бот должен быть добавлен в этот чат'
make_poll_confirm_text = 'Отправить данный опрос в чат с id {chat_id}?'

make_poll_answers_text = 'Отправьте варианты ответа на опрос\n' \
                         'Каждый ответ напишите на новой строке:\n' \
                         'ответ 1\n' \
                         'ответ 2\n' \
                         'ответ 3\n'

make_poll_chat_id_error_text = 'Не удалось найти час с id {chat_id}.\n' \
                               'Возможно бот не добавлен в этот чат\n' \
                               'Отправьте новый id или перезапустите действие'
good_send_poll_text = 'Опрос был отправлен'
bad_send_poll_text = 'Не удалось отправить опрос'
bad_make_poll_text = 'Не удалось создать опрос'

success_cancel_text = 'Действие отменено'

menu_text = 'Для получения погоды отправьте команду /weather\n' \
            'Для конвертации валюты отправьте команду /currency\n' \
            'Для получения списка валюты отправьте команду /currency_symbols\n' \
            'Для получения случайного фото котика отправьте команду /cat\n' \
            'Для отправки опроса в группу отправьте команду /poll\n' \
            'Для отмены действия отправьте команду /cancel'

bad_photo_text = 'Не удалось найти милое фото'

start_weather_text = 'Отправьте название города для получения погоды'
bad_weather_text = 'Не удалось получить данные о погоде в городе {city_name}'

from_currency_text = 'Отправьте сокращенное название валюты из которой хотите перевести'
to_currency_text = 'Отправьте сокращенное название валюты в которую хотите перевести'
amount_currency_text = 'Отправьте сумму в {from_currency} для для расчета перевода в {to_currency}'
bad_amount_currency_text = 'Отправьте число'
result_currency_text = '{amount} в {from_currency} равняется {res_amount} в {to_currency}'

bad_currency_text = 'Не удалось получить данные'