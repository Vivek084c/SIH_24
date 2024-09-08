import sys
import json
import ast

# data_to_pass_back = "Send this to node process."
# input = ast.literal_eval(sys.argv[1])
# output = input
# output.append(data_to_pass_back)
# print(json.dump(output))

# sys.stdout.flush()

data_to_pass_back = "vivek this to node process."
input = sys.argv[1]
output = data_to_pass_back
print(output)
sys.stdout.flush()