[View code on GitHub](https://github.com/playcanvas/engine/src/framework/handlers/loader.js)

# ResourceLoader Class

The `ResourceLoader` class is responsible for loading resource data, potentially from remote sources, and caching the resource on load to prevent multiple requests. It also adds `ResourceHandlers` to handle different types of resources.

## Constructor

The constructor takes an `app` parameter, which is an instance of `AppBase`. It initializes the `_handlers`, `_requests`, `_cache`, and `_app` properties.

```javascript
constructor(app) {
    this._handlers = {};
    this._requests = {};
    this._cache = {};
    this._app = app;
}
```

## Methods

### addHandler(type, handler)

This method adds a `ResourceHandler` for a resource type. The handler should support at least `load()` and `open()`. Handlers can optionally support `patch(asset, assets)` to handle dependencies on other assets.

```javascript
addHandler(type, handler) {
    this._handlers[type] = handler;
    handler._loader = this;
}
```

### removeHandler(type)

This method removes a `ResourceHandler` for a resource type.

```javascript
removeHandler(type) {
    delete this._handlers[type];
}
```

### getHandler(type)

This method gets a `ResourceHandler` for a resource type.

```javascript
getHandler(type) {
    return this._handlers[type];
}
```

### load(url, type, callback, asset)

This method makes a request for a resource from a remote URL. It parses the returned data using the handler for the specified type. When loaded and parsed, it uses the callback to return an instance of the resource.

```javascript
load(url, type, callback, asset) {
    const handler = this._handlers[type];
    if (!handler) {
        const err = `No resource handler for asset type: '${type}' when loading [${url}]`;
        Debug.errorOnce(err);
        callback(err);
        return;
    }

    // handle requests with null file
    if (!url) {
        this._loadNull(handler, callback, asset);
        return;
    }

    const key = url + type;

    if (this._cache[key] !== undefined) {
        // in cache
        callback(null, this._cache[key]);
    } else if (this._requests[key]) {
        // existing request
        this._requests[key].push(callback);
    } else {
        // new request
        this._requests[key] = [callback];

        const self = this;

        const handleLoad = function (err, urlObj) {
            if (err) {
                self._onFailure(key, err);
                return;
            }

            handler.load(urlObj, function (err, data, extra) {
                // make sure key exists because loader
                // might have been destroyed by now
                if (!self._requests[key]) {
                    return;
                }

                if (err) {
                    self._onFailure(key, err);
                    return;
                }

                try {
                    self._onSuccess(key, handler.open(urlObj.original, data, asset), extra);
                } catch (e) {
                    self._onFailure(key, e);
                }
            }, asset);
        };

        const normalizedUrl = url.split('?')[0];
        if (this._app.enableBundles && this._app.bundles.hasUrl(normalizedUrl)) {
            if (!this._app.bundles.canLoadUrl(normalizedUrl)) {
                handleLoad(`Bundle for ${url} not loaded yet`);
                return;
            }

            this._app.bundles.loadUrl(normalizedUrl, function (err, fileUrlFromBundle) {
                handleLoad(err, {
                    load: fileUrlFromBundle,
                    original: normalizedUrl
                });
            });
        } else {
            handleLoad(null, {
                load: url,
                original: asset && asset.file.filename || url
            });
        }
    }
}
```

### open(type, data)

This method converts raw resource data into a resource instance. For example, it takes 3D model format JSON and returns a `Model`.

```javascript
open(type, data) {
    const handler = this._handlers[type];
    if (!handler) {
        console.warn('No resource handler found for: ' + type);
        return data;
    }

    return handler.open(null, data);
}
```

### patch(asset, assets)

This method performs any operations on a resource that require a dependency on its asset data or any other asset data.

```javascript
patch(asset, assets) {
    const handler = this._handlers[asset.type];
    if (!handler)  {
        console.warn('No resource handler found for: ' + asset.type);
        return;
    }

    if (handler.patch) {
        handler.patch(asset, assets);
    }
}
```

### clearCache(url, type)

This method removes a resource from the cache.

```javascript
clearCache(url, type) {
    delete this._cache[url + type];
}
```

### getFromCache(url, type)

This method checks the cache for a resource from a URL. If present, it returns the cached value.

```javascript
getFromCache(url, type) {
    if (this._cache[url + type]) {
        return this._cache[url + type];
    }
    return undefined;
}
```

### enableRetry(maxRetries)

This method enables retrying of failed requests when loading assets. The `maxRetries` parameter is the maximum number of times to retry loading an asset. It defaults to 5.

```javascript
enableRetry(maxRetries = 5) {
    maxRetries = Math.max(0, maxRetries) || 0;

    for (const key in this._handlers) {
        this._handlers[key].maxRetries = maxRetries;
    }
}
```

### disableRetry()

This method disables retrying of failed requests when loading assets.

```javascript
disableRetry() {
    for (const key in this._handlers) {
        this._handlers[key].maxRetries = 0;
    }
}
```

### destroy()

This method destroys the resource loader.

```javascript
destroy() {
    this._handlers = {};
    this._requests = {};
    this._cache = {};
}
```

## Callbacks

### ResourceLoaderCallback

This callback is used by `ResourceLoader.load()` when a resource is loaded (or an error occurs). It takes two parameters:

- `err`: The error message in the case where the load fails.
- `resource`: The resource that has been successfully loaded.

```javascript
/**
 * Callback used by {@link ResourceLoader#load} when a resource is loaded (or an error occurs).
 *
 * @callback ResourceLoaderCallback
 * @param {string|null} err - The error message in the case where the load fails.
 * @param {*} [resource] - The resource that has been successfully loaded.
 */
```
## Questions: 
 1. What is the purpose of the `ResourceLoader` class?
- The `ResourceLoader` class is used to load resource data, potentially from remote sources, and caches the resource on load to prevent multiple requests. It also allows for the addition and removal of `ResourceHandlers` to handle different types of resources.

2. What is the `load` method used for?
- The `load` method is used to make a request for a resource from a remote URL, parse the returned data using the handler for the specified type, and return an instance of the resource using the provided callback.

3. What is the purpose of the `patch` method?
- The `patch` method is used to perform any operations on a resource that require a dependency on its asset data or any other asset data. It takes an `Asset` object and an `AssetRegistry` object as parameters.