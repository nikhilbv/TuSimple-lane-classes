import json

json_file = '/home/nikhil/Documents/nodeFormatter/prediction/pred-7-260919_111614_tuSimple.json'
with open(json_file, 'r') as file:
  json_lines = file.readlines()
  line_index = 0
  # print(json_lines)
  print(len(json_lines))
  # Iterate over each image
  # while line_index < len(json_lines):
  for json_line in json_lines:  
    sample = json.loads(json_line)
    # print(sample)
    lanes = sample['lanes']
    h_samples = sample['h_samples']
    
    for i,lane in enumerate(lanes):
      if len(lanes) != len(h_samples):
        # print("Error: In lane[{}], len of x_axis is not equal to len of y_axis".format(i))
        print("Error: In lane[%s], len of x_axis is not equal to len of y_axis"%(i))


    
    