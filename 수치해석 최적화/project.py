import sys, os

sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict  # collections 모듈 내 OrderedDict 로드
from optimizer import *  # 직접 제작한 optimizer 모듈 로드


# def f(x, y):
#     return x**2 / 20.0 + y**2
#
#
# def df(x, y):
#     return x / 10.0, 2.0*y

def f(x, y):
    return (1 - x)**2 + 100.0 * ((y - x**2)**2)
def df(x, y):
    # f의 도함수 (미분)
    return (2.0 * (x - 1) - 400.0 * x * (y - x**2), 200.0 * (y - x**2))


init_pos = (-2.0, 2.0)
params = {}
params['x'], params['y'] = init_pos[0], init_pos[1]
grads = {}
grads['x'], grads['y'] = 0, 0

optimizers = OrderedDict() # 여러 가중치를 테스트 하기 위함
optimizers["Momentum"] = Momentum(lr=0.000512) # 최종
# 최종 0.000512 (-2.0, 2.0)
idx = 1

for key in optimizers:
    optimizer = optimizers[key]
    x_history = []
    y_history = []
    params['x'], params['y'] = init_pos[0], init_pos[1]

    for i in range(50):
        x_history.append(params['x'])
        y_history.append(params['y'])

        grads['x'], grads['y'] = df(params['x'], params['y'])
        optimizer.update(params, grads)

    xx = np.arange(-10, 10, 0.01)
    yy = np.arange(-5, 5, 0.01)
    X, Y = np.meshgrid(xx, yy)
    Z = f(X, Y)

    # 그래프 그리기
    plt.subplot(1, 1, idx)
    idx += 1
    levels = np.logspace(-2, 3, 15)
    plt.plot(x_history, y_history, 'o-', color="black")

    plt.contourf(X, Y, Z, alpha=0.2, levels=levels)
    plt.contour(X, Y, Z, colors="gray",
                levels=[0.4, 3, 15, 50, 150, 500, 1500, 5000])
    plt.plot(1, 1, 'ro', markersize=10, markeredgecolor="cornflowerblue")
    plt.xlim(-4, 4)
    plt.ylim(-3, 3)

    plt.xticks(np.linspace(-4, 4, 9))
    plt.yticks(np.linspace(-3, 3, 7))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("2D Rosenbrock func ")

plt.show()
print(x_history[-1],y_history[-1])
