{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome!\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please enter the intial velocity: 5\n",
      "Please enter in the angle at which it was launched: 0.75\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time taken is 0.6955497551258513\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# importing required modules \n",
    "import matplotlib.pyplot as plt \n",
    "import numpy as np \n",
    "import math as m\n",
    "print(\"Welcome!\")\n",
    "\n",
    "u = float(input(\"Please enter the intial velocity:\"))\n",
    "A = float(input(\"Please enter in the angle at which it was launched:\"))\n",
    "\n",
    "time = (2*u*m.sin(A))/9.8 \n",
    "\n",
    "print(\"Time taken is\",time)\n",
    "# function to generate coordinates \n",
    "def create_plot(ptype): \n",
    "    # setting the x-axis vaues \n",
    "    x =  np.arange(0, time, 0.1)\n",
    "      \n",
    "    # setting the y-axis values \n",
    "    if ptype == 'range': \n",
    "        y = (9.8*x*x)/(2*np.tan(A))\n",
    "    elif ptype == 'height': \n",
    "        y = (x*x*9.8)/8\n",
    "    return(x, y) \n",
    "  \n",
    "# setting a style to use \n",
    "plt.style.use('fivethirtyeight') \n",
    "  \n",
    "# create a figure \n",
    "fig = plt.figure() \n",
    "  \n",
    "# define subplots and their positions in figure \n",
    "plt1 = fig.add_subplot(221) \n",
    "plt2 = fig.add_subplot(222) \n",
    "  \n",
    "# plotting points on each subplot \n",
    "x, y = create_plot('range') \n",
    "plt1.plot(x, y, color ='r') \n",
    "plt1.set_title('Range vs Time') \n",
    "  \n",
    "x, y = create_plot('height') \n",
    "plt2.plot(x, y, color ='b') \n",
    "plt2.set_title('Height ') \n",
    "\n",
    "fig.subplots_adjust(hspace=.5,wspace=0.5) \n",
    "  \n",
    "# function to show the plot \n",
    "plt.show()\n",
    "         "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
