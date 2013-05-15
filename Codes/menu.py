import os
import sys
import time
from checksum import check_cs
from berger import check_ber
#options contains an (code number, code name, code program) array
options = [(1,'Checksum',check_cs),(2,'Berger',check_ber)]

def select_op(op):
	for o in options:
		if(op in o):
			return (True, o[2])
	return (False, None)


def print_header():

	print "  __________________________________"
	print " | >>  Codes comparison program  << |"
	print " |__________________________________|"



def csv_to_matrix(f_name):
	opened = False
	matrix = []
	try:
		f = open(f_name, 'r')
		opened = True
		lines = f.readlines()
		num_rows = len(lines)
		if(num_rows == 0):
			opened = False
		else:
			num_cols = len(lines[0])

	except IOError:
		opened = False
		print '\nError: Inexistent or empty file'

	if opened:
		# Parsing csv format
		for l in lines:
			row = l.strip().split(',')
			row = filter(None,row)
			row = map(int,row)
			matrix.append(row)

	return (opened, matrix)


def sel_code():
	correct = False
	while not correct:
	
		print " |__________________________________|"
		print " | Select the code you want to try: |"
		for o in options:
			print ' | %d) %s' % (o[0],o[1]),
			print ' '*(34 - 5 - len(str(o[0])) - len(o[1])),
			print '|'
		print " |> ",
		code_n = int(sys.stdin.readline().strip())
		(correct, code) = select_op(code_n)

		print '|'+' '*34 +'|'

	return code

def the_end():
	print " |             THE END              |"
	print " |__________________________________|"


def wait():

	print ' | Sleep time!                      |'
	time.sleep(0.5)
	print ' |                    zZzZ...       |'
	time.sleep(1)
	print ' |       zZzZ...                    |'
	time.sleep(1)
	print ' | I\'m back!                        |'

