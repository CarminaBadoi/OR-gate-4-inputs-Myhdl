from myhdl import *
@block
def OR4(A, B, C, D, Output):
    @always_comb
    def fct_or():
        Output.next=A or B or C or D
    return instances()
@block
def banc_de_test():
    A = Signal(bool(0))
    B = Signal(bool(0))
    C = Signal(bool(0))
    D = Signal(bool(0))
    Output = Signal(bool(0))

    POARTA_OR = OR4(A, B, C, D, Output)
    @instance
    def circuit():
        # 0 0 0 0
        print("A\tB\tC\tD\t\tOutput")
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" %(A, B, C, D, Output))


        # 0 0 0 1
        D.next = 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 0 0 1 0
        C.next, D.next = 1, 0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 0 0 1 1
        C.next, D.next = 1, 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 0 1 0 0
        B.next, C.next, D.next = 1, 0, 0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 0 1 0 1
        B.next, C.next, D.next = 1, 0, 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 0 1 1 0
        B.next, C.next, D.next = 1, 1, 0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 0 1 1 1
        A.next, B.next, C.next, D.next = 0,1, 1, 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 0 0 0
        A.next, B.next, C.next, D.next = 1, 0, 0, 0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 0 0 1
        A.next, B.next, C.next, D.next = 1, 0, 0, 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 0 1 0
        A.next, B.next, C.next, D.next = 1, 0, 1, 0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 0 1 1
        A.next, B.next, C.next, D.next = 1, 0, 1, 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 1 0 0
        A.next, B.next, C.next, D.next = 1,1,0,0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 1 0  1
        A.next, B.next, C.next, D.next = 1, 1, 0,1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


        # 1 1 1 0
        A.next, B.next, C.next, D.next = 1, 1, 1,0
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))



        # 1 1 1 1
        A.next, B.next, C.next, D.next = 1, 1, 1, 1
        yield delay(20)
        print("%d\t%d\t%d\t%d\t\t%d" % (A, B, C, D, Output))


    return POARTA_OR, circuit
sys=banc_de_test()
sys.config_sim(trace=True)
sys.run_sim()