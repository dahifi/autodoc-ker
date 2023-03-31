[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/clustered-lighting.tsx)

The `ClusteredLightingExample` class is a code example that demonstrates how to use clustered lighting in the PlayCanvas engine. Clustered lighting is a technique used to improve the performance of rendering many lights in a scene. 

The `example` method of the `ClusteredLightingExample` class takes an HTML canvas element and a device type as input parameters. It creates a graphics device using the `pc.createGraphicsDevice` method and initializes a new PlayCanvas application using the `pc.AppBase` constructor. 

The method then sets the canvas to fill the window and automatically change resolution to be the same as the canvas size. It also creates a ground plane and a high polycount cylinder using the `pc.Entity` constructor and adds them to the scene. 

The method then creates many omni and spot lights using the `pc.Entity` constructor and adds them to the scene. It also creates a single directional light which casts shadows. The lights are moved and rotated using the `on` method of the app's `update` event. 

Finally, the method sets an update function on the app's update event that moves the lights around the cylinder and rotates the directional light. 

This code example can be used as a starting point for developers who want to implement clustered lighting in their PlayCanvas projects. Developers can modify the code to create their own scenes and add their own lights. They can also experiment with different values for the `lighting.cells` and `lighting.maxLightsPerCell` parameters to optimize the performance of their scenes. 

Example usage:

```
import ClusteredLightingExample from 'path/to/ClusteredLightingExample';

const canvas = document.getElementById('canvas');
const deviceType = 'webgl2';

const example = new ClusteredLightingExample();
example.example(canvas, deviceType);
```
## Questions: 
 1. What is the purpose of the `ClusteredLightingExample` class?
- The `ClusteredLightingExample` class is an example of how to use clustered lighting in the PlayCanvas engine, and it includes code for creating and manipulating various types of lights.

2. What is the significance of the `WEBGPU_ENABLED` property?
- The `WEBGPU_ENABLED` property indicates whether the example is compatible with the WebGPU API, which is a new graphics API that is designed to provide better performance and more efficient use of hardware resources.

3. What is the purpose of the `gfxOptions` object?
- The `gfxOptions` object is used to specify various options for creating a graphics device, including the type of device to create (e.g. WebGL or WebGPU), and the URLs of various libraries that are required for graphics rendering.