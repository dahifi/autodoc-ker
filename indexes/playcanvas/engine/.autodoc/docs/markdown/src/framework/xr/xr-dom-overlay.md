[View code on GitHub](https://github.com/playcanvas/engine/src/framework/xr/xr-dom-overlay.js)

The code defines a class called `XrDomOverlay` that provides the ability to use DOM elements as an overlay in a WebXR AR session. It requires that the root DOM element is provided for session start. This way, input source select events are first tested against DOM Elements and then propagated down to the XR Session. If this propagation is not desirable, use the `beforexrselect` event on a DOM element and the `preventDefault` function to stop propagation.

The class has a constructor that takes a `manager` parameter, which is a WebXR Manager. It has a private `_manager` property that is set to the `manager` parameter. It also has a private `_supported` property that is set to `true` if the browser is supported and the `window.XRDOMOverlayState` is available. It has a private `_root` property that is set to `null`.

The class has a `supported` getter that returns the value of the `_supported` property. It has an `available` getter that returns `true` if the `_supported` property is `true`, the `_manager.active` property is `true`, and the `_manager._session.domOverlayState` property is not `null`.

The class has a `state` getter that returns the state of the DOM Overlay, which defines how the root DOM element is rendered. Possible options are `screen`, `floating`, and `head-locked`. It returns `null` if the `_supported` property is `false`, the `_manager.active` property is `false`, or the `_manager._session.domOverlayState` property is `null`.

The class has a `root` setter that sets the `_root` property to the value passed in if the `_supported` property is `true` and the `_manager.active` property is `false`. It has a `root` getter that returns the `_root` property.

To use the `XrDomOverlay` class, first create an instance of the `XrDomOverlay` class by passing in a `manager` parameter. Then set the `root` property to the root DOM element. Finally, start the WebXR session using the `start` method of the WebXR Manager. Here is an example:

```javascript
const xrManager = new XrManager();
const xrDomOverlay = new XrDomOverlay(xrManager);
xrDomOverlay.root = document.getElementById('root');
xrManager.start(camera, pc.XRTYPE_AR, pc.XRSPACE_LOCALFLOOR);
```

To disable input source firing `select` event when some descendant element of DOM overlay root is touched/clicked, use the `beforexrselect` event on a DOM element and the `preventDefault` function to stop propagation. Here is an example:

```javascript
someElement.addEventListener('beforexrselect', function (evt) {
    evt.preventDefault();
});
```
## Questions: 
 1. What is the purpose of the XrDomOverlay class?
- The XrDomOverlay class provides the ability to use DOM elements as an overlay in a WebXR AR session, allowing input source select events to be first tested against DOM elements and then propagated down to the XR Session.

2. How can a developer disable input source firing 'select' event when some descendant element of DOM overlay root is touched/clicked?
- A developer can use the 'beforexrselect' event on a DOM element and the 'preventDefault' function to stop propagation.

3. What are the possible options for the state of the DOM Overlay?
- The possible options for the state of the DOM Overlay are 'screen', 'floating', and 'head-locked'.