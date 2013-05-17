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

if checker(code_sent,code_recv):
	print ' |        > Correct <' + ' '*15 +'|'
else:
	print ' |        > Incorrect <' + ' '*13 +'|'

the_end()