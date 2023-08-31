'''
Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y 
 dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
'''
def decoder(string):

    
    # Creamos un diccionario con el alfabeto en codigo morse
    morse = {"A":"·-","B":"-···","C":"-·-·","D":"-··","E":"·","F":"··-·","G":"--·","H":"····",
            "I":"··","J":"·---","K":"-·-","L":"·-··","M":"--","N":"-·","Ñ":"--·--","O":"---",
            "P":"·--·","Q":"--·-","R":"·-·","S":"···","T":"-","U":"··-","V":"···-","W":"·--",
            "X":"-··-","Y":"-·--","Z":"--··","0":"-----","1":"·----","2":"··---","3":"···--",
            "4":"····-","5":"·····","6":"-····","7":"--···","8":"---··","9":"----·","·":"·-·-·-",
            ",":"--··--","?":"··--··",'"':"·-··-·","/":"-··-·", " ":"  "}

    # alfabeto de codigo morse
    natural = '·-'

    # variables que almacena la decodificacion
    code_morse = ''
    decoder_text = ''

    # mensaje en lenguaje natural
    if string[0] not in natural:
        string = string.upper()

        for i in string:
            if i == ' ':
                decoder_text += ' '
            else:
                decoder_text += morse[i] + ' '
        return decoder_text

    # mensaje en codigo morse    
    else:
        text_new = string.replace('  ',',bb,')
        text_new = text_new.replace(' ',',')
        text_new = text_new.replace('bb','  ')
        string = text_new.split(',')
        for i in string:
            for key, value in morse.items():
                if value == i:
                    decoder_text += key 
        return decoder_text
    
print(decoder('Hola Mundo'))
print(decoder('···· --- ·-·· ·-  -- ··- -· -·· ---'))