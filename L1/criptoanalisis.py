diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
diccionario.split

x='A'
cont=0
n=0
letras=[]
nums=[]

texto = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
texto.split

for i in diccionario:
    for j in texto:
        if (i==j):
            cont=cont+1
    
    nums.append(cont)
    letras.append(i)
    cont=0

print(nums)
print(letras)
nums.sort(reverse=True)            
print (nums)

print(len(letras))
print(len(nums))

texto_nuevo= texto.replace("X","e")
texto_nuevo= texto_nuevo.replace("E","a")
texto_nuevo= texto_nuevo.replace("J","n")
texto_nuevo= texto_nuevo.replace("T","l")
texto_nuevo= texto_nuevo.replace("A","d")

texto_nuevo= texto_nuevo.replace("P","m")
texto_nuevo= texto_nuevo.replace("V","y")
texto_nuevo= texto_nuevo.replace("I","o")

texto_nuevo= texto_nuevo.replace("K","r")
texto_nuevo= texto_nuevo.replace("Z","u")
texto_nuevo= texto_nuevo.replace("R","c")
texto_nuevo= texto_nuevo.replace("C","i")

texto_nuevo= texto_nuevo.replace("N","s")
texto_nuevo= texto_nuevo.replace("L","z")
texto_nuevo= texto_nuevo.replace("Q","b")

texto_nuevo= texto_nuevo.replace("U","g")

texto_nuevo= texto_nuevo.replace("H","t")
texto_nuevo= texto_nuevo.replace("G","j")

texto_nuevo= texto_nuevo.replace("S","q")

texto_nuevo= texto_nuevo.replace("D","p")
texto_nuevo= texto_nuevo.replace("F","x")
texto_nuevo= texto_nuevo.replace("O","f")


print(texto_nuevo)