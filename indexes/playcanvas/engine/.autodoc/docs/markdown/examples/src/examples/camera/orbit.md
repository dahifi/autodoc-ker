[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/camera/orbit.tsx)

The `OrbitExample` class is a part of the PlayCanvas engine project and is responsible for creating an example of an orbit camera. The purpose of this code is to demonstrate how to create an orbit camera in PlayCanvas. An orbit camera is a type of camera that allows the user to orbit around a target object. This is useful for games and applications where the user needs to view an object from different angles.

The `example` method is the main method of the `OrbitExample` class. It takes two parameters, a canvas element and a device type. It creates a new PlayCanvas application and starts the update loop. It then loads two assets, a 3D model of a statue and a script for the orbit camera. Once the assets are loaded, it creates an entity hierarchy representing the statue and adds it to the root of the application. It also creates a camera entity with an orbit camera script and adds it to the root of the application. Finally, it creates a directional light and adds it to the root of the application.

The `OrbitExample` class can be used as a starting point for creating an orbit camera in a PlayCanvas project. Developers can use this code as a reference to understand how to create an orbit camera and customize it to fit their specific needs. For example, they can change the target object, adjust the camera settings, or add additional input methods for the camera. Here is an example of how to use the `OrbitExample` class:

```javascript
import OrbitExample from 'path/to/OrbitExample';

const canvas = document.getElementById('canvas');
const deviceType = 'desktop';

const orbitExample = new OrbitExample();
orbitExample.example(canvas, deviceType);
```

This code creates a new instance of the `OrbitExample` class and calls the `example` method with a canvas element and a device type. This will create an orbit camera in the PlayCanvas application and display the statue object. Developers can then modify the code to fit their specific needs.
## Questions: 
 1. What is the purpose of the `OrbitExample` class?
- The `OrbitExample` class is an example of how to create a camera with an orbit camera script and a directional light in the PlayCanvas engine.

2. What are the parameters of the `example` method?
- The `example` method takes in an HTML canvas element and a device type as parameters.

3. What is the purpose of the `assetListLoader` variable?
- The `assetListLoader` variable is used to load the assets needed for the example, which are a 3D model of a statue and a script for the orbit camera.