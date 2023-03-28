import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random

from google.colab import drive, files
drive.mount('/gdrive')

N=100;                                                          
m1=[0 0]; s1=[9 0;0 1];                                         
m2=[0 4]; s2=[9 0;0 1];                                         
                                                                
# 클래스 데이터 생성                                                    
X1=randn(N,2)*sqrtm(s1)+repmat(m1,N,1);  %클래스1 데이터 생성           
X2=randn(N,2)*sqrtm(s2)+repmat(m2,N,1);  %클래스2 데이터 생성           
                                                                
figure(1);                                                      
plot(X2(:,1),X2(:,2),'ro'); hold on                             
plot(X1(:,1),X1(:,2),'*');                                      
axls([-10 10 -5 10]);                                           
save data8_9 X1 X2     