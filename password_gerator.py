chave = input("digot a senha")
senha = ""

for letra in chave:
    if letra in 'Aa':
        senha = senha + '10'
    elif letra in 'Bb':senha = senha + '11'
    elif letra in 'Cc':senha = senha + '13'
    elif letra in 'Dd':senha = senha + '14'
    elif letra in 'Ee':senha = senha + '15'
    elif letra in 'Ff':senha = senha + '16'
    elif letra in 'Gg':senha = senha + '17'
    elif letra in 'Hh':senha = senha + '18'
    elif letra in 'Ii':senha = senha + '19'
    elif letra in 'Jj':senha = senha + '%'
    elif letra in 'Kk':senha = senha + '*'
    elif letra in 'Ll':senha = senha + ')'
    elif letra in 'Mm':senha = senha + '#'
    elif letra in 'Nn':senha = senha + '('
    elif letra in 'Oo':senha = senha + '!'
    elif letra in 'Pp':senha = senha + '$'
    elif letra in 'Qq':senha = senha + '¨'
    elif letra in 'Rr':senha = senha + '&'
    elif letra in 'Ss':senha = senha + '"'
    elif letra in 'Tt':senha = senha + '_'
    elif letra in 'Uu':senha = senha + '+'
    elif letra in 'Vv':senha = senha + '='
    elif letra in 'Ww':senha = senha + '-'
    elif letra in 'Xx':senha = senha + '?'
    elif letra in 'Yy':senha = senha + '/'
    elif letra in 'Zz':senha = senha + '}'

print(senha)