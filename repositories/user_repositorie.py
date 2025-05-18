from abc import ABC, abstractmethod
from models.user import User


class IUserRepository(ABC):

    @abstractmethod
    def add(self, user: User):
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def list_all(self) -> list[User]:
        pass
