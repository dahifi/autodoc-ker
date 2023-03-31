[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/model-textured-box.tsx)

The `ModelTexturedBoxExample` class is a code example that demonstrates how to create a 3D scene with a textured box, a light source, and a camera using the PlayCanvas engine. The purpose of this code is to show how to use the PlayCanvas engine to create a simple 3D scene with basic components.

The `example` method is the main entry point of the code example. It takes two parameters: a canvas element and a device type. The canvas element is used to render the 3D scene, while the device type specifies the type of graphics device to use (e.g., WebGL, WebGPU).

The code first creates an asset object that contains a texture asset for the clouds. It then creates a graphics device using the `pc.createGraphicsDevice` method, passing in the canvas element and graphics options. The graphics options specify the device type and the URLs for the glslang and twgsl libraries.

Next, the code creates an `AppOptions` object that specifies the graphics device and the component systems and resource handlers to use. It then creates a new `pc.AppBase` object and initializes it with the `AppOptions`.

The code sets the canvas fill mode to `pc.FILLMODE_FILL_WINDOW` and the canvas resolution to `pc.RESOLUTION_AUTO`. It then loads the assets using an `AssetListLoader` object and starts the app.

The code sets the ambient light of the scene to a dark gray color. It then creates a `StandardMaterial` object with the clouds texture and creates a box entity with a render component that uses the material. It also creates a light entity with an omni light component and a sphere model component. The light entity is scaled down to 0.1m. Finally, the code creates a camera entity with a camera component.

The code adds the box, light, and camera entities to the app's root entity. It then sets an update function on the app's update event that rotates the box and moves the light in a circle.

This code example demonstrates how to create a simple 3D scene with a textured box, a light source, and a camera using the PlayCanvas engine. It can be used as a starting point for more complex 3D scenes that require additional components and functionality.
## Questions: 
 1. What is the purpose of the `ModelTexturedBoxExample` class?
- The `ModelTexturedBoxExample` class is an example of how to create a 3D scene with a textured box, an omni light, and a camera using the PlayCanvas engine.

2. What is the significance of the `WEBGPU_ENABLED` property?
- The `WEBGPU_ENABLED` property indicates whether the example is compatible with the WebGPU API, which is a new graphics API for the web that provides lower-level access to the GPU.

3. What is the purpose of the `gfxOptions` object?
- The `gfxOptions` object is used to specify options for creating a graphics device, including the type of device to create and the URLs for the glslang and twgsl libraries.