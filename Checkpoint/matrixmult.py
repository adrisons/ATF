from menu import sel_matrix
from menu import csv_to_matrix
import os
import time

f_res_n = 'result.txt'
f_cp_n = 'checkPoint.txt'
a_name = ''
b_name = ''
actual_path = os.getcwd() + '/'


def wait(i,j):
	if(i==3):
		print 'I\'m going to sleep'
		time.sleep(3)
		print 'I\'m back!'

def restore_cp():
	auxF_cp = open(f_cp_n, 'r')
	lines = auxF_cp.read().strip().split('\n')
	last_row = lines[-1]
	last_row = last_row.split(',')
	last_row = filter(None,last_row)
	last_row = map(int,last_row)
	cp_row = last_row[0]
	cp_col = last_row[1]
	print 'cp_row = %d\ncp_col = %d\n' % (cp_row,cp_col)
	return (cp_row, cp_col)

def create_cp():

	row = 0
	col = 0
	restoring = False
	# If the checkPoint exists, the program was not finished when it failed
	if(os.path.isfile(actual_path + f_cp_n)):
		auxF_cp = open(f_cp_n, 'r')
		lines = auxF_cp.read().strip().split('\n')
		if(len(lines) > 2):
			
			file1 = lines[0]
			file2 = lines[1]
			# Check if it is the right checkPoint
			if( (file1 == a_name and file2 == b_name) or
				(file2 == a_name and file1 == b_name) ):
				print 'RESTORING...'
				restoring = True
				(cp_row, cp_col) = restore_cp()
				row = cp_row
				col = cp_col
				f_res = open(f_res_n, 'a')

	if not restoring:
		f_res = open(f_res_n, 'w')		
	f_cp = open(f_cp_n, 'w')
	f_cp.write(a_name + '\n')
	f_cp.write(b_name + '\n')
	f_cp.close()
	f_res.close()

	return (row, col)

def save_checkpoint(row, col):
	f_cp = open(f_cp_n, 'a')
	f_cp.write(str(row) + ',')
	f_cp.write(str(col) + '\n')

	f_cp.close()

def save_res(data, row, col, max_col):
	save_checkpoint(row,col)

	f_res = open(f_res_n, 'a')
	d = str(data) + ','
	f_res.write(d)
	if(col == max_col):
		f_res.write('\n')
	f_res.close()


def matrixmult_cp (A, B):
	rows_A = len(A)
	cols_A = len(A[0])
	rows_B = len(B)
	cols_B = len(B[0])
	row = 0
	col = 0

	if cols_A != rows_B:
		print "Cannot multiply the two matrices. Incorrect dimensions."
		return
	# Create the result matrix
	# Dimensions would be rows_A x cols_B
	C = [[0 for row in range(cols_B)] for col in range(rows_A)]

	(row,col) = create_cp()

	max_col = cols_B - 1

	for i in range(row,rows_A):
		for j in range(col,cols_B):
			for k in range(cols_A):
				C[i][j] += A[i][k]*B[k][j]

			save_res(C[i][j], i, j, max_col)
			wait(i,j)

	os.remove(actual_path + '/' + f_cp_n)
	return C


def matrixmult():
	global a_name
	global b_name
	(A, a_name) = sel_matrix()
	(B, b_name) = sel_matrix()
	Sol = matrixmult_cp(A,B)
