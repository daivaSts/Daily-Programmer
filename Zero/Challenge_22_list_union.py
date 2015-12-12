'''
[3/10/2012] Challenge #22 [easy]
Write a program that will compare two lists, and append any elements in the second list that doesn't exist in the first.
input: ["a","b","c",1,4,], ["a", "x", 34, "4"]
output: ["a", "b", "c", 1, 4,"x",34, "4"]

'''

a = ["a", "b", "c", 1, 4]
b = ["a", "x", 34, "4"]

def challenge22(a,b):
	z = list(set.union(set(a),set(b)))
	return z

if __name__ == "__main__":
    print challenge22(a,b)