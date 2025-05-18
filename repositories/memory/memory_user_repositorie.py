from typing import Optional

from repositories.user_repositorie import User
from repositories.user_repositorie import IUserRepository


class MemoryBookRepositorie(IUserRepository):
    
    def __init__(self):
        self.__users: list[User] = []

    def add(self, user: User):
        self.__users.append(user)
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        user_found = None

        for user in self.__users:
            if user_id == user.id:
                user_found = user
                break

        return user_found

    def list_all(self) -> list[User]:
        return self.__users.copy()
