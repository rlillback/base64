import base64


if __name__ == '__main__':
    username = input('Username (e.g. DOMAIN\\username): ')
    password = input('Password: ')
    plain_text = f"{username}:{password}"
    print(f"plain_text = {plain_text}")

    basic_auth = "Basic " + base64.b64encode(plain_text.encode('utf-8')).decode('utf-8')
    print(f"Basic authentication = {basic_auth}")

    encoded_text = basic_auth[6:]
    decoded_text = base64.b64decode(encoded_text)
    print(f"decoded_text = {decoded_text}")
