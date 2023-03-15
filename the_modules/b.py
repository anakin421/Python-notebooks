print(f"out side B's display method")

global b_show,b_display
b_show = 0
b_display = 0

def show():
    global b_show
    b_show += 1

    import a
    a.display()

def display():
    global b_display
    b_display += 1 

    print(f"in side B's display method")


print(f"   show() of B: {b_show}")
print(f"   display() of B: {b_display}")

show()

# if __name__ == '__main__':
# 	show()


# print("ola B")

# import a

# print("end of B")