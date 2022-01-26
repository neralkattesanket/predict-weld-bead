import pandas as pd 
import numpy as np

import tensorflow as tf 
from tensorflow.keras import layers

df = pd.read_csv(
    './aws_a5_1_all.csv' , 
    usecols= lambda x : x in []

)

print(df.head())