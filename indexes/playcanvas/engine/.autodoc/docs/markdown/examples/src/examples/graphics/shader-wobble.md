[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/shader-wobble.tsx)

The `ShaderWobbleExample` class is a part of the PlayCanvas engine project and is responsible for creating a wobbling effect on a 3D model using a custom shader. The class contains a static `example` method that takes in a canvas element, device type, and shader files as parameters. 

The method first creates a `pc.Asset` object for the 3D model and a `gfxOptions` object that specifies the device type and URLs for the glslang and twgsl libraries. It then creates a graphics device using the `pc.createGraphicsDevice` method and initializes a new PlayCanvas application using the `pc.AppBase` constructor. 

The method sets the canvas fill mode and resolution, creates a camera and light entity, and adds them to the scene hierarchy. It then creates a custom shader using the `pc.createShaderFromCode` method and a new material using the `pc.Material` constructor. The method instantiates the 3D model and sets the new material on all meshes in the model, using the original texture from the model on the new material. 

Finally, the method sets up an update event listener that updates the time parameter for the shader and updates the material accordingly. 

This method can be used to create a wobbling effect on any 3D model in a PlayCanvas application. Developers can customize the shader code to achieve different effects and modify the material properties to change the appearance of the model. 

Example usage:

```
const canvas = document.getElementById('application-canvas');
const deviceType = 'webgl2';
const shaderFiles = {
  'shader.vert': /* glsl */`
    // vertex shader code
  `,
  'shader.frag': /* glsl */`
    // fragment shader code
  `
};

ShaderWobbleExample.example(canvas, deviceType, shaderFiles);
```
## Questions: 
 1. What does this code do?
- This code defines a class called `ShaderWobbleExample` that contains a static `example` method which creates a 3D scene with a wobbling shader effect on a 3D model.

2. What external dependencies does this code have?
- This code imports the `pc` module from a relative path that is three levels up from the current directory. It also relies on external assets such as a 3D model file and two JavaScript files for glslang and twgsl.

3. What is the purpose of the `example` method?
- The `example` method creates a 3D scene with a camera, an omni light, and a 3D model with a wobbling shader effect. It also sets up the graphics device, loads assets, creates a shader, and updates the shader's time parameter.