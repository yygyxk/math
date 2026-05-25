import matplotlib.pyplot as plt
import os
import math

os.makedirs('/Users/yangyake/IdeaProjects/math/handouts/images', exist_ok=True)

def draw_tri(filename, A, B, C, labels, alt_lines=None, extra_points=None):
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot([A[0], B[0]], [A[1], B[1]], 'k-', lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], 'k-', lw=1.5)
    ax.plot([C[0], A[0]], [C[1], A[1]], 'k-', lw=1.5)

    if alt_lines:
        for line in alt_lines:
            ax.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'k--', lw=1)

    if extra_points:
        for pt, lbl in extra_points:
            ax.text(pt[0], pt[1]-0.4, lbl, fontsize=12, ha='center')

    ax.text(A[0]-0.3, A[1]-0.3, labels[0], fontsize=12, ha='right')
    ax.text(B[0]+0.3, B[1]-0.3, labels[1], fontsize=12, ha='left')
    ax.text(C[0], C[1]+0.3, labels[2], fontsize=12, ha='center')

    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(f'/Users/yangyake/IdeaProjects/math/handouts/images/{filename}', dpi=300)
    plt.close()

# Original
draw_tri('trig_original.png', (0,0), (2,0), (8,6), ['A', 'B', 'C'], alt_lines=[((8,6),(8,0)), ((2,0),(8,0))], extra_points=[((8,0), 'D')])

# V1
draw_tri('trig_var1.png', (0,0), (5,0), (2, 3.464), ['C', 'A', 'B'])

# V2
draw_tri('trig_var2.png', (0,0), (4,0), (1, 2), ['C', 'A', 'B'])

# V3
draw_tri('trig_var3.png', (0,0), (6,0), (2, 3), ['B', 'C', 'A'])

# V4 (with median)
A = (0,0); C = (2,0); B = (3*math.cos(math.pi/3), 3*math.sin(math.pi/3))
D = ((B[0]+C[0])/2, (B[1]+C[1])/2)
draw_tri('trig_var4.png', A, B, C, ['A', 'B', 'C'], alt_lines=[(A, D)], extra_points=[(D, 'D')])

# V5
draw_tri('trig_var5.png', (0,0), (4,0), (1.5, 3), ['B', 'C', 'A'])

# Test 1
draw_tri('trig_test1.png', (0,0), (3,0), (1, 2), ['A', 'B', 'C'])

# Test 2
draw_tri('trig_test2.png', (0,0), (5,0), (2, 4), ['B', 'C', 'A'])

# Test 3 (with angle bisector)
A = (0,0); B = (4,0); C = (2, 3)
# arbitrary D on BC
D = (3, 1.5)
draw_tri('trig_test3.png', A, B, C, ['A', 'B', 'C'], alt_lines=[(A, D)], extra_points=[(D, 'D')])

