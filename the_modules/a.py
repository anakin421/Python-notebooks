print(f"out side A's display method")

global a_show,a_display
a_show = 0
a_display = 0

def show():
    global a_show
    a_show += 1 

    import b
    b.display()

def display():
    global a_display
    a_display += 1 

    print(f"in side A's display method")


print(f"   show() of A: {a_show}")
print(f"   display() of A: {a_display}")

print(__name__)
show()

# if __name__ == '__main__':
# 	show()


# print("ola A")
# import b

# print("end of A")