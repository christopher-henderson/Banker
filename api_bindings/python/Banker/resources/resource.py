class Resource(object):

    BORG = dict()

    def __init__(self, db_connector, **kwargs):
        object.__setattr__(self, 'db_attrs', dict())
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)
            self.db_attrs[k] = v
        self.db_connector = db_connector

    def __settattr__(self, k, v):
        if k in self.db_attrs:
            self.db_attrs[k] = 1
        object.__setattr__(self, k, v)

    def save(self):
        dirty_attrs = self.get_dirty_attrs()
        self.db_connector.send(self.__class__.name, 'PATCH', dirty_attrs)
        for attr in dirty_attrs.keys():
            self.db_attrs[attr] = 0

    def get_dirty_attrs(self):
        return {
            attr: self.__getattribute__[attr]
            for attr, dirty in self.db_attrs.items() if dirty
        }

