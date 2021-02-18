import numpy as np
import matplotlib.pyplot as plt
from mltools import plot_data, plot_frontiere, make_grid, gen_arti

def mse(w,x,y):
    # a implémenter
    x, y = x.reshape(len(y), -1), y.reshape(-1, 1)
    w = w.reshape(-1, 1)
    return ((x.dot(w) - y)**2).mean()


def reglog(w,x,y):
    x, y = datax.reshape(len(y), -1), datay.reshape(-1, 1)
    w = w.reshape(-1, 1)
    h = x.dot(w)
    sig = 1 / (1 + np.exp(-h))
    cost = -(1 / x.shape[0]) * np.sum(y * np.log(sig) + (1 - y) * np.log(1 - sig))
    return cost


def mse_grad(w,x,y):
    x, y = datax.reshape(len(y), -1), datay.reshape(-1, 1)
    w = w.reshape(-1, 1)
    return (x.T.dot(x.dot(w) - y)) * (2 / y.size)

def reglog_grad(w,x,y):
    x, y = datax.reshape(len(y), -1), datay.reshape(-1, 1)
    w = w.reshape(-1, 1)
    res = x.dot(w)
    sig = 1 / (1 + np.exp(-res))
    return (1 / x.shape[0]) * (np.dot(x.T, sig) - y)

def grad_check(f,f_grad,N=100):

    pass


def descente_gradient(datax,datay,f_loss,f_grad,eps,iter):
    w = np.zeros(datax.shape[1])
    costs = []

    for i in range(iter):
        cost = f_loss(w,datax,datay)
        costs.append(costs)
        gradient = f_grad(w,datax,datay)
        w -= gradient * eps

    w_opti = np.argmin(w)
    return w_opti, w, costs


##
##
if __name__=="__main__":
 ## Tirage d'un jeu de données aléatoire avec un bruit de 0.1
    datax, datay = gen_arti(epsilon=0.1)
    ## Fabrication d'une grille de discrétisation pour la visualisation de la fonction de coût
    grid, x, y = make_grid(xmin=-2, xmax=2, ymin=-2, ymax=2, step=100)
    
    plt.figure()
    ## Visualisation des données et de la frontière de décision pour un vecteur de poids w
    w = np.random.randn((datax.shape[1],1))
    plot_frontiere(datax,lambda x : np.sign(x.dot(w)),step=100)
    plot_data(datax,datay)

    ## Visualisation de la fonction de coût en 2D
    plt.figure()
    plt.contourf(x,y,np.array([mse(w,datax,datay).mean() for w in grid]).reshape(x.shape),levels=50)
    