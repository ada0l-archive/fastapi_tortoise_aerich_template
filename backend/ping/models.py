from tortoise import Model, fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Ping(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)


Ping_Pydantic = pydantic_model_creator(Ping, name="Ping")
PingIn_Pydantic = pydantic_model_creator(Ping, name="PingIn", exclude_readonly=True)
