from menu import print_header
from menu import sel_code
from menu import csv_to_matrix
from menu import the_end

emisor = 'Emisor.csv'
receptor = 'Receptor.csv'

print_header()
checker = sel_code()

code_sent = csv_to_matrix(emisor)[1]
code_recv = csv_to_matrix(receptor)[1]

i1 = checker(code_sent)
print ' | sent:' + i1 + ' '*(28-len(i1)) + '|'
i2 = checker(code_recv)
print ' | recv:' + i2 + ' '*(28-len(i2)) + '|'

if i1 == i2:
	print ' |        > Correct <' + ' '*15 +'|'
else:
	print ' |        > Incorrect <' + ' '*13 +'|'

the_end()