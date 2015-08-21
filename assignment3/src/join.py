import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    table    = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(key, records):
    # key: order_id
    # value: list of records
    for r in records:
        if r[0] == "order":
            for u in records:
                if(r[0]!=u[0]):
                    mr.emit(r+u)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
