import bz2
import pickle

# Path to the compressed model file
input_file_path = 'model.pkl.bz2'
# Path to the decompressed model file
output_file_path = 'model_decompressed.pkl'

with bz2.BZ2File(input_file_path, 'rb') as f_in, open(output_file_path, 'wb') as f_out:
    pickle.dump(pickle.load(f_in), f_out)