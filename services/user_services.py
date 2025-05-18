from typing import Optional

from models.user import User
from repositories.user_repositorie import IUserRepository


class BookService:

    def __init__(self, user_repositorie: IUserRepository):
        self.__user_repositorie = user_repositorie
    
    def add_user(self, user: User):
        if self.__user_repositorie.find_by_id(user.id):
            raise ValueError(f"Book with ID: {user.id} already exists.")
        
        self.__user_repositorie.add(user)

    def get_user_by_id(self, book_id: int) -> Optional[User]:
        return self.__user_repositorie.find_by_id(book_id)
    
    def list_users(self):
        return self.__user_repositorie.list_all()
    