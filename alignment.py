import stdarray
import stdio

# Read x, y, and opt from standard input.
x = stdio.readString()
y = stdio.readString()
opt = stdarray.readInt2D()

# Compute M and N.
M = len(x)
N = len(y)

# Write edit distance between x and y (i.e. the value of opt[0][0])
stdio.writeln("Edit distance = " + str(opt[0][0]))

# Recover and write an optimal alignment, starting at opt[0][0] and ending
# at opt[M - 1][N - 1].
i = 0
j = 0
# If opt[i][j] equals opt[i + 1][j] + 2, then align x[i] with a gap and
# penalty of 2, and increment i by 1.
while i < M and j < N:
    if(opt[i][j] == opt[i + 1][j] + 2):
        stdio.writeln(x[i] + " - 2")
        i += 1
# Otherwise if opt[i][j] equals opt[i][j + 1] + 2, then align a gap with
# y[j] and penalty of 2, and increment j by 1.
    elif(opt[i][j] == opt[i][j + 1] + 2):
        stdio.writeln("- " + y[j] + " 2")
        j += 1
# Otherwise, align x[i] with y[j] and penalty of 0/1 based on whether x[i]
# and y[j] match or not, and increment both i and j by 1.
    else:
        if(x[i] == y[j]):
            stdio.writeln(x[i] + " " + y[j] + " 0")
        else:
            stdio.writeln(x[i] + " " + y[j] + " 1")
        i += 1
        j += 1

# If x (or y) is exhausted before y (or x), align a character from y (or
# x) with a gap and penalty of 2.

# x is exhausted before y.
while j < N:
    if(opt[i][j] == opt[i][j + 1] + 2):
        stdio.writeln("- " + y[j] + " 2")
        j += 1

# y is exhausted before x.
while i < M:
    if(opt[i][i] == opt[i + 1][j] + 2):
        stdio.writeln(x[i] + " - 2")
        i += 1
