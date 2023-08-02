# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —кортеж вещей. 
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. 
# Код должен расширяться на любое большее количество друзей.

things = {
    'Игорь': ('компас', 'cпальник', 'палатка', 'дождевик', 'сеть'),
    'Егор': ('cпальник', 'палатка', 'удочка', 'аптечка'),
    'Саня': ('палатка', 'рюкзак', 'каремат', 'карта', 'спички'),
    'Костян': ('cпальник', 'кроссовки','палатка','дождевик'),
    'Ефим': ('пластыри', 'бинт', 'половник', 'спички')
}

all_things = set()
single_things = {}
lacking_things = {}

for friends in things:
    single = set(things[friends])
    lacking = set()
    for next_friend in things:
        if next_friend != friends:
            single -= set(things[next_friend])
            if not lacking:
                lacking |= (set(things[next_friend]))
            else:
                lacking.intersection_update(set(things[next_friend]))
    all_things |= set(things[friends])
    single_things[friends] = single
    lacking_things[friends] = lacking - set(things[friends])

print(f"Все вещи: {all_things}\n"
      f"Уникальные вещи: {single_things}\n"
      f"Вещи которые есть у всех друзей кроме одного: {lacking_things}\n")