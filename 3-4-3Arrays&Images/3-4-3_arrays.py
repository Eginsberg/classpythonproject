import os.path
import matplotlib.pyplot as plt

directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'cat1-a.gif')

img = plt.imread(filename)