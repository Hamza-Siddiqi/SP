# to check if the cordinates are just right
def isValid (x,y):
	xx=x+1
	yy=y+1
	if (x < 0 or x > 7 ) or (y < 0 or y > 7 ) or (xx < 0 or xx > 7 ) or (yy < 0 or yy > 7 ):
		return False
	else:
		return True


#to check if we have found 2 by 2 matrix 
def is_equal_matrix(x,y,inputarr,arr):
	xx=x+1
	yy=y+1
	if(inputarr[0][1] ==arr[x][yy] and inputarr[1][0] == arr[xx][y] and inputarr[1][1] == arr[xx][yy]):
		return True
	else:
		return False


#to Print array of 2 by 2 with index values 
def printFoundArray(x,y,arr):
	print("At index {0} {1} value = {2} ".format(x,y,arr[x][y]))
	print("At index {0} {1} value = {2} ".format(x,y+1,arr[x][y+1]))
	print("At index {0} {1} value = {2} ".format(x+1,y,arr[x+1][y]))
	print("At index {0} {1} value = {2} ".format(x+1,y+1,arr[x+1][y+1]))


#main function 

# 8 by 8 matrix 
n=8
a=[[0] * n for i in range(n)]
for i in range(n):
	for j in range(n):
		a[i][j]=i



# 2 by 2 matrix
n=2
ar=[[0] * n for i in range(n)]
for i in range(n):
	for j in range(n):
		print("Value at index {0} {1}".format(i,j))			
		num=input("Enter num : ")
		nn=str(num)
		while(not(nn.isdigit())):			
			print("Inavlid Number ")	
			print("Value at index {0} {1}".format(i,j))			
			num=input("Enter num : ")
			nn=str(num)	
		ar[i][j]=int(num)






#displaying the array you are sreaching for 
print("The 2 by 2 array you entered")
for row in ar:
	print(" ".join([str(elem) for elem in row])) 


		
#to keep track if we found the array or not 
f=True
# a loop traversing the whole 8 by 8 array to find the first element of 2 by 2 element 
n=8
for i in range(n):
	for j in range(n):			
		if(ar[0][0] == a[i][j]):
			if(isValid (i,j)):
				#print("{0} and {1} are valid ".format(i,j))
				if(is_equal_matrix(i,j,ar,a)):
					print("Given matrix found here ({0},{1})".format(i,j))			
					printFoundArray(i,j,a)
					f=False
					break
if(f==True):
	print("No Array was Found")
