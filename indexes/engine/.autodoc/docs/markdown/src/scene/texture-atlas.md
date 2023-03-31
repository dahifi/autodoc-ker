[View code on GitHub](https://github.com/playcanvas/engine/src/scene/texture-atlas.js)

## TextureAtlas Class

The `TextureAtlas` class is a subclass of `EventHandler` that contains a number of frames from a texture. Each frame defines a region in a texture. The TextureAtlas is referenced by `Sprite`s. 

### Constructor

The constructor creates a new instance of the `TextureAtlas` class. It initializes two private properties `_texture` and `_frames` to `null`.

### Properties

#### texture

The `texture` property is a setter and getter that sets and gets the texture used by the atlas. It is of type `import('../platform/graphics/texture.js').Texture`.

#### frames

The `frames` property is a setter and getter that sets and gets the frames which define portions of the texture atlas. It is of type `object`.

### Methods

#### setFrame(key, data)

The `setFrame` method sets a new frame in the texture atlas. It takes two parameters: `key` and `data`. `key` is the key of the frame and `data` is an object that contains the properties of the frame. The properties of the `data` object are:

- `rect`: The u, v, width, height properties of the frame in pixels. It is of type `import('../core/math/vec4.js').Vec4`.
- `pivot`: The pivot of the frame - values are between 0-1. It is of type `import('../core/math/vec2.js').Vec2`.
- `border`: The border of the frame for 9-slicing. Values are ordered as follows: left, bottom, right, top border in pixels. It is of type `import('../core/math/vec4.js').Vec4`.

If the frame with the given `key` already exists, its properties are updated with the new values. Otherwise, a new frame is created with the given `key` and `data` properties.

#### removeFrame(key)

The `removeFrame` method removes a frame from the texture atlas. It takes one parameter: `key`, which is the key of the frame to be removed.

#### destroy()

The `destroy` method frees up the underlying texture owned by the atlas.

### Example

```javascript
var atlas = new pc.TextureAtlas();
atlas.frames = {
    '0': {
        // rect has u, v, width and height in pixels
        rect: new pc.Vec4(0, 0, 256, 256),
        // pivot has x, y values between 0-1 which define the point
        // within the frame around which rotation and scale is calculated
        pivot: new pc.Vec2(0.5, 0.5),
        // border has left, bottom, right and top in pixels defining regions for 9-slicing
        border: new pc.Vec4(5, 5, 5, 5)
    },
    '1': {
        rect: new pc.Vec4(256, 0, 256, 256),
        pivot: new pc.Vec2(0.5, 0.5),
        border: new pc.Vec4(5, 5, 5, 5)
    }
};

atlas.setFrame('1', {
    rect: new pc.Vec4(0, 0, 128, 128),
    pivot: new pc.Vec2(0.5, 0.5),
    border: new pc.Vec4(5, 5, 5, 5)
});

atlas.removeFrame('1');

atlas.destroy();
```

In the above example, a new instance of the `TextureAtlas` class is created. The `frames` property is set to an object that contains two frames with keys `0` and `1`. The `setFrame` method is called to update the properties of the frame with key `1`. The `removeFrame` method is called to remove the frame with key `1`. Finally, the `destroy` method is called to free up the underlying texture owned by the atlas.
## Questions: 
 1. What is the purpose of the TextureAtlas class?
    
    The TextureAtlas class contains a number of frames from a texture, where each frame defines a region in a texture, and is referenced by Sprites.

2. What are the properties of a frame in the texture atlas?
    
    A frame in the texture atlas has properties such as rect (u, v, width, height in pixels), pivot (x, y values between 0-1 which define the point within the frame around which rotation and scale is calculated), and border (left, bottom, right and top in pixels defining regions for 9-slicing).

3. How can a developer set or remove a frame in the texture atlas?
    
    A developer can set a new frame in the texture atlas using the `setFrame` method, which takes a key and data object containing properties of the frame. A developer can remove a frame from the texture atlas using the `removeFrame` method, which takes a key of the frame to be removed.