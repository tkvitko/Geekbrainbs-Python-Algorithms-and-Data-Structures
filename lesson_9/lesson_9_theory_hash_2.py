import hashlib

print(hashlib.sha1(b'Hello World!').hexdigest())
print(hashlib.sha1(b'Hello World.').hexdigest())

# При передаче данных злоумышленник может подменить как данные, так и сам хеш
# Чтобы этого избежать, используется секретное слово
# слово знают только отправитель и получатель.
# Если злоумышленник перехватит письмо, подделать хеш не получится (для хеширования нужно будет секретное слово)

print(hashlib.sha1(b'secret_word' + b'Hello World.').hexdigest())

# Но злоумышленник может дописать что-то в конце письма
# посчитать хеш дописанного куска
# и прибавить его к имеющемуся хешу
# выход:

s = hashlib.sha1(b'Hello world.').hexdigest()
print(s.encode('utf-8'))
print(hashlib.sha1(b'secret_word' + bytes(s.encode('utf-8'))).hexdigest())
# тогда верный хеш злоумышленник не сформирует