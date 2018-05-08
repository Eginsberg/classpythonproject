'''Acesses file in the current directory'''
import os.path

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')

'''Acesses image'''
import matplotlib.pyplot as plt 

# Read the image data into an array
img = plt.imread(filename)


'''Displays image'''
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')

# Show the figure on the screen
fig.show()






