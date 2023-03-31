[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/material-basic.tsx)

The `MaterialBasicExample` class is a code example that demonstrates how to use the PlayCanvas engine to create a basic material with alpha blending and alpha testing. The purpose of this code is to show how to create a simple scene with multiple boxes that have different alpha blending modes and alpha test values. The code also shows how to create a text element-based entity and how to rotate the boxes in the scene.

The `MaterialBasicExample` class imports the PlayCanvas engine and defines three static properties: `CATEGORY`, `NAME`, and `WEBGPU_ENABLED`. These properties are used to categorize and name the example and to indicate whether the example is compatible with the WebGPU API.

The `example` method of the `MaterialBasicExample` class takes two parameters: a canvas element and a device type string. The method creates two assets: a font asset and a texture asset. It then creates a graphics device using the `createGraphicsDevice` method of the PlayCanvas engine and initializes an app using the `AppBase` class. The app is set to fill the window and automatically change resolution to be the same as the canvas size.

The method then creates an entity with a camera component and adds it to the app's root entity. It also creates multiple boxes with different alpha blending modes and alpha test values and adds them to the app's root entity. Finally, it creates two text element-based entities and adds them to the app's root entity.

The `example` method sets an update function on the app's update event that rotates the boxes in the scene. The `MaterialBasicExample` class is exported as the default export of the module.

Example usage:

```javascript
import MaterialBasicExample from 'path/to/MaterialBasicExample.js';

const canvas = document.getElementById('canvas');
const deviceType = 'webgl2';

const example = new MaterialBasicExample();
example.example(canvas, deviceType);
```

This code creates a new instance of the `MaterialBasicExample` class and calls its `example` method with a canvas element and a device type string. The example is then displayed on the canvas.
## Questions: 
 1. What is the purpose of the `MaterialBasicExample` class?
- The `MaterialBasicExample` class is an example of how to use basic materials in the PlayCanvas engine to create a scene with boxes that have different alpha blend modes and alpha test values.

2. What assets are being loaded in the `example` method?
- The `example` method loads two assets: a font and a texture.

3. What is the purpose of the `createText` function?
- The `createText` function creates a text element-based entity with a specified font, message, position, and rotation, and adds it to the scene. In this example, it is used to create two text elements that label the rows and columns of boxes.