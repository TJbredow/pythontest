import requests
s = requests.session()
response = s.get('http://127.0.0.1:5000/getcode')
testdata = response.json().get('values')
sumval = response.json().get('sumvalue')
print(response.json())
increment_counter = 0
id = response.json().get('id')
for i, val in enumerate(testdata):
    try:
        if val < testdata[i + 1]:
            increment_counter = increment_counter + 1
    except IndexError:
        break
payload = {'id':id,'answer':increment_counter}
print(increment_counter)

response = s.post('http://127.0.0.1:5000/submitcode',json=payload)
print(response.text)

increment_counter = 0
for i, val in enumerate(testdata):
    try:
        if val < testdata[i + sumval]:
            increment_counter = increment_counter + 1
    except IndexError:
        break
payload = {'id':id,'answer':increment_counter}
print(increment_counter)

response = s.post('http://127.0.0.1:5000/submitcodetwo',json=payload)
print(response.text)

