try:
    xx = 1 / 0
except ZeroDivisionError as error:
    print(f'ZeroDivisionError: {error}')

try:
    assert False, 'Помилка перевірки'
except AssertionError as error:
    print(f'AssertionError: {error}')

try:
    xx = None
    xx.method()
except AttributeError as error:
    print(f'AttributeError: {error}')

try:
    import xxmodule
except ImportError as error:
    print(f'ImportError: {error}')

try:
    xlist = [1, 2, 3]
    xx = xlist[10]
except IndexError as error:
    print(f'IndexError: {error}')

try:
    xdict = {'key': 'value'}
    xx = xdict['nonexistent_key']
except KeyError as error:
    print(f'KeyError: {error}')

try:
    xlist = [0] * (10**8)
except MemoryError as error:
    print(f'MemoryError: {error}')

try:
    print(xxx)
except NameError as error:
    print(f'NameError: {error}')

try:
    with open('xx.txt', 'r') as file:
        file.read()
except FileNotFoundError as error:
    print(f'FileNotFoundError: {error}')
except PermissionError as error:
    print(f'PermissionError: {error}')

try:
    with open('/etc/passwd', 'w') as file:
        file.write('content')
except FileNotFoundError as error:
    print(f'FileNotFoundError: {error}')
except PermissionError as error:
    print(f'PermissionError: {error}')

import socket

try:
    socket.setdefaulttimeout(2)
    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("xxtestxxsitexx.com", 81))
except OSError as error:
    print(f'OSError: {error}')

def xxff(xx):
    if xx == 0:
        return
    xxff(xx - 1)

try:
    xxff(10000)
except RecursionError as error:
    print(f'RecursionError: {error}')

try:
    exec('print("Hello, world!"')
except SyntaxError as error:
    print(f'SyntaxError: {error}')

try:
    xx = '1' + 2
except TypeError as error:
    print(f'TypeError: {error}')

try:
    xx = int('Текст')
except ValueError as error:
    print(f'ValueError: {error}')

try:
    text = b'\x80'.decode('utf-8')
except UnicodeDecodeError as error:
    print(f'UnicodeDecodeError: {error}')

try:
    text = 'Привіт'.encode('ascii')
except UnicodeEncodeError as error:
    print(f'UnicodeEncodeError: {error}')
