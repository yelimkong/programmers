def solution(n, m) :
    # 최대 공약수 
    def gcd(a, b):
        while b != 0 :
            a, b = b, a % b
        return a
    
    # 최소 공배수
    def lcm(a, b) :
        return (a * b) // gcd(a, b)
    
    return [gcd(n, m), lcm(n, m)]