
card1 = ['purple', 'empty', 'rect', 'one']
card2 = ['green', 'empty', 'rect', 'two']
card3 = ['red', 'empty', 'rect', 'three']

for i in range(4):
    if card1[i] == card2[i] == card3[i] or card1[i] != card2[i] != card3[i]:
        print('AAI')
