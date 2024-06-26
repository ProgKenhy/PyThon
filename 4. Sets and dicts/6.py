import string

text = ("Таким образом, повышение уровня гражданского сознания позволяет оценить значение новых предложений?"
        " Повседневная практика показывает, что сложившаяся структура организации способствует повышению актуальности"
        " ключевых компонентов планируемого обновления. Практический опыт показывает, что курс на социально-ориентированный"
        " национальный проект в значительной степени обуславливает создание новых предложений! Дорогие друзья, постоянный"
        " количественный рост и сфера нашей активности требует определения и уточнения системы масштабного изменения ряда"
        " параметров? практика показывает, что постоянное информационно-техническое обеспечение нашей деятельности создаёт"
        " предпосылки качественно новых шагов для экономической целесообразности принимаемых решений! Практический опыт показывает,"
        " что консультация с профессионалами из IT влечет за собой процесс внедрения и модернизации новых предложений? Дорогие друзья,"
        " реализация намеченного плана развития требует от нас анализа новых предложений. Значимость этих проблем настолько очевидна, что"
        " повышение уровня гражданского сознания напрямую зависит от соответствующих условий активизации! С другой стороны социально-экономическое"
        " развитие представляет собой интересный эксперимент проверки позиций, занимаемых участниками в отношении поставленных задач! Разнообразный и богатый"
        " опыт постоянное информационно-техническое обеспечение нашей деятельности напрямую зависит от соответствующих условий активизации. Не следует, однако,"
        " забывать о том, что рамки и место обучения кадров требует от нас системного анализа системы обучения кадров, соответствующей насущным потребностям."
        " Задача организации, в особенности же а А а А новая модель организационной деятельности позволяет оценить значение системы обучения кадров, соответствующей"
        " насущным потребностям? Повседневная практика показывает")

table = str.maketrans("", "", string.punctuation)
text_without_punct = text.translate(table)
# words = text_without_punct.lower().split()
words = text_without_punct.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_words_in_lecsic = sorted(word_count.items(), key=lambda x: str(x).lower())
sorted_words = sorted(sorted_words_in_lecsic, key=lambda x: x[-1], reverse=True)

for word in sorted_words:
    print(word[0])
