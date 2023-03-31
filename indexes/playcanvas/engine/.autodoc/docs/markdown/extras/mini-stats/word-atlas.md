[View code on GitHub](https://github.com/playcanvas/engine/extras/mini-stats/word-atlas.js)

The `WordAtlas` class is responsible for generating a texture atlas of words that can be used for rendering text in a 2D context. The constructor takes in a texture and an array of words, and generates a canvas with the same dimensions as the texture. It then uses the canvas context to render each word onto the canvas, keeping track of the placement of each word in the atlas. The resulting texture is then used to render text in the 2D context.

The `render` method takes in a `render2d` object, a word to render, and the x and y coordinates of where to render the word. It looks up the placement of the word in the atlas and uses the `render2d` object to render a quad with the appropriate texture coordinates. The method returns the width of the rendered word.

This class is useful for rendering text in a 2D context efficiently, as it avoids the need to render each character separately. By generating a texture atlas of words, it reduces the number of draw calls needed to render text. This can be especially useful in games or other applications where text is frequently rendered.

Example usage:

```javascript
const texture = new Texture(device, {
    width: 512,
    height: 512,
    format: PIXELFORMAT_R8_G8_B8_A8
});

const words = ['hello', 'world', 'foo', 'bar'];
const wordAtlas = new WordAtlas(texture, words);

// render the word 'hello' at position (10, 10)
wordAtlas.render(render2d, 'hello', 10, 10);
```
## Questions: 
 1. What is the purpose of the WordAtlas class?
- The WordAtlas class is used to create a texture atlas of words that can be rendered in a 2D context.

2. What font is used to render the words in the texture atlas?
- The words are rendered using the "Lucida Console", Monaco, monospace font with a font size of 10px.

3. How are the words in the texture atlas colored?
- Single characters and '.' are colored white, while the rest of the characters are colored grey.