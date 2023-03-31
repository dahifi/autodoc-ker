[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/layers.tsx)

The `LayersExample` class is a code example that demonstrates how to use layers in the PlayCanvas engine. Layers are used to control the rendering order of entities in a scene. This code example creates a new layer and inserts it after the "World" layer. It then creates two entities, a red box, and a blue box. The red box is rendered first in the "World" layer, and the blue box is rendered in the new layer. The blue box is visible even though it should be inside the red box because it does not test for depth and is in a later layer.

The `example` method is the entry point for the code example. It takes an HTML canvas element and a device type as parameters. It creates a new graphics device using the `pc.createGraphicsDevice` method and initializes a new PlayCanvas application using the `pc.AppBase` class. It sets the canvas to fill the window and automatically change resolution to be the same as the canvas size. It then creates a new layer and inserts it after the "World" layer. It creates two entities, a camera, and a light, and adds them to the scene. Finally, it creates two materials, a red material, and a blue material, and uses them to render the red and blue boxes.

The `LayersExample` class is a useful code example for developers who want to learn how to use layers in the PlayCanvas engine. It demonstrates how to create a new layer, insert it into the scene, and use it to control the rendering order of entities. Developers can use this code example as a starting point for their own projects that require complex rendering order control.
## Questions: 
 1. What is the purpose of the LayersExample class?
- The LayersExample class is an example of how to use layers in the PlayCanvas engine to render entities in different layers.

2. What is the significance of the WEBGPU_ENABLED property?
- The WEBGPU_ENABLED property indicates whether the example is compatible with the WebGPU API, which is a new graphics API for the web.

3. What is the purpose of the gfxOptions object?
- The gfxOptions object is used to specify options for creating a graphics device, including the device type and the URLs for the glslang and twgsl libraries.