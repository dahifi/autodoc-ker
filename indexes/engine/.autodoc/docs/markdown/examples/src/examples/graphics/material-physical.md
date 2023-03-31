[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/material-physical.tsx)

The `MaterialPhysicalExample` class is a code example that demonstrates how to use the PlayCanvas engine to create a 3D scene with physically-based materials. The purpose of this code is to show how to create and manipulate entities, materials, and text elements in a PlayCanvas application.

The `example` method is the main entry point of the code example. It takes two parameters: a canvas element and a device type string. The canvas element is used to create a graphics device, which is then used to create a PlayCanvas application. The device type string specifies the type of graphics device to create, such as "webgl2" or "webgpu".

The `assets` object contains two assets: a texture asset for the environment map and a font asset for the text elements. These assets are loaded asynchronously using the `AssetListLoader` class, which is a utility class provided by the PlayCanvas engine.

Once the assets are loaded, the PlayCanvas application is initialized and the canvas is set to fill the window. The environment map is set to the loaded texture, and the tone mapping and skybox mip level are set to default values.

The code then creates a camera entity and adds it to the root of the scene. It also creates a grid of spheres with varying levels of glossiness and metalness, and adds them to the scene. The spheres are created using the `StandardMaterial` class, which is a physically-based material that simulates the behavior of real-world materials.

Finally, the code creates two text elements using the font asset, and adds them to the scene. These text elements display the labels "Glossiness" and "Metalness" next to the grid of spheres.

The code also includes a mouse event listener that allows the user to rotate the skybox by dragging the mouse. This is done by updating the skybox rotation quaternion based on the mouse movement.

Overall, this code example demonstrates how to create a simple 3D scene with physically-based materials and text elements using the PlayCanvas engine. It can be used as a starting point for more complex applications that require 3D graphics and interactivity.
## Questions: 
 1. What is the purpose of this code?
- This code is an example of a material physical implementation in the PlayCanvas engine.

2. What dependencies does this code have?
- This code imports the PlayCanvas engine from a relative path and uses HTMLCanvasElement and pc.GraphicsDevice.

3. What does this code do?
- This code creates a PlayCanvas app with a scene containing spheres with varying metalness and glossiness, and text labels. It also allows the user to rotate the skybox using mouse input.