from typing import Optional

from repositories.user_repositorie import User
from repositories.user_repositorie import IUserRepository


class MemoryUserRepositorie(IUserRepository):
    
    def __init__(self):
        self.__users: list[User] = []
        self.__current_id = 1

    def add(self, user: User):
        user.id = self.__current_id
        self.__users.append(user)
        self.__current_id += 1
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        user_found = None

        for user in self.__users:
            if user_id == user.id:
                user_found = user
                break

        return user_found

    def list_all(self) -> list[User]:
        return self.__users.copy()
