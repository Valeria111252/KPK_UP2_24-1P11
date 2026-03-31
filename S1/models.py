"""База данных Auth"""


from datetime import datetime
from peewee import (
    Model,
    CharField,
    BooleanField,
    DateTimeField,
    ForeignKeyField,
    AutoField,
    SqliteDatabase
)

DB = SqliteDatabase('auth.db')


class BaseModel(Model):
    """Базовая модель"""

    class Meta:
        """Класс мета"""

        database = DB


class User(BaseModel):
    """Класс пользователя"""

    id = AutoField()
    username = CharField(unique=True)
    email = CharField(unique=True)
    password_hash = CharField()
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.now)


class RefreshToken(BaseModel):
    """Класс токена"""

    id = AutoField()
    user = ForeignKeyField(User,
                           backref='tokens', on_delete='CASCADE'
                           )
    token = CharField()
    expires_at = DateTimeField()
    created_at = DateTimeField(default=datetime.now)


class PasswordReset(BaseModel):
    """Класс сброса пароля"""
    id = AutoField()
    user = ForeignKeyField(User,
                           backref='resets', on_delete='CASCADE'
                           )
    reset_token = CharField()
    expires_at = DateTimeField()
    is_used = BooleanField(default=False)


def create_tables():
    """Создаёт таблицы"""
    with DB:
        DB.create_tables([User,
                          RefreshToken, PasswordReset])


if __name__ == "__main__":
    create_tables()
