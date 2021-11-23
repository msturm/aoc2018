import sys
file='1.in'

freq = 0
freqs = {}
while True:
    with open(file, 'r') as f:
        for v in f:
            sym = v[0]
            value = int(v[1:])
            
            if sym == '+':
                freq = freq + value
            elif sym == '-':
                freq = freq - value
        
            if freq not in freqs:
                freqs[freq] = 1;
#                print(freqs)
#                print(freq)
            else:
                print(freq) 
                sys.exit(0)


