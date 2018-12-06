import sys

def load_grid():
   
    grid = []
    input_str = list(sys.stdin.readline().rstrip())
    grid.append(input_str)
    while( input_str ):
        input_str = list(sys.stdin.readline().rstrip())
        if(len(input_str) > 0):
            grid.append(input_str)
    

    words = []
 
    word_str = list(sys.stdin.readline().rstrip())
    words.append(word_str)
    while(word_str):
        word_str = list(sys.stdin.readline().rstrip())
        if(len(word_str) > 0):
            words.append(word_str)
        

    return grid, words


def search_for_word(grid, word):
    print(grid)
    print("-----------")
    print(word)
    operations = ((1, 0), (-1, 0), (0, 1), (0, -1), 
            (1, 1), (-1, -1), (1, -1), (-1, 1))

    nlines = len(grid)
    ncolumns = len(grid[0])

    for l in range(0, nlines):
        for c in range(0, ncolumns):
            if grid[l][c] != word[0]:
                continue

            for op in operations:
                for letter in range(len(word)):
                    opc = c+op[0]*letter
                    opl = l+op[1]*letter
                    if opc<0 or opc>=ncolumns or opl<0 or opl>=nlines:
                        break
                    if grid[opl][opc] != word[letter]:
                        break
                else:
                    return (word,l, c)


def search_words(grid, words):
    return [search_for_word(grid, word) for word in words]

if __name__ == '__main__':

    positions = search_words(*load_grid())
    print(positions)
    for word, line, column in positions:
        print("{} {} {}".format(word, line, column))

        
        

