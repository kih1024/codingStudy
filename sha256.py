import hashlib


answer = input()
print(hashlib.sha256(answer.encode()).hexdigest())