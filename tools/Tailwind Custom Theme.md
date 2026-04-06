### [Customizing your theme](https://tailwindcss.com/docs/outline-color#customizing-your-theme)

By default, Tailwind makes the entire [default color palette](https://tailwindcss.com/docs/customizing-colors#default-color-palette) available as outline colors. You can [customize your color palette](https://tailwindcss.com/docs/colors#customizing) by editing `theme.colors` or `theme.extend.colors` in your `tailwind.config.js` file.

```tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        'regal-blue': '#243c5a',
      },
    }
  }
}
```

For more https://tailwindcss.com/docs/theme