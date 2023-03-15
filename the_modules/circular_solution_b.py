def display_text_b(msg):
    print(msg)


def call_a():
    import circular_solution_a

    circular_solution_a.display_text_a("Hello a! I just imported you")


# call_a()

if __name__ == '__main__':
    call_a()

# call_a()
