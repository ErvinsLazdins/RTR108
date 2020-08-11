count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if line.startswith("X-DSPAM-Confidence:") :
        count=count+1 
    a=line.find('0.')
    b=float((line[a:]))
    total = total + b 
print('Average spam confidence:',total/count) 
