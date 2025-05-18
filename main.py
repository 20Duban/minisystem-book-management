from models.book import Book
from models.user import User
from repositories.memory.memory_book_repositorie import MemoryBookRepositorie
from repositories.memory.memory_user_repositorie import MemoryUserRepositorie
from repositories.memory.memory_loan_repositorie import MemoryLoanRepository
from services.book_services import BookService
from services.user_services import UserService
from services.loan_services import LoanService


def show_options():
    print("\n===== MINI BOOK MANAGEMENT SYSTEM =====")
    print("[1] Registrar libro")
    print("[2] Listar libros")
    print("[3] Registrar usuario")
    print("[4] Listar usuarios")
    print("[5] Prestar libro")
    print("[6] Devolver libro")
    print("[7] Ver préstamos")
    print("[0] Salir")

def option_1(book_service: BookService):
    title = input("Título del libro: ")
    author = input("Autor del libro: ")
    book = Book(id=0, title=title, author=author)
    book_service.add_book(book)
    print("✅ Libro registrado.")

def option_2(book_service: BookService):
    books = book_service.list_books()
    print("\n📚 Libros registrados:")
    for book in books:
        status = "Disponible" if book.is_available else "Prestado"
        print(f"[{book.id}] {book.title} - {book.author} ({status})")

def option_3(user_service: UserService):
    name = input("Nombre del usuario: ")
    user = User(id=0, name=name)
    user_service.add_user(user)
    print("✅ Usuario registrado.")

def option_4(user_service: UserService):
    users = user_service.list_users()
    print("\n👥 Usuarios registrados:")
    for user in users:
        print(f"[{user.id}] {user.name}")

def option_5(loan_service: LoanService):
    book_id = int(input("ID del libro a prestar: "))
    user_id = int(input("ID del usuario: "))
    try:
        loan_service.borrow_book(book_id, user_id)
        print("✅ Libro prestado.")
    except ValueError as e:
        print(f"❌ Error: {e}")

def option_6(loan_service: LoanService):
    loan_id = int(input("ID del préstamo: "))
    try:
        loan_service.return_book(loan_id)
        print("✅ Libro devuelto.")
    except ValueError as e:
        print(f"❌ Error: {e}")

def option_7(loan_service: LoanService):
    loans = loan_service.list_loans()
    print("\n📄 Préstamos:")
    for loan in loans:
        print(f"[{loan.id}] Libro ID: {loan.book_id}, Usuario ID: {loan.user_id}, Prestado: {loan.loan_date.strftime('%Y-%m-%d %H:%M')}")


def main():

    book_repo = MemoryBookRepositorie()
    user_repo = MemoryUserRepositorie()
    loan_repo = MemoryLoanRepository()

    book_service = BookService(book_repo)
    user_service = UserService(user_repo)
    loan_service = LoanService(loan_repo, user_repo, book_repo)

    while True:
        show_options()

        option = input("Seleccione una opción: ")

        if option == "1":
            option_1(book_service)

        elif option == "2":
            option_2(book_service)

        elif option == "3":
            option_3(user_service)

        elif option == "4":
            option_4(user_service)

        elif option == "5":
            option_5(loan_service)

        elif option == "6":
            option_6(loan_service)

        elif option == "7":
            option_7(loan_service)

        elif option == "0":
            print("👋 Saliendo del sistema.")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()