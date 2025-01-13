def insecure_function(user_input):
    # Potencjalna podatność na SQL Injection
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    print(query)  # Użycie niebezpiecznego wejścia bez sanitizacji

def example_division(a, b):
    return a / b  # Brak obsługi dzielenia przez zero

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content  # Brak obsługi potencjalnych błędów wejścia/wyjścia

def insecure_eval(user_input):
    eval(user_input)  # Wykorzystanie eval na niezweryfikowanym wejściu

# Przykłady wywołań
insecure_function("admin' --")
print(example_division(10, 0))  # To wywołanie spowoduje błąd
print(read_file("test.txt"))
insecure_eval("__import__('os').system('ls')")

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