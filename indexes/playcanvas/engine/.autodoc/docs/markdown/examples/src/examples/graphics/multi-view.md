[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/multi-view.tsx)

The `MultiViewExample` class is a code example that demonstrates how to create a PlayCanvas application with multiple cameras and views. The purpose of this code is to show how to create a scene with multiple cameras that can be used to render different parts of the scene. This is useful for creating split-screen games or for displaying different views of a 3D model.

The `example` method is the main entry point for the code example. It takes two parameters: a canvas element and a device type. The canvas element is used to create a graphics device, which is used to render the scene. The device type is used to specify which type of graphics device to create (e.g. WebGL or WebGPU).

The code first sets up and loads the Draco module, which is used to decode compressed GLB files. It then creates a list of assets that are used in the scene, including a chess board model, a cubemap texture, and a camera script. It also creates a list of graphics options that are used to create the graphics device.

The code then creates a new PlayCanvas application and sets the canvas to fill the window. It loads the assets and starts the application. It then creates three cameras: a left camera, a right orthographic camera, and a top camera. The left camera is a perspective camera that is positioned to the left of the scene. The right camera is an orthographic camera that is positioned above the scene. The top camera is a perspective camera that is positioned above and to the left of the scene. The code also adds an orbit camera script to the top camera, which allows the user to orbit around the scene using the mouse or touch input.

The code then creates a directional light that casts shadows and sets the skybox to a cubemap texture. Finally, it sets up an update function that is called once per frame. This function updates the position of the left camera and the orthographic height of the right camera.

Overall, this code example demonstrates how to create a PlayCanvas application with multiple cameras and views. It shows how to load assets, create cameras, add scripts, and update the scene. This code can be used as a starting point for creating split-screen games or for displaying different views of a 3D model.
## Questions: 
 1. What is the purpose of the `MultiViewExample` class?
- The `MultiViewExample` class is an example of how to use the PlayCanvas engine to create a scene with multiple cameras and a chess board model.

2. What is the significance of the `WEBGPU_ENABLED` property?
- The `WEBGPU_ENABLED` property indicates whether the example is compatible with the WebGPU API, which is a new graphics API for the web that provides lower-level access to the GPU.

3. What is the purpose of the `demo` function?
- The `demo` function is a callback function that is called after the Draco decoder module is loaded. It initializes the PlayCanvas app and sets up the scene with cameras, lighting, and models.