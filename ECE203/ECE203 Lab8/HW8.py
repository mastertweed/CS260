
files = (input('Enter Input Files then Output File: ')).split()

if len(files) < 2:
    exit("error -- must supply at least one input file and an output file")

out = open(files[-1], 'w+')
out = open(files[-1], 'a')

for i in range(len(files)-1):
    f = open(files[i], 'r')
    out.write(f.read() + '\n')

for param in files[0:-1]:
        print('Input File: %s' % param)

print('Output File: %s' % files[-1])
