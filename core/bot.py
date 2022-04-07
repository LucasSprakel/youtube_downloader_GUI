from pytube import YouTube
from PySimpleGUI import PySimpleGUI as sg


def download_video(link):
    try:
        i = 0
        video = YouTube(link)
        sg.popup("Your Download has started, a new windown will pop up when it's finished", 
        auto_close=True, auto_close_duration=5, font=('verdana', 13))
        video.streams.get_highest_resolution().download('Videos')
        sg.popup("Your Download has finished", font=('verdana', 13))
    except:
        if link == "":
            sg.theme('DarkBrown1')
            
            layout_column = [
                [sg.Image('core/images/warning.png')],   
                [sg.Text('Youtube Downloader Warning:', font=('verdana', 15), size=(24,0))],
                [sg.Text('Insert Youtube Link First', font=('verdana', 15))]
            ]   
            
            layout = [[sg.Column(layout_column, element_justification='center')]]
            
            janela = sg.Window('Warning', layout)
            
            while True:
                eventos, valores = janela.read()
                if eventos == sg.WINDOW_CLOSED:
                    break
        else:
            sg.theme('DarkBrown4')

            layout_column = [
                [sg.Image('core/images/error.png')],
                [sg.Text('Youtube Downloader Error:', font=('verdana', 15), size=(21, 0))],
                [sg.Text('Invalid Youtube Link', font=('verdana', 15))]
            ]   
            
            layout = [[sg.Column(layout_column, element_justification='center')]]
            
            janela = sg.Window('Error', layout)
            
            while True:
                eventos, valores = janela.read()
                if eventos == sg.WINDOW_CLOSED:
                    break


def download_audio(link):
    try:
        video = YouTube(link)
        video.streams.get_audio_only().download('Audios')
    except:
        if link == "":
            sg.theme('DarkBrown1')
            
            layout_column = [
                [sg.Image('core/images/warning.png')],   
                [sg.Text('Youtube Downloader Warning:', font=('verdana', 15), size=(24,0))],
                [sg.Text('Insert Youtube Link First', font=('verdana', 15))]
            ]   
            
            layout = [[sg.Column(layout_column, element_justification='center')]]
            
            janela = sg.Window('Warning', layout)
            
            while True:
                eventos, valores = janela.read()
                if eventos == sg.WINDOW_CLOSED:
                    break
        else:
            sg.theme('DarkBrown4')

            layout_column = [
                [sg.Image('core/images/error.png')],
                [sg.Text('Youtube Downloader Error:', font=('verdana', 15), size=(21, 0))],
                [sg.Text('Invalid Youtube Link', font=('verdana', 15))]
            ]   
            
            layout = [[sg.Column(layout_column, element_justification='center')]]
            
            janela = sg.Window('Error', layout)
            
            while True:
                eventos, valores = janela.read()
                if eventos == sg.WINDOW_CLOSED:
                    break


def credits():

    sg.theme('DarkRed1')

    layout_column = [
        [sg.Text('By Lucas Sprakel', font=('verdana', 30))]
    ]

    layout = [[sg.Column(layout_column, element_justification='center')]]

    janela = sg.Window('Credits', layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
    

def help():
    sg.theme('DarkGreen')

    layout_column = [
        [sg.Text('Before Download, insert youtube link', font=('verdana', 15))],
        [sg.Text('\nAfter Download, a window will popup', font=('verdana', 15))]
    ]

    layout = [[sg.Column(layout_column, element_justification='center')]]

    janela = sg.Window('Help', layout)

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break

       
def __main__():
    sg.theme('DarkRed1')

    layout_column = [
        [sg.Image('core/images/icone.png')],
        [sg.Text('Url:'), sg.Input(key='url', size=(48,3))],
        [sg.Button('Download Video', size=(50,1))],
        [sg.Button('Download Audio', size=(50,1))],
        [sg.Button('Credits', size=(50,1))],
        [sg.Button('Help', size=(50,1))],
    ]

    layout = [[sg.Column(layout_column, element_justification='center')]]

    janela = sg.Window('Youtube Downloader by Lucas Sprakel', layout, resizable=True, element_justification='center')

    while True:
        i=0
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Download Video':
            download_video(valores['url'])
        if eventos == 'Download Audio':
            download_audio(valores['url'])
        if eventos == 'Credits':
            credits()
        if eventos == 'Help':
            help()


    
