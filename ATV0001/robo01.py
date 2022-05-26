import json
import pyautogui as p
import win32api
import win32con
import pywintypes


def bot01():
    """
    Funcao que pega a resolucao atual do windows pelo pyautogui
    e junto com a bib win32 faz a conversao para a nova resolucao informada no JSON
    """
    res_width, res_height = p.size()
    print('Resolução Atual: ', res_width, 'x', res_height)

    with open("APR.json", encoding='utf-8') as apr_json:
        resolucao = json.load(apr_json)

    for i in resolucao:
        print('Resolução lida do JSON: ',
              i['width_json'], 'x', i['height_json'])

    if res_width == (i['width_json']) and res_height == (i['height_json']):
        print('Resolução está OK.')

    if res_width != (i['width_json']) and res_height != (i['height_json']):
        devmode = pywintypes.DEVMODEType()

        devmode.PelsWidth = (i['width_json'])
        devmode.PelsHeight = (i['height_json'])

        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

        win32api.ChangeDisplaySettings(devmode, 0)
        print('Resolução alterada para =',
              i['width_json'], 'x', i['height_json'])


if __name__ == '__main__':
    bot01()
