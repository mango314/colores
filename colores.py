from skimage import io
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = 6,6
 
im = io.imread("filename.jpg") 

#crop
piece = im[1250:2250, 1250:2250,:]

K = 10

xBar = np.floor(255*np.random.random( (K,3) )).astype(int)

for t in range(10):
    print t,
    diff = np.argmin(np.sum((piece[...,...,None,...] - xBar[None,...])**2, axis=3), axis=2)
    xBar = [np.average(piece[np.where(diff==k)],axis=0) for k in range(K) if len(np.where(diff==k)[0] > 0)]
    xBar += [ (255*np.random.random( 3 )).astype(int) for k in range(K - len(xBar))]
    xBar = np.array(xBar)
    xBar = xBar.astype(int)
    
plt.fill([0,1000,1000,0], [0,0,100,100]  , color= 0.95*np.ones(3))
plt.fill([0,0,100,100]  , [0,1000,1000,0], color= 0.95*np.ones(3))

for k in range(K):
    plt.fill(  [100*k,100*k,100*k+50,100*k+50],[0,50,50,0], color= xBar[k]*1.0/255)
    plt.fill(  [0,50,50,0], [100*k,100*k,100*k+50,100*k+50], color= xBar[k]*1.0/255)

plt.grid(True)
plt.xticks( 200*np.arange(5), ['' for k in range(5)])
plt.yticks( 200*np.arange(5), ['' for k in range(5)])

plt.xlim([0,1000])
plt.ylim([1000,0])
io.imshow(piece)
