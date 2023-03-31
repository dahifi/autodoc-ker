[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/misc/mini-stats.tsx)

The MiniStatsExample class is a demonstration of how to use the MiniStats system in the PlayCanvas engine. The MiniStats system is a tool that provides real-time performance statistics for a PlayCanvas application. The MiniStatsExample class creates a PlayCanvas application, sets up the MiniStats system, and adds some entities to the scene to demonstrate how the MiniStats system works.

The example method of the MiniStatsExample class takes three parameters: a canvas element, a device type string, and a pcx object. The canvas element is used to create the PlayCanvas application. The device type string is not used in this example. The pcx object is used to access the MiniStats system.

The example method creates a PlayCanvas application and sets the canvas to fill the window. It also sets up the options for the MiniStats system. The options include the sizes of the MiniStats display, the statistics to display, and the starting size of the MiniStats display. The example method then creates the MiniStats system using the options.

The example method adds some entities to the scene to demonstrate how the MiniStats system works. The entities are created and destroyed every frame to simulate the allocation and deallocation of resources. The MiniStats system displays statistics such as frame update time, total number of draw calls, number of triangles, number of materials used, frame time for frustum culling, VRAM usage, frames per second, and delta time. The statistics are updated in real-time as the entities are created and destroyed.

The MiniStatsExample class is a useful tool for developers who want to optimize the performance of their PlayCanvas applications. By using the MiniStats system, developers can identify performance bottlenecks and optimize their code accordingly. The MiniStatsExample class can be used as a starting point for developers who want to integrate the MiniStats system into their own PlayCanvas applications.
## Questions: 
 1. What is the purpose of this code?
- This code is an example of how to use the MiniStats system in the PlayCanvas engine to display performance statistics in a web application.

2. What are the requirements for the MiniStats system to report values for certain counters?
- For most of the counters to report values, either a debug or profiling engine build needs to be used.

3. What does the `createPrimitive` function do?
- The `createPrimitive` function creates a primitive shape with a random color material, given a shape type, position, and scale.