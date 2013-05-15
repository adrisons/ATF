import os
import sys
import time

options = [1, 2]

def select_op(op):
	if op in options:
		return True
	return False

def print_menu():

	print "  __________________________________"
	print " | >> Multiply matrixes program  << |"
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


def sel_matrix():
	opened = False
	matrix = []
	while not opened:
	
		print " |__________________________________|"
		print " | Insert the name of the file      |"
		print " | containing the matrix(csv format)|"
		print " |> ",
		f_name = sys.stdin.readline().strip()
		actual_path = os.getcwd()
		if(actual_path not in f_name):
			f_name = actual_path + '/' + f_name
		print "| Loaded!                          |"			
#		print '%s' % f_name
		(opened,matrix) = csv_to_matrix(f_name)

	return (matrix, f_name)
def the_end():
	print " |             THE END              |"
	print " |__________________________________|"

def print_error_dimensions():
	print " | Error: Cannot multiply the two   |"
	print " | matrixes. Incorrect dimensions.  |"
	print " | Try again...                     |"
	

def wait():

	print ' | Sleep time!                      |'
	time.sleep(0.5)
	print ' |                    zZzZ...       |'
	time.sleep(1)
	print ' |       zZzZ...                    |'
	time.sleep(1)
	print ' | I\'m back!                        |'

