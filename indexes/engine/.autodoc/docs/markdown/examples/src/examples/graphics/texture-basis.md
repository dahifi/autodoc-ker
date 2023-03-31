[View code on GitHub](https://github.com/playcanvas/engine/examples/src/examples/graphics/texture-basis.tsx)

The `TextureBasisExample` class is a code example that demonstrates how to use the PlayCanvas engine to load and display textures in the Basis format. The Basis format is a compressed texture format that provides high-quality textures with smaller file sizes. 

The `example` method of the `TextureBasisExample` class takes two parameters: a canvas element and a device type. It initializes the Basis library by calling the `basisInitialize` method with the URLs of the Basis WebAssembly and JavaScript files. It then creates a new PlayCanvas application with the canvas element and loads four assets: a color texture, a gloss texture, a normal map texture, and a cubemap texture. 

Once the assets are loaded, the application starts and sets the canvas to fill the window and automatically change resolution to be the same as the canvas size. It also sets the skybox to a cubemap texture and creates a directional light. 

The code then constructs a material with the loaded textures and creates a torus shape with the material. It also creates an entity with a camera component and adds all the entities to the application hierarchy. Finally, it sets an update function on the application's update event to rotate the torus shape.

This code example demonstrates how to use the PlayCanvas engine to load and display textures in the Basis format. It shows how to load multiple textures and use them to construct a material for a 3D object. It also demonstrates how to create entities and add them to the application hierarchy. This code can be used as a starting point for building 3D applications that use Basis textures.
## Questions: 
 1. What is the purpose of the `TextureBasisExample` class?
- The `TextureBasisExample` class is an example of how to use the PlayCanvas engine to create a 3D scene with a torus shape and various textures.

2. What is the `basisInitialize` function doing?
- The `basisInitialize` function is initializing the basis library by providing URLs to the necessary files.

3. What textures are being used in this example and how are they being applied?
- The example is using a color texture, a gloss texture, and a normal map texture, which are being applied to a torus shape using a `StandardMaterial`. The textures have been converted using the `basisu` tool with specific arguments.