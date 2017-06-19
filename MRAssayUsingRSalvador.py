import rpy2
print(rpy2.__version__)
import rpy2.robjects as robj

header = ['spore', 'sc_count', 'sc_pe', 'can_pe', 'mr', 'low', 'high', 'can_counts']
data_by_spore = {}
can_by_spore = {}

with open(r"MRAssayDataSample.csv", 'r') as f_obj:
    reader = f_obj.readlines()
    for line in reader[1:]:
        line = line.split(",")
        data_by_spore[line[0]] = line[1:7]
        can_by_spore[line[0]] = line[7:]

rsum = robj.r["sum"]
psum = rsum(robj.IntVector([1, 2, 3]))
print(psum)
