for a in range(0,20):
    for b in range(0, 20):
        for c in range(0, 20):
            for d in range(0, 20):
                for e in range(0, 20):
                    for f in range(0, 20):
                        if a+b+c==d+e+f and a*b*c == d*e*f and a!=b and a!=c and a!=e and a!=f and b!=c and b!=d and b!=e and b!=f and c!=d and c!=e and c!=f and d!=e and d!=f and e!=f :
                            print(a,b,c,d,e,f)
                            # and a != b != c != d != e != f