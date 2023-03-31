[View code on GitHub](https://github.com/playcanvas/engine/src/framework/i18n/constants.js)

This code defines two constants related to localization in the PlayCanvas engine project. The first constant, `DEFAULT_LOCALE`, sets the default locale to 'en-US'. This means that if no specific locale is specified, the code will default to using the English language with US regional settings.

The second constant, `DEFAULT_LOCALE_FALLBACKS`, defines a set of fallback locales for specific languages. For example, if the desired locale is 'en-AS' (English language with American Samoa regional settings), but the project only has 'en-US' and 'en-GB' locales available, the code will fallback to using 'en-US'. If 'en-US' is also not available, the code will pick the first locale that satisfies the language, which in this case would be 'en-GB'.

This constant is useful for ensuring that the project can still display content in the user's preferred language, even if a specific regional setting is not available. It also allows for more flexibility in the localization process, as developers can focus on creating translations for the most commonly used regional settings and rely on fallbacks for less common ones.

Here is an example of how this constant could be used in the PlayCanvas engine project:

```javascript
// get the user's preferred language and regional settings
const userLocale = navigator.language;

// check if the desired locale is available, otherwise fallback to a default
const localeToUse = DEFAULT_LOCALE_FALLBACKS[userLocale] || DEFAULT_LOCALE;

// load the appropriate localization data for the chosen locale
loadLocalizationData(localeToUse);
```

In this example, the code first gets the user's preferred language and regional settings using the `navigator.language` property. It then checks if the desired locale is available in the project's localization data, using the `DEFAULT_LOCALE_FALLBACKS` constant to determine the fallback locale if necessary. Finally, it loads the appropriate localization data for the chosen locale using a `loadLocalizationData` function (not shown).
## Questions: 
 1. What is the purpose of the `DEFAULT_LOCALE` constant?
   - The `DEFAULT_LOCALE` constant is used as a fallback locale if a specific locale is not found.

2. What is the structure of the `DEFAULT_LOCALE_FALLBACKS` object?
   - The `DEFAULT_LOCALE_FALLBACKS` object maps language codes to their corresponding fallback locales.

3. How are fallback locales chosen if a specific locale is not found?
   - If a specific locale is not found, the fallback locale is chosen based on the language code. If a fallback for the specific language code is not found, the first locale that satisfies the language is chosen.