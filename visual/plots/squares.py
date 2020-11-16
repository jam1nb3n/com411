import matplotlib.pyplot as plt

def small():
    # (3,3) (4,3) (4,4) (3,4) (3,3)
    x = [3,4,4,3,3]
    y = [3,3,4,4,3]
    plt.plot(x,y,'ro:')



def medium():
    # (2,2) (5,2) (5,5) (2,5) (2,2)
    x = [2,5,5,2,2]
    y = [2,2,5,5,2]
    plt.plot(x,y,'gs--')


def large():
    # (1,1) (6,1) (6,6) (1,6) (1,1)
    x = [1,6,6,1,1]
    y = [1,1,6,6,1]
    plt.plot(x,y,'bp-')


small()
medium()
large()
plt.show()