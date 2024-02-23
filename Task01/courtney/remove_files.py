import os
import PySimpleGUI as sg

sg.theme('SystemDefaultForReal')
layout = [
    [sg.Text('Directory', justification='right'), sg.InputText(key='-DIR-', justification='right', do_not_clear=False), sg.FolderBrowse()],
    [sg.Text('Extension of Files to Remove', justification='right'), sg.InputText(key='-EXT-', justification='right', size=(5,5), do_not_clear=False)],
    [sg.Ok(), sg.Cancel()],
    [sg.Multiline(default_text="Script Progress\n------------------------------------------------\n", size=(80, 10),
                  auto_refresh=True, reroute_stdout=False, key="-OUTPUT-", autoscroll=True, border_width=5)]
]
window = sg.Window('Remove Unwanted Files', layout)
check = False
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        directory = str(values['-DIR-'])
        extension = str(values['-EXT-'])
        output = window['-OUTPUT-']
        output.update('\nScanning ' + directory + '...', append=True)
        for dirs, subdirs, files in os.walk(directory):
            for file in files:
                check = False
                if file.endswith(extension):
                    output.update('\n\nRemoving File: ' + file, append=True)
                    check = True
                    os.remove(os.path.join(dirs, file))
        if not check:
            output.update('\n\nNo files found in directory with the extension: ' + extension, append=True)
        output.update('\n\n\nComplete!', append=True)
window.close()
