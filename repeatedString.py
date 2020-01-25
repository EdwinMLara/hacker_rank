from math import ceil

def repeatedString(s, n):
    if ('a' in s):
        tam_str = len(s)
        if tam_str == 1:
            return n
        else:
            aux = divmod(n,tam_str)
            num_a = s.count('a')*aux[0]
            aux_str_final =  s[0:aux[1]]
            num_a_aux = aux_str_final.count('a')
            return (num_a + num_a_aux)
    else:
        return 0

s = 'aba'
s2 = 'a'
s3 = 'ceebbcb'
s4 = 'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm'
print(repeatedString(s4,736778906400))