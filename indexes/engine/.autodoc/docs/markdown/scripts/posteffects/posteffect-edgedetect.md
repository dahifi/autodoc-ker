[View code on GitHub](https://github.com/playcanvas/engine/scripts/posteffects/posteffect-edgedetect.js)

# PlayCanvas Engine: EdgeDetectEffect

The `EdgeDetectEffect` class is a post-processing effect that applies an edge detection filter to the rendered scene. It uses the Sobel filter to calculate the intensity of the edges in the scene and applies a color and intensity to the detected edges.

## Usage

To use the `EdgeDetectEffect` in a PlayCanvas project, you can create an instance of the `EdgeDetect` script and attach it to a camera entity. The script will automatically add the effect to the camera's post-processing queue.

```javascript
var cameraEntity = app.root.findByName('Camera');
var edgeDetect = cameraEntity.addComponent('script');
edgeDetect.script.create('edgeDetect', {
    intensity: 1.5,
    color: [1, 0, 0, 1]
});
```

## Constructor

### EdgeDetectEffect(graphicsDevice)

Creates a new instance of the `EdgeDetectEffect` post effect.

- `graphicsDevice` - The graphics device of the application.

## Properties

### resolution

A `Float32Array` that represents the resolution of the input target.

### intensity

A `float` that represents the intensity of the edge detection effect.

### color

A `pc.Color` that represents the color of the detected edges.

## Methods

### render(inputTarget, outputTarget, rect)

Renders the effect to the output target.

- `inputTarget` - The input target to render.
- `outputTarget` - The output target to render to.
- `rect` - The rectangle to render to.

## Script Attributes

### intensity

A `number` that represents the intensity of the edge detection effect. The default value is `1` and the valid range is `0` to `2`.

### color

An `rgba` color that represents the color of the detected edges. The default value is `[0.5, 0.5, 0.5, 1]`.

## Example

```javascript
var cameraEntity = app.root.findByName('Camera');
var edgeDetect = cameraEntity.addComponent('script');
edgeDetect.script.create('edgeDetect', {
    intensity: 1.5,
    color: [1, 0, 0, 1]
});
```

This code creates a new instance of the `EdgeDetect` script and attaches it to a camera entity. It sets the intensity of the effect to `1.5` and the color of the detected edges to red. The effect will be automatically added to the camera's post-processing queue.
## Questions: 
 1. What does this code do?
- This code defines a post effect called EdgeDetectEffect that uses a Sobel filter to detect edges in an image. It creates a new instance of the effect and sets its intensity and color attributes. It also defines a script called EdgeDetect that initializes the effect and adds it to the camera's post effects queue.

2. What is the purpose of the "cnv" array in the fragment shader?
- The "cnv" array is used to store the convolution values for the two masks used in the Sobel filter. These values are squared and then added together to get the final edge detection intensity value.

3. What is the significance of the "attr" event listener in the EdgeDetect script?
- The "attr" event listener is used to update the effect's attributes (intensity and color) whenever they are changed in the editor. This allows the effect to be customized without having to modify the script code directly.