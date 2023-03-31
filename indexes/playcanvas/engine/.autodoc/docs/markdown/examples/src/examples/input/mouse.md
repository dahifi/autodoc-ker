[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/input/mouse.tsx)

The code defines a class called `MouseExample` that provides an example of how to use the PlayCanvas engine to create a 3D scene that responds to mouse input. The purpose of the code is to demonstrate how to create a PlayCanvas application that uses the mouse to rotate a 3D object in the scene.

The `MouseExample` class has a single method called `example` that takes two arguments: a canvas element and a device type. The canvas element is used to create a graphics device, which is then used to create a PlayCanvas application. The device type is used to specify the type of graphics device to create, such as WebGL or WebGPU.

The `example` method creates two assets: a texture and a 3D model. It then creates a graphics device using the `pc.createGraphicsDevice` method, passing in the canvas element and device type. Once the graphics device is created, it creates a PlayCanvas application using the `pc.AppBase` class and initializes it with the graphics device.

The method then sets the canvas fill mode and resolution, loads the assets using an `AssetListLoader`, and starts the application. It sets the skybox, creates a camera entity, adds the 3D model to the scene, and creates a `pc.Mouse` object that listens for mouse events.

When the mouse moves, the `mousemove` event is fired, and the code checks if the left mouse button is pressed. If it is, it updates the rotation of the 3D model based on the mouse movement.

Overall, this code demonstrates how to use the PlayCanvas engine to create a 3D scene that responds to mouse input. It shows how to create a graphics device, load assets, create entities, and handle mouse events. This code can be used as a starting point for creating more complex PlayCanvas applications that use mouse input.
## Questions: 
 1. What is the purpose of the `MouseExample` class?
- The `MouseExample` class is an example of how to use mouse input in the PlayCanvas engine.

2. What assets are being loaded in the `example` method?
- The `example` method loads a texture asset and a container asset.

3. What does the `mousemove` event listener do?
- The `mousemove` event listener updates the rotation of an entity based on the movement of the mouse, but only if the left mouse button is pressed.