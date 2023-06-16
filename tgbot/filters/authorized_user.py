import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.services.interact_database import db_interaction


class AuthorizedUserFilter(BoundFilter):
    key = 'is_authorized'

    def __init__(self, is_authorized: typing.Optional[bool] = None):
        self.is_authorized = is_authorized

    async def check(self, obj):
        if self.is_authorized is None:
            return False
        is_authorized = db_interaction.check_user_in_db(obj.from_user.id)
        return is_authorized == self.is_authorized
