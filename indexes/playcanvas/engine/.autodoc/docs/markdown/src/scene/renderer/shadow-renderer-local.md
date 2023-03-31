[View code on GitHub](https://github.com/playcanvas/engine/src/scene/renderer/shadow-renderer-local.js)

The `ShadowRendererLocal` class is responsible for rendering shadows for local lights in the PlayCanvas engine. Local lights are lights that have a position and a limited range, as opposed to directional lights which have no position and infinite range. The class contains methods for culling shadow casters, preparing lights for rendering shadows, and setting up render passes for rendering shadows.

The `cull` method is responsible for culling shadow casters for a given light. It first checks if the light has a shadow map allocated, and if not, it creates one. It then calculates the number of faces to render based on the light type (spot or omni), and for each face, it sets up a shadow camera and culls shadow casters using the `shadowRenderer.cullShadowCasters` method.

The `prepareLights` method is responsible for preparing lights for rendering shadows. It takes an array of `lights` and adds any lights that need to render shadows to the `shadowLights` array. It then prepares each face of the shadow camera for each light that needs to render shadows.

The `prepareClusteredRenderPass` method sets up a render pass for rendering shadows for local clustered lights. It first prepares the shadow cameras for rendering, and then sets up the render pass using any of the cameras. It then renders shadows for each light in the `shadowLights` array, and clears the array when done.

The `setupNonClusteredFaceRenderPass` method sets up a render pass for rendering a single face of a shadow map for a non-clustered light. It prepares the shadow camera for rendering, creates a new render pass, and sets up the render pass using the shadow camera. It then adds the render pass to the frame graph.

The `buildNonClusteredRenderPasses` method sets up render passes for rendering shadows for local non-clustered lights. It loops through each light, and if the light needs to render shadows, it sets up a render pass for each face of the shadow map.

Overall, the `ShadowRendererLocal` class is an important part of the PlayCanvas engine's rendering pipeline, as it enables local lights to cast shadows. It provides methods for culling shadow casters, preparing lights for rendering shadows, and setting up render passes for rendering shadows. These methods are used in conjunction with other parts of the engine to render shadows for local lights.
## Questions: 
 1. What is the purpose of this code file?
- This code file contains the implementation of the `ShadowRendererLocal` class, which is responsible for rendering shadows for local lights in the PlayCanvas engine.

2. What types of lights are supported for shadow rendering?
- The code supports two types of lights for shadow rendering: `LIGHTTYPE_OMNI` for omni-directional lights and `LIGHTTYPE_SPOT` for spot lights.

3. How are the shadow maps allocated and rendered?
- The code allocates shadow maps for lights unless in clustered lighting mode, and then culls shadow casters and renders shadows for each face of the light's shadow map. For non-clustered lights, each shadow face is rendered in a separate render pass to a separate render target.