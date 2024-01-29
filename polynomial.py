class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, sub):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)


class sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)


class div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, sub):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)


poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), sub(Mul(X(), X()), Int(1)))))
print(poly)
poly = Add(Add(Int(4), Int(3)), Add(X(), div(Int(1), sub(Mul(X(), X()), Int(1)))))
print(poly)
poly = Add(Add(Int(4), Int(3)), Add(X(), div(Add(Int(1), Int(99)), sub(Mul(X(), X()), Int(1)))))
print(poly)
