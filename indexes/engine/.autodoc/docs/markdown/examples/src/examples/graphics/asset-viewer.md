[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/asset-viewer.tsx)

The code is a React component that demonstrates the use of the PlayCanvas engine to create a 3D asset viewer. The component imports the necessary modules from the PlayCanvas engine and other libraries, including React, and defines a class called AssetViewerExample. 

The AssetViewerExample class has two static properties: CATEGORY and NAME. These properties are used to categorize and name the example in the larger project. The class also has two methods: controls and example. 

The controls method returns a React component that renders two buttons labeled "Previous" and "Next". When clicked, these buttons emit events that are handled by the example method. 

The example method creates a graphics device using the createGraphicsDevice method from the PlayCanvas engine. It then creates an AppBase instance and initializes it with the graphics device and other options. The method loads a list of assets, including textures, models, and fonts, and instantiates them as entities in the scene. 

The method also creates a plane entity with a checkerboard material and adds it to the scene. It creates a camera entity with an orbit camera script and adds it to the scene. It creates a directional light entity and adds it to the scene. It sets the environment map, tone mapping, skybox rotation, and skybox intensity of the scene. 

The method also adds event listeners to the canvas element that handle touch events and change the focus entity of the camera when the "Previous" or "Next" button is clicked. 

Overall, the code demonstrates how to use the PlayCanvas engine to create a 3D asset viewer with a camera that can be controlled by the user. It also shows how to load and instantiate assets, create entities, and add them to the scene.
## Questions: 
 1. What is the purpose of the `controls` method in the `AssetViewerExample` class?
- The `controls` method returns a React component that contains two buttons for navigating between assets.

2. What is the purpose of the `gfxOptions` object?
- The `gfxOptions` object contains options for creating a graphics device, including the device types and URLs for glslang and twgsl.

3. What is the purpose of the `jumpToAsset` function?
- The `jumpToAsset` function changes the camera position and focus entity to the next or previous asset in the `assetList` array, depending on the offset parameter.