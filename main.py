import random

RANDOM_START = 1000
RANDOM_END = 5000


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def generate_prime(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def greatest_com_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(a, b):
    for inv in range(0, b):
        if (a * inv) % b == 1:
            return inv
    print("There is no modular inverse -> a is not a coprime to m")


def generate_rsa_key():
    p = generate_prime(RANDOM_START, RANDOM_END)
    q = generate_prime(RANDOM_START, RANDOM_END)
    while p == q:
        q = generate_prime(RANDOM_START, RANDOM_END)
    n = p * q
    m = (p - 1) * (q - 1)
    e = random.randrange(1, m)
    while greatest_com_divisor(e, m) != 1:
        e = random.randrange(1, m)
    d = mod_inverse(e, m)
    return (d, n), (e, n)


def encrypt(public_key, plain_text):
    e, n = public_key
    cipher_text = []
    for char in plain_text:
        a = ord(char)
        cipher_text.append(pow(a, e, n))

    return cipher_text


def decrypt(private_key, cipher_text):
    d, n = private_key
    plain_text = ''
    for num in cipher_text:
        a = pow(num, d, n)
        plain_text = plain_text + str(chr(a))
    return plain_text


if __name__ == '__main__':
    private_key, public_key = generate_rsa_key()
    message = 'example message with RSA algorithm'
    print('original message: ', message)
    cipher = encrypt(public_key, message)
    print("Cipher text is: ", cipher)
    plain = decrypt(private_key, cipher)
    print("Decrypted text is : ", plain)