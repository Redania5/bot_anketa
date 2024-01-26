import telebot
import json
from questions import all_questions, results
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message

TOKEN = '6925944808:AAHQecKROgFYRHczkepdTd5jKV441A_I_Wc'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message: Message):

    bot.send_message(message.chat.id, 'Привет! Это небольшая бот-анкета, которая проверит ваши знания о гусях.')
    que = 1
    chat_id = str(message.chat.id)
    with open('question_number', 'r') as f:
        all_qn1 = json.load(f)

        if chat_id not in all_qn1 or (chat_id in all_qn1 and all_qn1[chat_id][0] == 1):
            all_qn1[chat_id] = [1, 0]

            with open('question_number', 'w') as f2:
                json.dump(all_qn1, f2)

            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for opt in all_questions[que][1]:
                markup.add(KeyboardButton(opt))
            to_send = f'{que}. {all_questions[que][0][0]}'
            bot.send_message(message.chat.id, to_send, reply_markup=markup)
            # задали 1-ый вопрос и следующее сообщение/ответ обработаем в обработчике handle_main
            bot.register_next_step_handler_by_chat_id(message.chat.id, handle_main)

        elif chat_id in all_qn1 and all_qn1[chat_id][0] >= 1:
            s9 = f"У вас есть начатая попытка прохождения теста, вы ответили на {all_qn1[chat_id][0] - 1}/8 вопросов."
            bot.send_message(message.chat.id, s9)
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton('Да'))
            markup.add(KeyboardButton('Нет'))
            bot.send_message(message.chat.id, 'Хотите ли вы продолжить её?', reply_markup=markup)
            # Перенаправка следующего сообщения в обработчик found_saved
            bot.register_next_step_handler_by_chat_id(message.chat.id, found_saved)


def found_saved(message2: Message):

    from_user3 = message2.text
    chat_id = str(message2.chat.id)
    if from_user3 == '/start':
        return handle_start(message2)

    if from_user3.lower() != 'да' and from_user3.lower() != 'нет':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(KeyboardButton('Да'))
        markup.add(KeyboardButton('Нет'))
        bot.send_message(message2.chat.id, 'Пожалуйста, выберите Да или Нет', reply_markup=markup)
        # если не Да и не Нет, то следующее сообщение обрабатываем снова в found_saved, пока не будет Да или Нет
        bot.register_next_step_handler_by_chat_id(message2.chat.id, found_saved)
        return

    if from_user3.lower() == 'да':
        with open('question_number', 'r') as f:
            all_qn1 = json.load(f)
            que = all_qn1[chat_id][0]

    elif from_user3.lower() == 'нет':
        with open('question_number', 'r') as f:
            all_qn1 = json.load(f)
        with open('question_number', 'w') as f:
            que = 1
            all_qn1[chat_id] = [1, 0]
            json.dump(all_qn1, f)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in all_questions[que][1]:
        markup.add(KeyboardButton(opt))
    to_send = f'{que}. {all_questions[que][0][0]}'
    bot.send_message(message2.chat.id, to_send, reply_markup=markup)
    # задали вопрос и следующее сообщение/ответ обработаем в обработчике handle_main
    bot.register_next_step_handler_by_chat_id(message2.chat.id, handle_main)


# @bot.message_handler(content_types=['text'])
def handle_main(message: Message):
    from_user = message.text

    if from_user == '/start':
        return handle_start(message)

    chat_id = str(message.chat.id)
    with open('question_number', 'r') as f:
        all_qn = json.load(f)
        que = all_qn[chat_id][0]
        corr_ans = all_qn[chat_id][1]

    if from_user in all_questions[que][1]:
        if from_user == all_questions[que][0][1]:
            corr_ans += 1

        que += 1
        if que != 9:
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for opt in all_questions[que][1]:
                markup.add(KeyboardButton(opt))
            to_send = f'{que}. {all_questions[que][0][0]}'
            bot.send_message(message.chat.id, to_send, reply_markup=markup)

        else:
            bot.send_message(message.chat.id, f'Вы набрали {corr_ans}/8 правильных ответов.')
            for num in results:
                if corr_ans >= num:
                    # изображение
                    if num != '9':
                        img = open(f"{str(num)}.jpg", 'rb')
                        bot.send_photo(message.chat.id, img)
                    bot.send_message(message.chat.id, results[num])
                    break
            with open('question_number', 'w') as f:
                all_qn[chat_id] = [1, 0]
                json.dump(all_qn, f)
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(KeyboardButton('/start'))
            bot.send_message(message.chat.id, 'Для повторного прохождения теста нажмите /start.',
                             reply_markup=markup)
            return

    else:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        for opt in all_questions[que][1]:
            markup.add(KeyboardButton(opt))
        bot.send_message(message.chat.id, 'Пожалуйста, выберите один из предложенных варантов ответа.',
                         reply_markup=markup)

    chat_id = str(message.chat.id)
    with open('question_number', 'r') as f:
        all_qn = json.load(f)
    with open('question_number', 'w') as f2:
        all_qn[chat_id] = [que, corr_ans]
        json.dump(all_qn, f2)

    # задали вопрос и снова ждем ответ в обработчике handle_main
    bot.register_next_step_handler_by_chat_id(message.chat.id, handle_main)


@bot.message_handler(content_types=['text'])
def handle_default(message: Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('/start'))
    bot.send_message(message.chat.id, 'Для повторного прохождения теста нажмите /start.',
                     reply_markup=markup)


bot.polling()
