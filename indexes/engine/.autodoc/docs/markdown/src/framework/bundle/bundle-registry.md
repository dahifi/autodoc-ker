[View code on GitHub](https://github.com/playcanvas/engine/src/framework/bundle/bundle-registry.js)

# BundleRegistry Class

The `BundleRegistry` class is responsible for keeping track of which assets are in bundles and loading files from bundles. This class is used internally by the PlayCanvas engine and is not intended to be used directly by developers.

## Constructor

The constructor takes an instance of the `AssetRegistry` class as its only argument. It initializes several internal indexes and registers event listeners for when assets are added or removed from the registry.

## Methods

### _onAssetAdded(asset)

This method is called when an asset is added to the registry. If the asset is a bundle, it is added to the `_bundleAssets` index and its referenced assets are indexed in the `_assetsInBundles` index. If the asset is not a bundle, its URLs are indexed in the `_urlsInBundles` index.

### _registerBundleEventListeners(bundleAssetId)

This method registers event listeners for when a bundle asset is loaded or fails to load.

### _unregisterBundleEventListeners(bundleAssetId)

This method unregisters event listeners for a bundle asset.

### _indexAssetInBundle(assetId, bundleAsset)

This method indexes an asset and its file URLs in the `_assetsInBundles` and `_urlsInBundles` indexes, respectively.

### _indexAssetFileUrls(asset)

This method indexes the file URLs of an asset in the `_urlsInBundles` index.

### _getAssetFileUrls(asset)

This method returns an array of all possible URLs for an asset.

### _normalizeUrl(url)

This method removes query parameters from a URL.

### _onAssetRemoved(asset)

This method is called when an asset is removed from the registry. If the asset is a bundle, it is removed from the `_bundleAssets` index and its referenced assets are removed from the `_assetsInBundles` and `_urlsInBundles` indexes. If the asset is not a bundle, its URLs are removed from the `_urlsInBundles` index.

### _onBundleLoaded(bundleAsset)

This method is called when a bundle asset is loaded. It resolves any pending file requests that can be satisfied by the bundle.

### _onBundleError(err, bundleAsset)

This method is called when a bundle asset fails to load. It searches for other bundles that can satisfy any pending file requests for the URLs in the failed bundle. If no other bundles are found, the file requests are failed with the specified error.

### _findLoadedOrLoadingBundleForUrl(url)

This method finds a bundle that contains the specified URL and is either loaded or currently being loaded.

### listBundlesForAsset(asset)

This method lists all available bundles that reference the specified asset.

### list()

This method lists all available bundles, including those that are not loaded.

### hasUrl(url)

This method returns true if there is a bundle that contains the specified URL.

### canLoadUrl(url)

This method returns true if there is a bundle that contains the specified URL and that bundle is either loaded or currently being loaded.

### loadUrl(url, callback)

This method loads the specified file URL from a bundle that is either loaded or currently being loaded. The callback is called when the file has been loaded or if an error occurs.

### destroy()

This method destroys the registry and releases its resources.
## Questions: 
 1. What is the purpose of the `BundleRegistry` class?
    
    The `BundleRegistry` class keeps track of which assets are in bundles and loads files from bundles.

2. What methods are available in the `BundleRegistry` class?
    
    The `BundleRegistry` class has methods such as `listBundlesForAsset`, `list`, `hasUrl`, `canLoadUrl`, `loadUrl`, and `destroy`.

3. What is the role of the `_fileRequests` property in the `BundleRegistry` class?
    
    The `_fileRequests` property contains requests to load file URLs indexed by URL. If there are any pending file requests that can be satisfied by a specified bundle, then they are resolved.