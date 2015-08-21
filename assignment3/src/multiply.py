import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    i = record[1]
    j = record[2]
    val = record[3]
    for k in range(0,5):
        if matrix=="a":
            mr.emit_intermediate((i,k), record)
        else:
            mr.emit_intermediate((k,j), record)

def reducer(key, list_of_values):
    sum = 0
    for v in list_of_values:
        if v[0] == "a":
            for w in list_of_values:
                if w[0] == "b" and v[2]==w[1]:
                    sum += v[3]*w[3]
    mr.emit((key[0],key[1],sum))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
