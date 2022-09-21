outfile = open('info_security.txt','r')
infile = ('encrypted.txt','w')

symbols = {'A': '~','a':'`', 'B': '!','b':'1', 'C':'@','c':'2','D':'#','d':'3','E':'$','e':'4','F':'%','f':'5','G':'^','g':'6','H':'&','h':'7','I':'*','i':'8','J':'(','j':'9','K':')','k':'0','L':'_','l':'-','M':'+','m':'=','N':'{','n':'[','O':'}','o':']','P':':','p':';','Q':'<','q':',','R':'>','r':'.','S':'?','s':'/','T':'01','t':'02','U':'03','u':'04','V':'05','v':'06','W':'07','w':'08','X':'09','x':'10','Y':'11','y':'12','Z':'13','z':'14'}
outfile_read = outfile.read()
for code in outfile_read():
    if code in symbols:
        infile.write(symbols[code])
    else:
        infile.write(code)

infile.close()
outfile.close()
