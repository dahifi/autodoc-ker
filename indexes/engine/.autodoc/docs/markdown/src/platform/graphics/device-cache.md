[View code on GitHub](https://github.com/playcanvas/engine/src/platform/graphics/device-cache.js)

# DeviceCache Class

The `DeviceCache` class is a cache that stores shared resources associated with a device. The resources are removed from the cache when the device is destroyed. This class is used internally in the PlayCanvas engine project.

## Properties

### _cache

This is a private property that stores the resource for each `GraphicsDevice`. It is a `Map` object that maps a `GraphicsDevice` to a resource.

```javascript
_cache = new Map();
```

## Methods

### get(device, onCreate)

This method returns the resources for the supplied `GraphicsDevice`. If the resource does not exist in the cache, it is created using the `onCreate` function and added to the cache. The `onCreate` function is a callback function that is called when the resource needs to be created.

```javascript
get(device, onCreate) {
    if (!this._cache.has(device)) {
        this._cache.set(device, onCreate());

        // when the device is destroyed, destroy and remove its entry
        device.on('destroy', () => {
            this.remove(device);
        });

        // when the context is lost, call optional loseContext on its entry
        device.on('devicelost', () => {
            this._cache.get(device)?.loseContext?.(device);
        });
    }

    return this._cache.get(device);
}
```

### remove(device)

This method destroys and removes the content of the cache associated with the `GraphicsDevice`.

```javascript
remove(device) {
    this._cache.get(device)?.destroy?.(device);
    this._cache.delete(device);
}
```

## Usage

The `DeviceCache` class is used to store shared resources associated with a `GraphicsDevice`. It is used internally in the PlayCanvas engine project to manage resources such as textures, shaders, and buffers. When a resource is needed, the `get` method is called with the `GraphicsDevice` as the argument. If the resource does not exist in the cache, it is created using the `onCreate` function and added to the cache. When the `GraphicsDevice` is destroyed, the resource is automatically removed from the cache. 

```javascript
const deviceCache = new DeviceCache();

const device = new GraphicsDevice();

const texture = deviceCache.get(device, () => {
    // create texture
    return new Texture(device, {
        width: 256,
        height: 256,
        format: PIXELFORMAT_R8_G8_B8_A8
    });
});

// use texture

device.destroy();

// texture is automatically removed from cache
```
## Questions: 
 1. What is the purpose of this code and how is it used in the PlayCanvas engine?
- This code defines a class called `DeviceCache` that stores shared resources associated with a graphics device. It is used to cache resources and remove them when the device is destroyed.

2. What is the `_cache` property and how is it used?
- The `_cache` property is a `Map` that stores the resource for each `GraphicsDevice`. It is used to retrieve and store resources associated with a device.

3. What happens when a device is destroyed or its context is lost?
- When a device is destroyed, its entry in the cache is removed. When its context is lost, the optional `loseContext` function is called on its entry.