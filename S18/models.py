from peewee import *
import sqlite3

db = SqliteDatabase('room_equipment.db')

class BaseModel(Model):
    class Meta:
        database = db

class Equipment(BaseModel):
    name = CharField(max_length=255, constraints=[Check('length(name) >= 1')])
    type = CharField(max_length=50)  # проектор, компьютеры, станки, доски, другое
    room_id = IntegerField()  # внешний ключ к Room Service, но здесь без FK
    status = CharField(max_length=20, default='active')
    inventory_number = CharField(max_length=50, unique=True, null=True)
    description = TextField(default='')

    class Meta:
        indexes = (
            (('room_id', 'name'), True),  # уникальная комбинация
        )

def init_db():
    db.connect()
    db.create_tables([Equipment], safe=True)
    db.close()

# точка входа для инициализации
if __name__ == '__main__':
    init_db()
    print("Database initialized for Room Equipment Service")