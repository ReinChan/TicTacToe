turn = "x"
a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
i = "i"

def main():
    print("|"+ a + "|" + b + "|" + c + "|")
    print("|"+ d + "|" + e + "|" + f + "|")
    print("|"+ g + "|" + h + "|" + i + "|")
main()
def ready(x):
    if a == b == c:
        x = 1
        if a == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x    
    if g == h == i:
        x = 1
        if g == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x      
    if a == d == g:
        x = 1
        if a == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x  
    if c == f == i:
        x = 1
        if c == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x      
    if d == e == f:
        x = 1
        if d == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x    
    if b == e == h:
        x = 1
        if b == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x      
    if a == e == i:
        x = 1
        if a == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x  
    if g == e == c:
        x = 1
        if g == "x":
            print("X Won Game! O LOOSER!")
        else:
            print("O Won Game! X LOOSER!")
        return x 
    if a != "a" and b != "b" and c != "c":
        if d != "d" and e != "e" and f != "f":
            if g != "g" and h != "h" and i != "i":
                x = 1
                print("draw,gk ada yg menang.korang cupu!")
                return x
while ready(0) != 1:    
    ashiap = input(turn + " Turn :")
    if ashiap == "a":
        if turn == "x":
            a = "x"
            turn = "o"
        else:
            a = "o"
            turn = "x"
    if ashiap == "b":
        if turn == "x":
            b = "x"
            turn = "o"
        else:
            b = "o"
            turn = "x"        
    if ashiap == "c":
        if turn == "x":
            c = "x"
            turn = "o"
        else:
            c = "o"
            turn = "x"    
    if ashiap == "d":
        if turn == "x":
            d = "x"
            turn = "o"
        else:
            d = "o"
            turn = "x"
    if ashiap == "e":
        if turn == "x":
            e = "x"
            turn = "o"
        else:
            e = "o"
            turn = "x"
    if ashiap == "f":
        if turn == "x":
            f = "x"
            turn = "o"
        else:
            f = "o"
            turn = "x"        
    if ashiap == "g":
        if turn == "x":
            g = "x"
            turn = "o"
        else:
            g = "o"
            turn = "x"
    if ashiap == "h":
        if turn == "x":
            h = "x"
            turn = "o"
        else:
            h = "o"
            turn = "x"
    if ashiap == "i":
        if turn == "x":
            i = "x"
            turn = "o"
        else:
            i = "o"
            turn = "x"
    main()        
       