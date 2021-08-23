# Lekcja 5.5
# restAPI + biblioteka request
# Jest to biblioteka HTTP na licencji Apache2 w Python'ie (możemy wykonywać requesty przy użyciu Python'a).
# CRUD - (C)reate, (R)ead/retrieve, (U)pdate, (D)elete/destroy
# CRUD stosowany jest w przypadku dostępu do pamięci trwałej (bazy danych), ale również w przypadku HTTP.
# Metody:
#  POST --> CREATE,
#  READ --> GET (pobranie lub wyświetlenie zasobów),
#  UPDATE --> PUT
#  DELETE --> DELETE (usuwanie zasobów na serwerze)
# Grupy statusów odpowiedzi HTTP:
#  1xx - Informational
#  2xx - Success
#  3xx - Redirection
#  4xx - Client Error
#  5xx - Server Error

import requests

# r = requests.get('https://fabrykatestow.pl')
# print(r)

# post = requests.post('http://httpbin.org/post')
# put = requests.put('http://httpbin.org/put')
# delete = requests.delete('http://httpbin.org/delete')
#
# print(delete)

# Dalej możemy przekazywać różne parametry w naszym zapytaniu, np. url z dowolnymi parametrami.

parameters = {'key1':'value1', 'key2':'value2'}

r = requests.get('https://fabrykatestow.pl', params=parameters)
print(r.url)
print(r.text)
print(r.encoding)

