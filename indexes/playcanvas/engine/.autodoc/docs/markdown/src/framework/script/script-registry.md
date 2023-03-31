[View code on GitHub](https://github.com/playcanvas/engine/src/framework/script/script-registry.js)

The `ScriptRegistry` class is a container for all `ScriptType`s that are available to the PlayCanvas engine application. It is an extension of the `EventHandler` class, which allows it to handle events. The purpose of this class is to manage the scripts that are used in the application and provide a way to add, remove, and get scripts from the registry.

When an instance of the `ScriptRegistry` class is created, it takes an `AppBase` object as a parameter. This object is the application to which the registry is attached. The `_scripts` and `_list` properties are initialized as empty objects and arrays, respectively.

The `add` method is used to add a `ScriptType` to the registry. If the script already exists in the registry, and the new script has a `swap` method defined, it will perform code hot swapping automatically in an asynchronous manner. The `add` method returns `true` if the script is added for the first time or `false` if the script already exists.

The `remove` method is used to remove a `ScriptType` from the registry. It takes the name or type of the script as a parameter and returns `true` if the script is removed or `false` if it is not in the registry.

The `get` method is used to get a `ScriptType` by name. It takes the name of the script as a parameter and returns the script type if it exists in the registry or `null` otherwise.

The `has` method is used to check if a `ScriptType` with the specified name is in the registry. It takes the name or type of the script as a parameter and returns `true` if the script is in the registry.

The `list` method is used to get a list of all `ScriptType`s from the registry. It returns an array of all `ScriptType`s in the registry.

Overall, the `ScriptRegistry` class provides a way to manage the scripts used in the PlayCanvas engine application. It allows for easy addition, removal, and retrieval of scripts from the registry. It also provides a way to check if a script is in the registry and get a list of all scripts in the registry.
## Questions: 
 1. What is the purpose of the `ScriptRegistry` class?
    
    The `ScriptRegistry` class is a container for all `ScriptType`s that are available to the PlayCanvas application. It allows PlayCanvas scripts to access the Script Registry from inside the application with `AppBase#scripts`.

2. What methods are available in the `ScriptRegistry` class?
    
    The `ScriptRegistry` class has several methods available, including `add`, `remove`, `get`, `has`, and `list`. These methods allow developers to add, remove, get, check for, and list `ScriptType`s in the registry.

3. How does the `add` method work in the `ScriptRegistry` class?
    
    The `add` method in the `ScriptRegistry` class adds a `ScriptType` to the registry. If a script already exists in the registry and the new script has a `swap` method defined, it will perform code hot swapping automatically in an async manner. The method returns `true` if the script was added for the first time or `false` if the script already exists.