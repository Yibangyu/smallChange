#!/usr/bin/python

row_line = input()
P,A = row_line.split()

P_list = [int(x) for x in P.split('.')]
A_list = [int(x) for x in A.split('.')]

P_knut = P_list[0]*17*29 + P_list[1]*29 + P_list[2]
A_knut = A_list[0]*17*29 + A_list[1]*29 + A_list[2]

result_knut = abs(A_knut - P_knut)

gallen = result_knut // (17*29)
sickle = (result_knut - gallen*17*29) // 29
knut = result_knut - gallen*17*29 - sickle*29

string = str(gallen)+'.'+str(sickle)+'.'+str(knut)

if A_knut >= P_knut:
	print(string)
else:
	print('-'+string)



