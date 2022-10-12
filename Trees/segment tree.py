'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
leng = 1000; 
  

tree = [0] * (2 * leng); 
  

def build(arr) :
  
    
    for i in range(n) : 
        tree[n + i] = arr[i]; 
      
   
    for i in range(n - 1, 0, -1) : 
        tree[i] = tree[i << 1] + tree[i << 1 | 1]; 
  
 
def updateTreeNode(p, value) : 
      
     
    tree[p + n] = value; 
    p = p + n; 
      
  
    i = p;
      
    while i > 1 :
          
        tree[i >> 1] = tree[i] + tree[i ^ 1]; 
        i >>= 1; 
  
 
def query(l, r) : 
  
    res = 0; 
      
    
    l += n;
    r += n;
      
    while l < r :
      
        if (l & 1) :
            res += tree[l]; 
            l += 1
      
        if (r & 1) :
            r -= 1;
            res += tree[r]; 
              
        l >>= 1;
        r >>= 1
      
    return res; 
  

if __name__ == "__main__" : 
  
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14]; 
  
    
    n = len(a); 
      
     
    build(a); 
      
    
    print(query(3, 9)); 
      
  
    updateTreeNode(4, 11); 
      
  
    print(query(3, 9)); 