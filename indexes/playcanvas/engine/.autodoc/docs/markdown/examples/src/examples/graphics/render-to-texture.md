[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/render-to-texture.tsx)

The `RenderToTextureExample` class is a code example that demonstrates how to render a scene to a texture using the PlayCanvas engine. The purpose of this code is to show how to create a texture and a render target, and how to use two cameras to render objects into the texture and the main camera. 

The code creates a graphics device, initializes an app, and sets the canvas to fill the window. It then loads assets, including a texture and a script, and creates a layer for objects that do not render into the texture. The code also creates a main camera that renders entities in the world, excluded, and skybox layers, and an orbit camera script with mouse and touch support. 

The code creates a texture camera that renders entities in the world and skybox layers into the texture, and an entity with an omni light component that is added to the world layer. The code also creates a plane called `tv` that is used to display the rendered texture, and a skydome that uses the top mipmap level of a cubemap. 

The code updates things each frame, including rotating the texture camera around the objects and switching the texture camera between perspective and orthographic projection every 5 seconds. 

This code can be used as a reference for developers who want to create a similar feature in their PlayCanvas project. For example, a developer could use this code to create a mini-map that shows a top-down view of the game world, or to create a security camera system that displays a live feed from a camera in the game world. 

Example usage:

```javascript
const canvas = document.getElementById('application-canvas');
const deviceType = 'webgl2';
const renderToTextureExample = new RenderToTextureExample();
renderToTextureExample.example(canvas, deviceType);
```
## Questions: 
 1. What is the purpose of the `RenderToTextureExample` class?
- The `RenderToTextureExample` class is an example of how to render objects into a texture using the PlayCanvas engine.

2. What are the two cameras used in this example and what are their purposes?
- The two cameras used in this example are `textureCamera` and `camera`. `textureCamera` renders entities in the `worldLayer` and `skyboxLayer` into the texture, while `camera` renders entities in the `worldLayer`, `excludedLayer`, and `skyboxLayer`.

3. What is the purpose of the `createPrimitive` function?
- The `createPrimitive` function is a helper function that creates a primitive with a specified shape type, position, scale, color, and layer. It creates a material of the specified color, creates a primitive with the specified type and layer, sets the position and scale, and adds it to the scene.