from tortoise import fields
from tortoise.models import Model
from enum import Enum


class Game(Model):
    game_id = fields.BigIntField(pk=True)
    guild_id = fields.BigIntField()
    creator_id = fields.BigIntField()
    isStarted = fields.BooleanField(default=False)
    category_id = fields.BigIntField(null=True)
    lobby_id = fields.BigIntField(null=True)
    alpha_id = fields.BigIntField(null=True)
    bravo_id = fields.BigIntField(null=True)
    chat_id = fields.BigIntField(null=True)
    players: fields.ReverseRelation["Player"]

    class Meta:
        table = "games"


class RoleEnum(str, Enum):
    SUPPORT = "support"
    SLAYER = "slayer"
    BACKLINE = "backline"


class Player(Model):
    player_id = fields.BigIntField(pk=True)  # manually assigned Discord user ID
    game_ref = fields.ForeignKeyField("models.Game", related_name="players")
    username = fields.CharField(max_length=64)
    role = fields.CharEnumField(enum_type=RoleEnum, default=RoleEnum.SUPPORT)
    position = fields.IntField()
    isCreator = fields.BooleanField(default=False)

    class Meta:
        table = "players"
