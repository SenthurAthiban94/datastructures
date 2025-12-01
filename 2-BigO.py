def constant(n=1):    # O(1) - Constant
    print(f'Constant O(1): {n*n}\n')

def linear(n=1):      # O(N) - Linear
    for i in range(n):
        print(i)
    print(f'Linear O(N)\n')

def dropconstant(n=1):      # O(2N) - Drop Constant -> O(N) -> Linear
    for i in range(n):      # O(N)
        print(i)
    for j in range(n):      # O(N)
        print(j)
    print(f'O(2N) -> Drop Constant -> O(N) Linear\n')

def quadratic(n=1):          # O(N²) - Quadratic
    for i in range(n):       
        for j in range(n):
            print(i,j)
    print(f'Quadratic O(N²)\n')

def drop_non_dominant_terms(n):  # O(N²+N) -> O(N²)
    for i in range(n):          
        for j in range(n):      # O(N²)
            print(i,j)
    
    for k in range(n):          # O(N)
        print(k)
    print(f'Quadratic O(N²+N) -> O(N²)\n')

def lograthmic(n=8):
    print(f'Lograthmic O(2^?) = N  -> Log2(8) = 3\n')

# Big O
constant(4)
linear(100)
dropconstant(100)
quadratic(2)
drop_non_dominant_terms(2)
lograthmic(2)