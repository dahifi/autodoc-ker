[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/model-outline.tsx)

The `ModelOutlineExample` class is an example of how to use the PlayCanvas engine to create a model outline effect. The purpose of this code is to demonstrate how to create a post-processing effect that outlines 3D models in a scene. The example creates a scene with a ground plane and three primitives (a sphere, a box, and a cone) that are visible in both the world layer and the outline layer. The example also creates two cameras, one for rendering the world layer and one for rendering the outline layer. The outline camera renders the outline layer into a render target, which is then used as a texture for the outline effect.

The `example` method takes two arguments, a canvas element and a device type. It creates a graphics device using the `createGraphicsDevice` method and initializes a new PlayCanvas application using the `AppBase` class. It then sets the canvas to fill the window and automatically change resolution to be the same as the canvas size. The example loads an asset for the outline effect and creates a list of component systems and resource handlers to be used by the application. It then creates a list of assets to be loaded and loads them using an `AssetListLoader`. Once the assets are loaded, the example starts the application and sets the ambient light of the scene.

The example defines a helper function `createPrimitive` that creates a primitive with a specified shape type, position, scale, color, and layer. It also defines a function `createRenderTarget` that creates a texture and render target for rendering into, including a depth buffer. The example creates a layer for rendering to texture and adds it to the beginning of layers to render into it first. It then creates the ground plane and three primitives, visible in both layers.

The example creates two cameras, one for rendering entities in the world layer and one for rendering entities in the outline layer into the render target. It creates an `OutlineEffect` object and adds it to the post-effects of the main camera. The example also creates an entity with an omni light component and adds it to both layers.

The example handles canvas resize and updates things each frame. It rotates the camera around the objects and updates the position and rotation of the outline camera to match the main camera.

Overall, this code demonstrates how to create a model outline effect using the PlayCanvas engine. It shows how to create a scene with multiple layers, cameras, and post-processing effects. This example can be used as a starting point for creating more complex scenes with custom post-processing effects.
## Questions: 
 1. What does this code do?
- This code is an example of how to create a model outline effect using the PlayCanvas engine. It creates a scene with several primitives and two cameras, one for the main view and one for the outline effect, and applies a post-processing effect to the main camera to create the outline effect.

2. What dependencies does this code have?
- This code depends on the PlayCanvas engine, which is imported at the beginning of the file using the wildcard import syntax. It also depends on several external scripts and libraries, including a glslang compiler and a twgsl library, which are specified in the gfxOptions object.

3. What is the purpose of the createPrimitive and createRenderTarget functions?
- The createPrimitive function is a helper function that creates a primitive shape (such as a sphere or box) with a specified position, scale, color, and layer, and adds it to the scene. The createRenderTarget function creates a texture and render target for rendering into, including a depth buffer, which is used by the outline camera to render the outline effect.