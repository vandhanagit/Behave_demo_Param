Feature: Calculator Functionality
    #test suite
        # n num of test cases
    Scenario Outline: Addition of two numbers <A>,<B>
        Given A Number "<A>"
        When Added to Number "<B>"
        Then Sum of <A> and <B> is <C>

        Examples: Cases
        |A|B|C|
        |3|4|7|
        |5|8|13|
        |1|1|2|
        |6|1|2|


