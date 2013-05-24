from menu import sel_matrix
from menu import csv_to_matrix
from menu import print_error_dimensions
from menu import wait
import os
import time

f_res_n = 'result.csv'
f_cp_n = 'checkPoint.txt'
a_name = ''
b_name = ''
actual_path = os.getcwd() + '/'


def get_next_pos(row, col, max_col):
	print 'max_col = %d' % max_col
	print 'BEFORErow,col = %d,%d' % (row,col)
	if(col == max_col):
		row += 1
		col = 0
	else:
		col += 1
	print 'AFTER row,col = %d,%d' % (row,col)
	return (row, col)
def last_row_csv2int(f_name):
	with open(f_name, 'r') as auxF:
		lines = auxF.read().strip().split('\n')
	last_row = lines[-1]
	last_row = last_row.split(',')
	last_row = filter(None,last_row)
	last_row = map(int,last_row)	
	return last_row

def restore_cp(max_col):
	last_row = last_row_csv2int(f_cp_n)
	cp_row = last_row[0]
	cp_col = last_row[1]
#	print 'cp_row = %d\ncp_col = %d\n' % (cp_row,cp_col)
	r_matrix = csv_to_matrix(f_res_n)[1]
	r_row = len(r_matrix) -1
	r_col = len(r_matrix[-1]) -1
	# If the last value in cp was saved in the result file -> next pos
	if(r_col == cp_col):
		(cp_row, cp_col) = get_next_pos(cp_row, cp_col, max_col)
		print 'SAME cols:       col = %d' % r_col
	# If the last value in cp wasn't saved in the result file -> next pos from the result
	elif(cp_col > r_col):
		(cp_row, cp_col) = get_next_pos(r_row, r_col, max_col)
		print 'DIFERENT cols: r_col = %d' % r_col
	return (cp_row, cp_col)

def create_cp(max_col):

	row = 0
	col = 0
	restoring = False
	# If the checkPoint exists, the program was not finished when it failed
	if(os.path.isfile(actual_path + f_cp_n)):
		start = time.time()		
		auxF_cp = open(f_cp_n, 'r')
		lines = auxF_cp.read().strip().split('\n')
		if(len(lines) > 2):
			
			file1 = lines[0]
			file2 = lines[1]
			# Check if it is the right checkPoint
			if( (file1 == a_name and file2 == b_name) or
				(file2 == a_name and file1 == b_name) ):
				print ' | RESTORING...'
				restoring = True
				(cp_row, cp_col) = restore_cp(max_col)
				row = cp_row
				col = cp_col
				f_res = open(f_res_n, 'a')
				f_cp = open(f_cp_n, 'a')
		end = time.time()
		print 't_restauracion=', end-start
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
	f_cp.write(str(col) + ',\n')

	f_cp.close()

def save_res(data, row, col, max_col):
	save_checkpoint(row,col)
#	print 'Guardado CP'
#	time.sleep(2)
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
		print_error_dimensions()
		matrixmult()
		return
	# Create the result matrix
	# Dimensions would be rows_A x cols_B
	C = [[0 for row in range(cols_B)] for col in range(rows_A)]

	
	max_col = cols_B - 1
	(row,col) = create_cp(max_col)
#	print 'row=%d\ncol=%d\n' % (row,col)
	for i in range(row,rows_A):
		for j in range(col,cols_B):
			for k in range(cols_A):
				C[i][j] += A[i][k]*B[k][j]

			save_res(C[i][j], i, j, max_col)
			wait()

	os.remove(actual_path + '/' + f_cp_n)
	return C



def matrixmult():
	global a_name
	global b_name
	(A, a_name) = sel_matrix()
	(B, b_name) = sel_matrix()
	start = time.time()
	Sol = matrixmult_cp(A,B)
	end = time.time()
	print 't_ej=', end-start

