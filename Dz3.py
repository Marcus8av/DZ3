# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.
import string
from collections import Counter

text = '''Равным образом консультация с профессионалами из IT позволяет выполнить важнейшие задания по разработке существующих финансовых и административных условий. 
Разнообразный и богатый опыт повышение уровня гражданского сознания требует от нас системного анализа системы масштабного изменения ряда параметров? 
Соображения высшего порядка, а также выбранный нами инновационный путь играет важную роль в формировании системы масштабного изменения ряда параметров.
Задача организации, в особенности же реализация намеченного плана развития представляет собой интересный эксперимент проверки соответствующих условий активизации! 
С другой стороны выбранный нами инновационный путь в значительной степени обуславливает создание направлений прогрессивного развития? 
Равным образом постоянный количественный рост и сфера нашей активности способствует подготовке и реализации дальнейших направлений развитая системы массового участия. 
Практический опыт показывает, что рамки и место обучения кадров способствует повышению актуальности дальнейших направлений развития проекта.
Равным образом социально-экономическое развитие позволяет выполнить важнейшие задания по разработке всесторонне сбалансированных нововведений! 
Равным образом повышение уровня гражданского сознания способствует повышению актуальности системы масштабного изменения ряда параметров. 
Соображения высшего порядка, а также рамки и место обучения кадров требует от нас системного анализа дальнейших направлений развития проекта. 
Значимость этих проблем настолько очевидна, что сложившаяся структура и организации играет важную роль в формировании форм воздействия.'''

text = text.translate(str.maketrans('', '', string.punctuation)).lower().split()

word_counts = Counter(text)
most_common_words = word_counts.most_common(10)

print(most_common_words)
