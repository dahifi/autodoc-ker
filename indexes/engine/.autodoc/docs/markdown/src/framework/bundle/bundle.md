[View code on GitHub](https://github.com/playcanvas/engine/src/framework/bundle/bundle.js)

The `Bundle` class represents the resource of a Bundle Asset in the PlayCanvas engine. A Bundle Asset is a collection of files that are loaded together as a single unit. The purpose of this class is to map the URLs of the files in the bundle to their corresponding blob URLs. Blob URLs are used to load binary data as a URL that can be used as the source of an image, audio, or video element.

The `constructor` method of the `Bundle` class takes an array of objects as its argument. Each object in the array represents a file in the bundle and has a `name` field and a `getBlobUrl()` function. The `name` field is used as the key in the `_blobUrls` object to map the file URL to its blob URL. The `getBlobUrl()` function is called to get the blob URL for the file.

The `hasBlobUrl()` method takes a file URL as its argument and returns `true` if the blob URL for the file exists in the `_blobUrls` object, otherwise it returns `false`.

The `getBlobUrl()` method takes a file URL as its argument and returns the blob URL for the file if it exists in the `_blobUrls` object.

The `destroy()` method is used to free up the blob URLs when the bundle is no longer needed. It iterates over the `_blobUrls` object and calls `URL.revokeObjectURL()` for each blob URL to free up memory.

This class is used internally by the PlayCanvas engine to manage the loading and unloading of Bundle Assets. Developers using the engine can use this class to get the blob URL for a file in a Bundle Asset. For example:

```javascript
const bundle = new Bundle(files);
const blobUrl = bundle.getBlobUrl('file.png');
const image = new Image();
image.src = blobUrl;
```
## Questions: 
 1. What is the purpose of the `Bundle` class and how is it used in the PlayCanvas engine?
- The `Bundle` class represents the resource of a Bundle Asset, which contains an index that maps URLs to blob URLs. It is used to manage blob URLs for files in a loaded bundle.

2. What is the format of the `files` parameter in the `Bundle` constructor?
- The `files` parameter is an array of objects that have a `name` field and contain a `getBlobUrl()` function.

3. What happens when the `destroy()` method is called on a `Bundle` instance?
- The `destroy()` method frees up blob URLs by revoking object URLs for each key in the `_blobUrls` object. After calling `destroy()`, the `_blobUrls` property is set to `null`.