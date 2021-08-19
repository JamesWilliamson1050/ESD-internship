

# Probably better to create a number filter first then do the and filter later
def andFilter(string):
    if '&' in string and 'And' in string:
        return string
    elif '&' in string and 'And' not in string:
        string = string.replace('&', 'And')
    elif 'And' in string and '&' not in string:
        string = string.replace('And', '&')
    if '1 And 2' in string:
        s1 = string.split('1')
        s1 = s1[0]
        s2 = s1 + '2'
        s1 = s1 + '1'
        string = s1, s2
    elif '1 & 2' in string:
        s1 = string.split('1')
        s1 = s1[0]
        s2 = s1 + '2'
        s1 = s1 + '1'
        string = s1, s2

    if 'I And II' in string:
        s1 = string.split('I')
        s2 = s1[0] + 'Ii'
        s1 = s1[0] + 'I'
        string = s1, s2


    return string


def numberFilter(string):
    if '1 And 2' in string:
        s1 = string.split('1')
        s1 = s1[0]
        s2 = s1 + '2'
        s1 = s1 + '1'
        string = s1, s2
    elif '1 & 2' in string:
        s1 = string.split('1')
        s1 = s1[0]
        s2 = s1 + '2'
        s1 = s1 + '1'
        string = s1, s2

    if 'I And II' in string:
        s1 = string.split('I')
        s2 = s1[0] + 'Ii'
        s1 = s1[0] + 'I'
        string = s1, s2
    return string

def colonFilter(string):
    if ';' in string:
        string = string.replace(';', ':')
    elif ':' in string:
        string = string = string.replace(':', ';')
    return string


def bracketFilter(string):
    string = string.lower()

    if "(10 credits)" in string:
        string = string.replace("(10 credits)", '')
    if '(10-credit class)' in string:
        string = string.replace('(10-credit class)', '')
    if "(20 credits)" in string:
        string = string.replace("(20 credits)", '')
    if "(20-credits)" in string:
        string = string.replace("(20-credit class)", '')

    return string


if __name__ == '__main__':
    #print(andFilter('Forensic Science Principles And Practice Parts 1 And 2'))
    #print(andFilter('Chemical Engineering: Fundamentals, Techniques and Tools'))
    print(bracketFilter('Social Research Methods (10-Credit class)'))





