#example of argv system argument waorking
import sys

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 1 else 0.5

print(alpha, l1_ratio)

#To check this run cmd as admin then activate the env as: conda activate mlproj
# then: python argv_exp.py  (thus if no value is passed it will take the default value)
# but if assign a new value as:python argv_exp.py 0.9 0.4 then it will take this value for alpha and l1_ratio

