import pyautogui as pag

screen_width, screen_height = pag.size()


def open_cmd():
    pag.hotkey('win', 'r')
    pag.typewrite('cmd', interval=0.01)  # useful for entering text, newline is Enter
    pag.typewrite(['enter'])


def open_exe(file_paths, exe_names: list):
    open_cmd()
    for i in range(len(exe_names)):
        # wrtiing the path
        if '.py' in file_paths[i]:
            pag.typewrite(f'python {file_paths[i]}', interval=0.01)
            pag.typewrite(['enter'])

        else:
            pag.typewrite(f'cd {file_paths[i]}', interval=0.01)
            pag.typewrite(['enter'])
            pag.typewrite(f'{exe_names[i]}', interval=0.01)
            pag.typewrite(['enter'])

    for i in range(len(exe_names)+4):
        pag.click(x=960, y=540)
        pag.hotkey('win', 'down')


def confirm_automatization():
    pag.confirm('Deseja automatizar a execução dos seus programas?')


confirm_automatization()
open_exe([r'C:\Program Files\Google\Chrome\Application',
          r"C:\Users\l04620\AppData\Roaming\Spotify",
          r'C:\Users\l04620\Anaconda3\Scripts\anaconda-navigator-script.py'],

         ['chrome.exe', 'Spotify.exe', 'anaconda-navigator-script.py'])
