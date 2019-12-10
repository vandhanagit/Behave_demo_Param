@given(u'A Number <A>')
def num_one(context):
    context.A=6
    print("The value of A is {}".format(context.A))
    return context.A

@when(u'Added to Number <B>')
def second_number(context):
    context.B=9
    print("The value of B is {}".format(context.B))
    return context.B


@then(u'Sum of <A> and <B>')
def display_sum(context):
    context.C=context.A+context.B
    print("The sum of {},{} is {}".format(context.A,context.B,context.C))
    assert context.C==15

