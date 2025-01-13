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