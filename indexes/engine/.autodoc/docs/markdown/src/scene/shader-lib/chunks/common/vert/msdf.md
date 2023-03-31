[View code on GitHub](https://github.com/playcanvas/engine/src/scene/shader-lib/chunks/common/vert/msdf.js)

The code above is a GLSL shader code that defines a function called `unpackMsdfParams()`. This function is responsible for unpacking and decoding two sets of vertex attributes (`vertex_outlineParameters` and `vertex_shadowParameters`) that are used to render text with multi-channel signed distance field (MSDF) fonts. 

The `unpackMsdfParams()` function first extracts the little and big components of the `vertex_outlineParameters` attribute. The little component is obtained by taking the modulus of the attribute with 256, while the big component is obtained by subtracting the little component from the original attribute and dividing the result by 256. The little component encodes the red and blue channels of the outline color, while the big component encodes the green and alpha channels of the outline color. The outline thickness is obtained by dividing the little.z component by 255 and multiplying the result by a constant value of 0.2.

The function then proceeds to extract the little and big components of the `vertex_shadowParameters` attribute using the same approach as before. The little component encodes the red and blue channels of the shadow color, while the big component encodes the green and alpha channels of the shadow color. The shadow offset is obtained by remapping the z components of the little and big components from the range [0, 254] to the range [-1, 1] and multiplying the result by a constant value of 0.005.

Overall, this code is an essential part of the PlayCanvas engine's text rendering pipeline. It allows the engine to efficiently decode and extract the necessary information from the vertex attributes of MSDF fonts, which are used to render high-quality text with crisp outlines and soft shadows. Here is an example of how this code might be used in a larger project:

```javascript
// create a new material for text rendering
const textMaterial = new pc.StandardMaterial();

// set the shader code for the material
textMaterial.shader = new pc.Shader(device, {
    attributes: {
        vertex_outlineParameters: pc.SEMANTIC_ATTR0,
        vertex_shadowParameters: pc.SEMANTIC_ATTR1
    },
    vshader: /* glsl */`
        attribute vec3 vertex_outlineParameters;
        attribute vec3 vertex_shadowParameters;

        varying vec4 outline_color;
        varying float outline_thickness;
        varying vec4 shadow_color;
        varying vec2 shadow_offset;

        void main() {
            // unpack the MSDF parameters
            unpackMsdfParams();

            // pass the parameters to the fragment shader
            gl_Position = getPosition();
            outline_color.a = 1.0;
            shadow_color.a = 1.0;
            vUv0 = getUv();
        }
    `,
    fshader: /* glsl */`
        varying vec4 outline_color;
        varying float outline_thickness;
        varying vec4 shadow_color;
        varying vec2 shadow_offset;

        void main() {
            // render the text with the MSDF parameters
            gl_FragColor = renderText(outline_color, outline_thickness, shadow_color, shadow_offset);
        }
    `
});

// create a new text entity
const textEntity = new pc.Entity();
textEntity.addComponent('element', {
    type: 'text',
    text: 'Hello, world!',
    fontAsset: fontAsset,
    material: textMaterial
});

// add the text entity to the scene
app.root.addChild(textEntity);
``` 

In this example, the `textMaterial` object is created with the GLSL shader code that includes the `unpackMsdfParams()` function. The `textEntity` object is then created with a text component that specifies the font asset and the material to use for rendering the text. When the text is rendered, the `unpackMsdfParams()` function is called to extract the necessary MSDF parameters from the vertex attributes, which are then passed to the fragment shader for rendering the text with crisp outlines and soft shadows.
## Questions: 
 1. What is the purpose of this code and how is it used in the PlayCanvas engine?
   - This code defines a GLSL shader function called `unpackMsdfParams()` that unpacks outline and shadow parameters for a mesh. It is used to set the color, thickness, and offset of the mesh's outline and shadow.
2. What are the expected input and output types for this function?
   - The function takes in two attribute vectors of type `vec3` called `vertex_outlineParameters` and `vertex_shadowParameters`. It outputs four varying variables of type `vec4` and `float` called `outline_color`, `shadow_color`, `outline_thickness`, and `shadow_offset`.
3. What are the values of `_outlineThicknessScale` and `_shadowOffsetScale` and how do they affect the output of this function?
   - The value of `_outlineThicknessScale` is 0.2 and it is used to scale the outline thickness value. The value of `_shadowOffsetScale` is 0.005 and it is used to scale the shadow offset value. These values are used to remap the input values to the desired output range.