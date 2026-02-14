from aiogram.filters.state import State,StatesGroup
class ReklamaState(StatesGroup):
    add = State()
    check = State()
class TextState(StatesGroup):
    text = State()
    url = State()
    check = State()
class ImageState(StatesGroup):
    image = State()
    url = State()
    check = State()
class VideoState(StatesGroup):
    video = State()
    url = State()
    check = State()
class AddChannelState(StatesGroup):
    id = State()
    check = State()
class UserGetData(StatesGroup):
    name = State()
    role = State()
    group = State()
class UserChangeNameData(StatesGroup):
    name = State()
class UserChangeRoleData(StatesGroup):
    role = State()
class UserChangeGroupData(StatesGroup):
    group = State()
class AttestatTestCreate(StatesGroup):
    create = State()
class SchoolTestCreate(StatesGroup):
    create = State()
class SimpleTestCreate(StatesGroup):
    create = State()
    