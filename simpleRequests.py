import requests, os

methods = {
    'GET': requests.get,
    'POST':requests.post, 
    'HEAD':requests.head, 
    'OPTIONS':requests.options, 
    'DELETE':requests.delete, 
    'PUT':requests.put, 
    'PATCH':requests.patch
#    'CONNECT':requests.connect
#    'TRACE':requests.trace
}

def fire(method, url):
    call = methods.get(method, -1)
    if call != -1:
        if url:
            result = call(url)
            return result
        else:
            return f'Invalid url {url}'
    else:
        return f'Invalid Method {method}'

def clearConsole():
    os.system('cls')

if __name__ == '__main__':
    consoleRun = True
    print('Enter request in the form: <METHOD> <url>')
    while consoleRun:
        user = input(' $ ')

        match user:
            case 'cls':
                clearConsole()
            case 'clear':
                clearConsole()
         
        if user.split(' ')[0] in methods.keys:
            print(f' $ ~ {fire(user, user.split(' ')[1])}')