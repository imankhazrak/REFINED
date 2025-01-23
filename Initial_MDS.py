import os
import numpy as np
import pandas as pd

import pickle
import cv2
import matplotlib.pyplot as plt
import math

import scipy.misc

from sklearn.manifold import MDS
from sklearn.metrics.pairwise import euclidean_distances

import Toolbox
from Toolbox import two_d_eq, Assign_features_to_pixels
from config import *

########################################################

#%% Loading the data
data_dir = args.data_dir
output_file = args.output_file

# Check if the directory exists
if not os.path.isdir(data_dir):
    raise ValueError(f"The specified data directory does not exist: {data_dir}")

Feat_DF = pd.read_csv(args.data_dir).dropna(thresh=50)

X = Feat_DF.values; X = X[:,2:]
original_input = pd.DataFrame(data = X)                              # The MDS input should be in a dataframe format
feature_names_list = original_input.columns.tolist()                 # Extracting feature_names_list (gene_names or descriptor_names)
print(">>>> Data  is loaded")

#%% MDS
nn = math.ceil(np.sqrt(len(feature_names_list))) 				     # Image dimension
Nn = original_input.shape[1] 										 # Number of features
    
transposed_input = original_input.T 							     # The MDS input data must be transposed , because we want summarize each feature by two values (as compard to regular dimensionality reduction each sample will be described by two values)
Euc_Dist = euclidean_distances(transposed_input) 					 # Euclidean distance
Euc_Dist = np.maximum(Euc_Dist, Euc_Dist.transpose())   			 # Making the Euclidean distance matrix symmetric

embedding = MDS(n_components=2)										 # Reduce the dimensionality by MDS into 2 components
mds_xy = embedding.fit_transform(transposed_input)					 # Apply MDS			

print(">>>> MDS dimensionality reduction is done")

eq_xy = two_d_eq(mds_xy,Nn)
Img = Assign_features_to_pixels(eq_xy,nn,verbose=1)					# Img is the none-overlapping coordinates generated by MDS

#%% To be saved for hill climbing
Desc = Feat_DF.columns.tolist();    Desc = Desc[2:]					# Drug descriptors name
Dist = pd.DataFrame(data = Euc_Dist, columns = Desc, index = Desc)	# Generating a distance matrix which includes the Euclidean distance between each and every descriptor
data = (Desc, Dist, Img	)  											# Preparing the hill climbing inputs

with open(output_file, 'wb') as f:					# The hill climbing input is a pickle, therefore everything is saved as a pickle to be loaded by the hill climbing
    pickle.dump(data, f)