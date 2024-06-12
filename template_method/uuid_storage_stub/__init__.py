import uuid

class UUIDStorage:
    def __init__(self):
        self.storage = dict()
    def get_item_by_uuid(self, uuid):
        return self.storage.get(uuid)
    def put_item_in_storage(self, item):
        uuid_ = uuid.uuid4()
        try:
            self.storage[uuid_] = item
        except KeyError: #handling existing uuid but not likely happen
            uuid_ = None
        return uuid_
    def del_item_in_storage(self, uuid):
        if uuid in self.storage:
            del self.storage[uuid]
            return True
        else:
            return False