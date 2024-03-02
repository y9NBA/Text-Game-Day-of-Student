from models import dict_classes
from peewee import SqliteDatabase, Model, ForeignKeyField, TextField, IntegerField

db = SqliteDatabase("sqlite_peewee_db.db")


class DB(Model):
    class Meta:
        database = db


class Role(DB):
    name = TextField()


class Specialization(DB):
    name = TextField()


class User(DB):
    login = TextField()
    usertgID = IntegerField()
    role = ForeignKeyField(Role)
    specialization = ForeignKeyField(Specialization)

    async def exists(self):
        pass


db.connect()

if len(db.get_tables()) == 3:
    print("[~] БД уже создана")
else:
    db.create_tables([Role, Specialization, User], safe=True)
    print("[~] Таблицы БД были созданы")

db.close()


for x in dict_classes:
    class_u = Specialization.get_or_create(name=x)
    print(f"[+] Запись 'role' [{class_u[0].id} {class_u[0].name}] " + ("добавлена" if class_u[1] else "обновлена"))

for x in ["Админ", "Игрок"]:
    role_u = Role.get_or_create(name=x)
    print(f"[+] Запись 'class' [{role_u[0].id} {role_u[0].name}] " + ("добавлена" if role_u[1] else "обновлена"))

print("[~] БД готова к работе")
