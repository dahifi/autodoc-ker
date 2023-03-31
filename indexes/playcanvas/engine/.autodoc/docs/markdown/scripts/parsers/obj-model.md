[View code on GitHub](https://github.com/playcanvas/engine/scripts/parsers/obj-model.js)

# PlayCanvas Engine - Obj Model Parser

The `ObjModelParser` is a JavaScript class that provides a parser for OBJ files. OBJ files are a common file format used for storing 3D models. This parser is not included in the PlayCanvas engine library by default, but can be added to the engine by following the instructions provided in the code comments.

The `ObjModelParser` class provides a `parse` method that takes an OBJ file as input and returns a `pc.Model` object. The `pc.Model` object represents a 3D model that can be rendered in a PlayCanvas application. The `parse` method also takes a callback function that is called when the parsing is complete.

The `ObjModelParser` class also provides a `_parseIndices` method that is used internally by the `parse` method to parse the face indices in the OBJ file.

The `ObjModelParser` class is used in the PlayCanvas engine to load OBJ files as model assets. To use the `ObjModelParser`, you first need to register it with the model resource handler. This is done using the following code:

```javascript
var objParser = new pc.ObjModelParser(this.app.graphicsDevice);
this.app.loader.getHandler("model").addParser(objParser, function (url) {
    return (pc.path.getExtension(url) === '.obj');
});
```

This code creates a new `pc.ObjModelParser` object and registers it with the model resource handler. The `addParser` method takes two arguments: the parser object and a function that returns `true` if the parser should be used to parse the file with the given URL.

Once the parser is registered, you can load an OBJ file as a model asset using the following code:

```javascript
var asset = new pc.Asset("MyObj", "model", {
   url: "model.obj"
});
this.app.assets.add(asset);
this.app.assets.load(asset);
```

This code creates a new `pc.Asset` object with the name "MyObj" and the type "model". The `url` property specifies the URL of the OBJ file to load. The asset is then added to the PlayCanvas application's asset registry and loaded using the `load` method.

When the asset is loaded, the `pc.ObjModelParser` is used to parse the OBJ file and create a `pc.Model` object. The `pc.Model` object can then be used to render the 3D model in the PlayCanvas application.

Overall, the `ObjModelParser` class provides a convenient way to load OBJ files as model assets in a PlayCanvas application.
## Questions: 
 1. What is the purpose of this code?
- This code is a sample Obj model parser that is not built into the PlayCanvas engine library by default. It allows developers to register the parser and load obj as a model asset.

2. What are some known issues with this code?
- The code cannot handle meshes larger than 65535 verts, assigns default material to all meshes, and doesn't create indexed geometry.

3. How does the code parse the input?
- The code parses the input by splitting it into lines and then processing each line based on its first character. If the first character is 'v', the code adds the vertex, normal, or uv to the corresponding array. If the first character is 'g', 'o', or 'u', the code splits the input into groups. If the first character is 'f', the code parses the face indices and expands the corresponding vertices, uvs, and normals. Finally, the code creates a new mesh instance for each group and adds it to the model.