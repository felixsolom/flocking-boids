<div align="center">
  <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGhxYnN5ZjRkbHdheTY1dmY0MTczcGVsOWd0eDQ0MXV5cnQxdjhpbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26gst1l8FrcnFPa12/giphy.gif" width="100">
</div>

# 🐦 Flocking Boids

A flocking birds simulation algorithm builder and visualizer. "Boids" follow a set of simple rules, creating complex and lifelike swarm behavior on a screen.


## What is this?

This project is a simulation of "boids," an artificial life program developed by Craig Reynolds in 1986. It's a very cool attempt to explain complex emerging behavior with a few very simple rools, and this is why I like it. It complexity reduced to simplicty 

Each boid follows three basic rules:
*   **Separation:** Steer to avoid crowding local flockmates.
*   **Alignment:** Steer towards the average heading of local flockmates.
*   **Cohesion:** Steer to move toward the average position of local flockmates.

Another touch here, you can also click your mouse to create obstacles and see how the flock reacts!

Also there is a color indicator of speed. Each boid changes it color according to accelerating or deccelerating pattern. 

## How to Run

This project uses Python's built-in `tkinter` library, so no need to install any special packages.

1.  Clone this repository:
    ```bash
    git clone https://github.com/felixsolomon/flocking-boids.git
    cd flocking-boids
    ```
2.  Run the simulation:
    ```bash
    python3 src/main.py
    ```

## A Little Backstory

As a backend developer, my primary portfolio project is well, not very surprisingly a web application written in Go. This little simulation I built for fun, and to explore different programming concepts free of constraints, but also to show a different side of my skills. i trully enjoyed too much building it, and maybe it's also fun for others to watch.