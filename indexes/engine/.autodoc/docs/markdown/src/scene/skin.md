[View code on GitHub](https://github.com/playcanvas/engine/src/scene/skin.js)

The code defines a class called `Skin` which represents the data about the bones in a hierarchy that drive a skinned mesh animation. In particular, the `Skin` class stores the bone name and inverse bind matrix for each bone. The inverse bind matrices are important in the mathematics of vertex skinning.

The `Skin` class has a constructor that takes three parameters: `graphicsDevice`, `ibp`, and `boneNames`. The `graphicsDevice` parameter is an instance of the `GraphicsDevice` class which is used to manage the skin. The `ibp` parameter is an array of inverse bind matrices, and the `boneNames` parameter is an array of bone names for the bones referenced by this skin.

The `Skin` class is designed to be used in the larger project as a way to store and manage the data about the bones in a hierarchy that drive a skinned mesh animation. This data can then be used to perform vertex skinning calculations to animate the mesh.

Here is an example of how the `Skin` class might be used in the larger project:

```javascript
import { Skin } from 'playcanvas-engine';

// create an instance of the GraphicsDevice class
const graphicsDevice = new GraphicsDevice();

// create an array of inverse bind matrices
const ibp = [
  new Mat4(),
  new Mat4(),
  new Mat4()
];

// create an array of bone names
const boneNames = ['bone1', 'bone2', 'bone3'];

// create a new instance of the Skin class
const skin = new Skin(graphicsDevice, ibp, boneNames);
```

In this example, we create an instance of the `GraphicsDevice` class, an array of inverse bind matrices, and an array of bone names. We then create a new instance of the `Skin` class, passing in the `graphicsDevice`, `ibp`, and `boneNames` parameters. This creates a new `Skin` object that can be used to manage the data about the bones in a hierarchy that drive a skinned mesh animation.
## Questions: 
 1. What is the purpose of the Skin class?
- The Skin class contains data about the bones in a hierarchy that drive a skinned mesh animation, specifically the bone name and inverse bind matrix for each bone.

2. What parameters are required to create a new instance of the Skin class?
- To create a new instance of the Skin class, a graphics device, an array of inverse bind matrices, and an array of bone names for the bones referenced by the skin are required.

3. What is the significance of the inverse bind matrices in vertex skinning?
- Inverse bind matrices are instrumental in the mathematics of vertex skinning, as they are used to transform vertices from model space to bone space during animation.