import base64
def modInverse(a, m) : 
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
  
    while (a > 1) : 
  
        # q is quotient 
        q = a // m 
  
        t = m 
  
        # m is remainder now, process 
        # same as Euclid's algo 
        m = a % m 
        a = t 
        t = y 
  
        # Update x and y 
        y = x - q * y 
        x = t 
  
  
    # Make x positive 
    if (x < 0) : 
        x = x + m0 
  
    return x

def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a)

def lcm(a,b): 
    print (gcd(a,b))
    
p=109038277498642222804829973956413924259
q=160918435531417596852233325112195308824899
p1=p-1
q1=q-1
#print (gcd(p1,q1))
x=2
h=p1*q1
h=h//2
#print(h)
n=17546269028122080511909946954370136596673185679926898876699010669399066479324841
c=1806487421168675061093077619826276440395602338629619654715374081065862642738711
e=65537
d=modInverse(e,h)
x=d*e
print(x%h)
m=pow(c,d,n)
print (m)
print (hex(m))



