from behave import when,given,then


@given(u'A Number "{arg1}"')
def step_num_one(context, arg1):
    print("The value of A is {}".format(arg1))
    #return context.A


@when(u'Added to Number "{arg2}"')
def step_second_number(context, arg2):
    print("The value of B is {}".format(arg2))
    #return B


@then(u'Sum of {arg1} and {arg2} is {arg3}')
def step_display_sum(context, arg1 , arg2 , arg3):
    #print(type(arg3))
    sum=int(arg1)+int(arg2)
    #print(sum)
    #print("The sum of {},{} is {}".format(A,B,C))
    assert int(arg3)==sum

