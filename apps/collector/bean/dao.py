import abc


class DAO(abc.ABC):

    @abc.abstractmethod
    def create(self):
        pass

    @abc.abstractmethod
    def insert(self, bean):
        pass

    @abc.abstractmethod
    def delete(self, bean):
        pass

    @abc.abstractmethod
    def update(self, bean):
        pass

    @abc.abstractmethod
    def fetch_all(self):
        pass

    @abc.abstractmethod
    def clear(self):
        pass

    @abc.abstractmethod
    def flush(self):
        pass
