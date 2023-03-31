[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/shader-burn.tsx)

The `ShaderBurnExample` class is a part of the PlayCanvas engine project and is responsible for rendering a 3D model of a statue with a custom shader. The purpose of this code is to demonstrate how to create a custom shader and apply it to a 3D model in PlayCanvas. 

The `ShaderBurnExample` class has a static `FILES` object that contains two properties, `shader.vert` and `shader.frag`. These properties contain the vertex and fragment shader code, respectively. The vertex shader is responsible for transforming the vertices of the 3D model, while the fragment shader is responsible for coloring the pixels of the model. 

The `example` method of the `ShaderBurnExample` class takes three arguments: a canvas element, a device type, and a files object. The `example` method creates a new `pc.GraphicsDevice` object using the `pc.createGraphicsDevice` method and sets up an instance of the PlayCanvas application using the `pc.AppBase` constructor. 

The `example` method then loads the 3D model and texture assets using the `pc.AssetListLoader` and adds them to the PlayCanvas application. It creates an entity with a camera component and an entity with a light component and adds them to the scene hierarchy. 

The `example` method then creates a custom shader using the `pc.createShaderFromCode` method and sets it as the material for the 3D model. The `uHeightMap` parameter of the shader is set to the `clouds` texture asset. 

Finally, the `example` method updates the `uTime` parameter of the shader in the `on("update")` event listener, which causes the shader to "burn" away parts of the model based on the height map texture. 

Overall, the `ShaderBurnExample` class demonstrates how to create a custom shader and apply it to a 3D model in PlayCanvas. It can be used as a reference for developers who want to create their own custom shaders in PlayCanvas.
## Questions: 
 1. What does this code do?
- This code defines a class called `ShaderBurnExample` which contains a static `example` method that creates a 3D scene with a statue model and a shader that changes the color of the model based on a height map texture.

2. What external dependencies does this code have?
- This code imports the `pc` module from a relative path that is three levels up from the current directory. It also relies on external assets such as a 3D model and a texture.

3. What is the purpose of the `WEBGPU_ENABLED` static property?
- The `WEBGPU_ENABLED` property is a boolean that is set to `true`. It is likely used to indicate whether the code is compatible with the WebGPU API, which is a new graphics API for the web that is currently in development.