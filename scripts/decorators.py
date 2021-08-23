# Lekcja 5.4
# W trakcie pisania kodu błędy mogą się zdarzać b. często. Czasem mogą być to błędy podane przez użytkonika programu,
# a czasem może to być sytuacja wyjątkowa, której nie przewidzieliśmy w trakcie pisania programu.
# Np. funkcja dzielenia, gdzie możemy zapomnieć o dodaniu wyjątku dla dzielenia przez "0". (WYJĄTEK)
# Do tego należy obsługa wyjątków, które należy tutaj wywołać.
# try - except

try:
    wait = WebDriverWait(driver, 5)
    wait.until(ec.visibility_of_element_located((By.Id, 'test')))
    print('iframe found')

except TimeoutException:
    print('There is no iframe')

