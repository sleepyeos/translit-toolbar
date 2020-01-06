import PySimpleGUI as sg

translit_table = {
    'A':'А',
    'B':'Б',
    'V':'В',
    'G':'Г',
    'D':'Д',
    'E':'Е',
    'ЫO':'Ё',
    'ЗH':'Ж',
    'Z':'З',
    'I':'И',
    'J':'Й',
    'K':'К',
    'L':'Л',
    'M':'М',
    'N':'Н',
    'O':'О',
    'P':'П',
    'R':'Р',
    'S':'С',
    'T':'Т',
    'U':'У',
    'F':'Ф',
    'H':'Х',
    'C':'Ц',
    'ЦХ':'Ч',
    'СХ':'Ш',
    'ШХ':'Щ',
    'Y':'Ы',
    'ЫЕ':'Э',
    'ЫУ':'Ю',
    'ЫА':'Я',
    'a':'а',
    'b':'б',
    'v':'в',
    'g':'г',
    'd':'д',
    'e':'е',
    'ыo':'ё',
    'зh':'ж',
    'z':'з',
    'i':'и',
    'j':'й',
    'k':'к',
    'l':'л',
    'm':'м',
    'n':'н',
    'o':'о',
    'p':'п',
    'r':'р',
    's':'с',
    't':'т',
    'u':'у',
    'f':'ф',
    'h':'х',
    'c':'ц',
    'цх':'ч',
    'сх':'ш',
    'шх':'щ',
    'y':'ы',
    'ые':'э',
    'ыу':'ю',
    'ыа':'я',
    '\'':'ь',
    '{':'«',
    '}':'»'
}

class Toolbar:
    def __init__(self):
        sg.ChangeLookAndFeel('Black')
        
        layout = [
            [sg.InputText(change_submits=True, key='main', size=(75,3), focus=True, font=('Helvetica', 20))]
        ]

        window = sg.Window('Транслит', layout, no_titlebar=False, keep_on_top=True)
        
        while True:
            (event, value) = window.read()
            if event is None:
                break
            else:
                #sg.Popup(value['main'])
                #sg.Popup(window.FindElement('main'))
                #window.FindElement('main').Update('qq')
                text = value['main']
                for key, val in translit_table.items():
                    text = text.replace(key, val)
                    window.FindElement('main').Update(text.replace(key, val))


t = Toolbar()
