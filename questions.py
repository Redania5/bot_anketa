all_questions = {
    1: [['Что из перечисленных гусям НЕ полезно?', 'Хлеб'], ['Картофель', 'Соль', 'Свёкла', 'Хлеб']],
    2: [['Сколько обычно у гусей яиц?', '6-12'], ['6-12', '3-7', '2-8', '8-13']],
    3: [['Сколько весит взрослый домашний гусь?', '5-7 кг'], ['3-5 кг', '5-7 кг', '7-9 кг', '9-11 кг']],
    4: [['В каком семействе (по научной классификации) находится род "гуси"?', 'Утиные'],
        ['Утиные', 'Гусеобразные', 'Птицы', 'Хордовые']],
    5: [['Чем домашний гусь отличается от дикого?', 'Больше дикого, обычно белый.'],
        ['Больше дикого, обычно серый.', 'Больше дикого, обычно белый.',
         'Меньше дикого, обычно серый.', 'Меньше дикого, обычно белый.']],
    6: [['Какое из данных утвердений о гусях является верным?',
         'Человек приручил гусей 3000-4000 лет назад.'],
        ['Способность летать развивается через 5-6 месяцев после рождения.',
         'Гуси не могут развивать скорость более 80 км/ч.',
         'Линька у диких гусей встречается 3-4 раза в год.',
         'Человек приручил гусей 3000-4000 лет назад.']],
    7: [['Сколько обычно живут дикие гуси?', '18-20 лет'], ['10-12 лет', '14-16 лет', '18-20 лет', '22-24 года']],
    8: [['Какое из этих утверждений о гусях - ложное?', 'Гуси чаще летают парами, чем стаями.'],
        ['Дикие гуси способны летать на высоте до десяти километров.',
         'Гуси чаще летают парами, чем стаями.',
         'В языке гуся можно выделить десять отдельных звуков.',
         'На протяжении нескольких веков гусиные перья использовались для письма.']],
}

results = {
    9: 'Произошла ошибка.',
    8: 'Поздравляю! Вы знаете практически всё про гусей и набрали максимальное количество очков!',
    6: 'Вы очень многое знаете о гусях! Ещё немного, и будете настоящим специалистом :)',
    4: ('Неплохой результат! Вы имеете неплохие знания о гусях, но есть еще много, что можно изучить. ' +
        'Рекомендую вам продолжать изучать эту тему и расширять свои знания о гусях.'),
    2: 'Если вы не очень много знаете о гусях, наверняка вы очень талантливы в других сферах. Удачи!',
    0: ('Ответы, которые вы дали, были интересными и оригинальными. ' +
        'Иногда новый взгляд на вещи может привести к неожиданному открытию.')
}