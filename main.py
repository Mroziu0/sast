def unsafe_sql_query(user_input):
    import sqlite3

    # Potencjalna podatność na SQL Injection
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Niebezpieczne zapytanie
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

def divide_numbers(a, b):
    # Brak obsługi dzielenia przez zero
    return a / b  # To spowoduje błąd, jeśli b = 0

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()  # Brak obsługi błędów

def eval_user_input(user_input):
    # Użycie eval na niepewnym wejściu
    return eval(user_input)  # Potencjalna podatność na wykonanie kodu

# Użycie generujących błędy wywołań
print(unsafe_sql_query("admin' --"))
print(divide_numbers(5, 0))  # Brak obsługi dzielenia przez zero
print(read_file("nonexistent.txt"))  # Próbuj otworzyć nieistniejący plik
print(eval_user_input("__import__('os').system('ls')"))  # Niebezpieczne wykonanie

# def safe_division(a, b):
#     # Obsługuje przypadek dzielenia przez zero
#     if b == 0:
#         return "Error: Cannot divide by zero"
#     return a / b

# def read_file_safe(filename):
#     # Obsługuje błędy wejścia/wyjścia
#     try:
#         with open(filename, 'r') as file:
#             content = file.read()
#         return content
#     except FileNotFoundError:
#         return "Error: File not found"
#     except IOError:
#         return "Error: An I/O error occurred"

# def safe_eval(expression):
#     # Uważaj na eval – zaleca się unikanie go, ale jeśli musi być użyty:
#     safe_names = {'__builtins__': None}  # Ograniczamy dostęp do wbudowanych funkcji
#     return eval(expression, safe_names)

# # Przykładowe wywołania funkcji
# print(safe_division(10, 2))
# print(read_file_safe("test.txt"))
# print(safe_eval("1 + 2"))