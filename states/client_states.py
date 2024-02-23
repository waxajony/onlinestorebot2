from aiogram.fsm.state import State, StatesGroup


class ClientAdsStates(StatesGroup):
    selectAdCategory = State()
    selectAdProduct = State()
    insertTitle = State()
    insertText = State()
    insertPrice = State()
    insertImages = State()
    insertPhone = State()

class editClientAdsStates(StatesGroup):
    idADS = State()
    editselectAdCategory = State()
    editselectAdProduct = State()
    editinsertTitle = State()
    editinsertText = State()
    editinsertPrice = State()
    editinsertImages = State()
    editinsertPhone = State()