'''
1. copy paste the exposure times to input.csv
2. run python plot.py to generate an output file
3. copy paste the pixel values (read by MATLAB isetcam)
   to the generated output file
4. slopes and offsets of the 10000 pixels will be calcalated automatically
   by the excel formulas (already in the generated output file)
'''

ISO = 299

csv = []
with open('input.csv', 'r') as f:
    for line in f:
        csv.append(line)

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cols = []
for i in range(26):
    cols.append(letters[i])

for i in range(26):
    for j in range(26):
        cols.append(letters[i]+letters[j])

for i in range(26):
    for j in range(26):
        for k in range(26):
            cols.append(letters[i]+letters[j]+letters[k])

rc = -8
st = 1
for row in csv[-8:-3]:
    s = [row[:-2]]
    for i in range(10000):
        s.append(',')
        s.append('"=AVERAGE({0}{1}, {0}{2}, {0}{3}, {0}{4}, {0}{5})"'.format(
                    cols[i+1], st, st+5, st+10, st+15, st+20))
    s.append(row[-2:])
    csv[rc] = ''.join(s)
    rc = rc + 1
    st = st + 1 

for i in range(10000):
    csv.append('"=SLOPE({0}27:{0}31,A27:A31)","=INTERCEPT({0}27:{0}31,A27:A31)",=A{1}*0.459/0.204*299/55/1023,=B{1}*0.459/0.204*299/55/1023\r\n'.format(cols[i+1], 35+i))

with open('test_299_dc.csv', 'w') as f:
    for row in csv:
        f.write(row)
