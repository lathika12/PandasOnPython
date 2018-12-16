import numpy as np
import pandas as pd
print("Trying to create a series");
heights_A = [176.2, 158.4, 167.6, 156.2, 161.4 ];
HeightsA = pd.Series(heights_A , index =["s1", "s2", "s3", "s4", "s5"]);
print("Shape : ", HeightsA.shape);
print("XXXXXX task 2 XXXXX");
weights_A=[85.1, 90.2, 76.8, 80.4, 78.9];
WeightsA = pd.Series(weights_A , index =["s1", "s2", "s3", "s4", "s5"]);
print("Datatype of series : " , WeightsA.dtype);
print("XXXX Creating data frame XXXX ");
df_A = {'Student_height' : HeightsA , 'Student_weight' : WeightsA};
df = pd.DataFrame(df_A);
print(df.index);
