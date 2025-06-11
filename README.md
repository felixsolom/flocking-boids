# flocking-boids
This is a boids algorithm simulator 

## boids
Boids are a kind of birds. More precisely, they are little triangles that simulate the movememt of birds in a flock. The [idea](https://en.wikipedia.org/wiki/Boids) was developed by [Craig Raynolds](https://en.wikipedia.org/wiki/Craig_Reynolds_(computer_graphics)) in 1986. The algorithm has three basic forces that influence each boid's individual behavior in a flock.

### separation:
Basically, the directive to steer away from neighbors to avoid overcrowding.

### Alighnment:
Steer toward the average heading of of other boids that are considered neighbors.

### Cohision:
Steer towards the average position of your neghbors

## Flock
The flock is the sum of all boids conducting themselves in accordance to all the different forces of the algorithm. 

## Acceleration / Deceleration mechanics
Each time an individual boid forced to make a change of its heading and forced to steer, it's also forced to lower its speed. when it's back in the clear, the boid is free to accelerate until it gets to cruise speed. 
This acceleration/Deceleration mechanic is panctuated by a color change. From Blue to Red, when Green in the middle represent regular cruising speed 

## Obstacles
Obstacles are mouse click induced objects that force avoidance behavior on the boids. I must say that in this stage of the project, the competing forces of the algorithm make it so, that the avoidance behavior is not particularly convincing. Something to continue working on.

## Tkinter 
I chose the tkinter to represent visually all of the above. It is, I found a bit poor on the graphic side, but it freed me to deal with an actual logic of what I'm doing. 
Maybe the next step should be more captivating visual representation

