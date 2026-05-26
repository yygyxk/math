import matplotlib.pyplot as plt
import os

os.makedirs('/tmp/math_repo/handouts/images', exist_ok=True)

def draw_fig1():
    fig, ax = plt.subplots(figsize=(4, 4))
    A = (1, 2.5)
    B = (0.2, 1)
    C = (1, 0.2)
    D = (2.5, 0.5)

    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], D[0]], [C[1], D[1]], 'k-', lw=1.5)
    ax.plot([D[0], A[0]], [D[1], A[1]], 'k-', lw=1.5)

    ax.plot([A[0], C[0]], [A[1], C[1]], 'k-', lw=1.2)
    ax.plot([B[0], D[0]], [B[1], D[1]], 'k-', lw=1.2)

    ax.text(A[0]-0.1, A[1]+0.1, 'A', fontsize=14)
    ax.text(B[0]-0.2, B[1], 'B', fontsize=14)
    ax.text(C[0], C[1]-0.2, 'C', fontsize=14)
    ax.text(D[0]+0.1, D[1], 'D', fontsize=14)

    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig('/tmp/math_repo/handouts/images/ptolemy_fig1.png', dpi=300, bbox_inches='tight')
    plt.close()

def draw_fig2():
    fig, ax = plt.subplots(figsize=(4, 4))
    A = (1, 2.5)
    B = (0.2, 1)
    C = (1, 0.2)
    D = (2.5, 0.5)

    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], D[0]], [C[1], D[1]], 'k-', lw=1.5)
    ax.plot([D[0], A[0]], [D[1], A[1]], 'k-', lw=1.5)

    ax.text(A[0]-0.1, A[1]+0.1, 'A', fontsize=14)
    ax.text(B[0]-0.2, B[1], 'B', fontsize=14)
    ax.text(C[0], C[1]-0.2, 'C', fontsize=14)
    ax.text(D[0]+0.1, D[1], 'D', fontsize=14)

    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig('/tmp/math_repo/handouts/images/ptolemy_fig2.png', dpi=300, bbox_inches='tight')
    plt.close()

draw_fig1()
draw_fig2()

