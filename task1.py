def quad(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = (-b + discriminant ** 0.5) / (2 * a)
        return (int(x),)
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return tuple(sorted((int(x1), int(x2))))

def solution(a, b, c):
    root = quad(a, b, c)
    if root:
        return root
    else:
        return None

print(solution(a=1, b=6, c=5))  
print(solution(a=1, b=4, c=4))  
print(solution(a=1, b=6, c=45)) 