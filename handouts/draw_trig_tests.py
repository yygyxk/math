import matplotlib.pyplot as plt
import os
import math

os.makedirs('/Users/yangyake/IdeaProjects/math/handouts/images', exist_ok=True)

def draw_tri_simple(filename, A, B, C, labels, extra_lines=None, extra_labels=None):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], 'k-', lw=1.5)

    if extra_lines:
        for line in extra_lines:
            ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'k--', lw=1)

    ax.text(A[0]-0.2, A[1]-0.2, labels[0], fontsize=12, ha='center')
    ax.text(B[0]+0.2, B[1]-0.2, labels[1], fontsize=12, ha='center')
    ax.text(C[0], C[1]+0.2, labels[2], fontsize=12, ha='center')

    if extra_labels:
        for pos, text in extra_labels:
            ax.text(pos[0], pos[1]-0.2, text, fontsize=12, ha='center')

    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(f'/Users/yangyake/IdeaProjects/math/handouts/images/{filename}', dpi=300)
    plt.close()

# test1
draw_tri_simple('trig_test1.png', (2,0), (0,0), (1.5, 2.598), ['A', 'B', 'C'])

# test2
draw_tri_simple('trig_test2.png', (0,0), (4,0), (2, 3.464), ['A', 'B', 'C'])

# test3 (angle bisector CD)
C = (0, 3)
A = (-2, 0)
B = (4, 0)
D = (0, 0) # Roughly bisector
draw_tri_simple('trig_test3.png', A, B, C, ['A', 'B', 'C'], extra_lines=[(C, D)], extra_labels=[(D, 'D')])

