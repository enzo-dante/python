# regular expressions (regex) = describing patterns withing search strings

__cheat sheet__

https://www.rexegg.com/regex-quickstart.html

# writing basic regular expression

regex is case sensitive

/h/ = 'h' and not 'H'

> regular expression tester that catches python nuances

https://pythex.org/

__regex special characters__

\ = escape special meaning of a character

. = matches everything

\. = string value of a period

\d = digit 0-9

\w = letter, digit, or underscore

\s = whitespace character

\D = not a digit

\W = not a word character

\S = not a whitespace character

__quantifiers: specify how many times something should occur in a pattern__

+ = one or more

{x} = exactly x times.

    {3} = 3 times

{3,5} = 3 to 5 times

{4,} = four or more times

* = zero or more times

? = once or none (optional)

[] = character classes allow us to specify groups/ranges of characters

[^] = anything that is NOT the specified characters in the brackets with the carrot symbol

    [^k] = anything but the lowercase letter k

^ = carrot anchor species the search string has to start with defined regular expression

    ^\d{3}

'$' = dollar sign boundary denotes the end of string or line

\b = word boundary

ex: \b\w+\b = select only and every word

    'hello world I am typing'

> validating emails

__examples of different emails__

colt@gmail.com
carly.simon@yahoo.com
shoe_queen91@hello.net
david+lee+roth@hotmail.com
rosa-98@meals.org

> general email pattern sequence:
    > starts with 1 or more letter, number, plus sign, dash, underscore, or period
    > a single @ sign
    > 1 or more letter, number, or dash
    > a single dot
    > ends with 1 or more letter, number, dash or period

__POTENTIAL REGULAR EXPRESSION FOR EMAILS__

(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

__pattern explanation:__

    ^ = search string has to start with any of the defined characters in the bracket

    [a-zA-Z0-9_.+-] = allow lower case a-z, upper case a-z, 0-9, underscore, period, plus sign, or dash

    + = allow one or more of the specified characters in the defined bracket

    @ = a single 'commercial at' sign

    [a-zA-Z0-9-] = allow lower case a-z, upper case a-z, 0-9 or dash

    + = allow one or more of the specified characters in the defined bracket

    \. = a single dot that (must use escape backslash to specify)

    [a-zA-Z0-9-.] = allow lower case a-z, upper case a-z, 0-9, underscore, dash or period

    + = allow one or more of the specified characters in the defined bracket

    $ = search string has to end with any of the defined characters in the bracket

> other potential use cases

1. credit card number validation
2. phone number validation
3. advanced find/replace in text
4. formatting text/output
5. syntax highlighting