[View code on GitHub](https://github.com/playcanvas/engine/scripts/utils/download-texture.js)

The code in this file provides functionality for downloading a texture as a PNG file. It includes two functions for constructing a PNG file: `constructPngUrl` and `constructPngUrlOld`. The former function constructs an uncompressed PNG file manually, while the latter uses the canvas API to construct the PNG file. The `constructPngUrl` function is preferred over `constructPngUrlOld` because the canvas API suffers from bit loss due to its handling of premultiplied alpha. 

The `download` function downloads the data URI of the PNG file as a file with a specified filename. The `readPixels` function reads the pixel data of a given texture face and returns it as a `Uint8ClampedArray`. The `flipY` function flips the image data in the Y direction. Finally, the `downloadTexture` function downloads the texture as a PNG file. It takes in the texture, filename, face, and a boolean `flipY_` parameter. If the texture is a cubemap, it concatenates the six faces of the cubemap into a single image. 

This code is useful for exporting textures from the PlayCanvas engine. It allows users to download textures as PNG files, which can be used in other applications or for offline use. The `downloadTexture` function can be called from other parts of the PlayCanvas engine to provide a download button for textures. 

Example usage of the `downloadTexture` function:
```
var texture = app.assets.find("texture_asset").resource;
downloadTexture(texture, "texture.png", 0, true);
```
This code downloads the first face of the texture as a PNG file with the filename "texture.png". The `true` parameter flips the image data in the Y direction.
## Questions: 
 1. What is the purpose of the `constructPngUrl` function?
- The `constructPngUrl` function constructs an uncompressed PNG file manually because the canvas API suffers from bit loss due to its handling of premultiplied alpha.

2. What is the difference between `constructPngUrl` and `constructPngUrlOld` functions?
- `constructPngUrl` constructs an uncompressed PNG file manually, while `constructPngUrlOld` constructs a PNG using canvas API. The latter is faster but suffers from canvas premultiplied alpha bit loss.

3. What is the purpose of the `downloadTexture` function?
- The `downloadTexture` function downloads the image as png by calling the `download` function and passing the constructed PNG URL from the `constructPngUrl` function. It also reads the pixel data of the given texture face and flips the image data in Y if specified.