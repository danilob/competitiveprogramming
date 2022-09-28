

while True:
    try:
        n_test = int(input())
        for test in range(n_test):
            n_entries, m_lines = list(map(int,input().split()))
            translate = {}
            for entry in range(n_entries):
                japanese = input()
                portuguese = input()
                translate[japanese]  =  portuguese
            for lines in range(m_lines):
                output = []
                text = input().split()
                for fragment in text:
                    if fragment in translate:
                        output.append(translate[fragment])
                    else:
                        output.append(fragment)
                print(' '.join(output))
            print()
    except EOFError:
        break
    except ValueError:
        break