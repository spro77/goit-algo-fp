import matplotlib.pyplot as plt
import math

def draw_tree(ax, x, y, angle, length, depth):
    if depth == 0:
        return
    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)
    ax.plot([x, x2], [y, y2], color='brown', lw=1)

    draw_tree(ax, x2, y2, angle + math.pi/6, length * 0.7, depth - 1)

    draw_tree(ax, x2, y2, angle - math.pi/6, length * 0.7, depth - 1)

def main():
    level = int(input("Enter recursion level (e.g., 8): "))
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')
    draw_tree(ax, 0, 0, math.pi/2, 100, level)
    plt.show()

if __name__ == "__main__":
    main()
