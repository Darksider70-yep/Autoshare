# Autoshare — HTML Tags & CSS Properties Reference

> One-line explanation of every HTML tag and CSS property used across `index.html` and `style.css`.

---

## 📄 HTML Tags

| Tag | One-Line Explanation |
|---|---|
| `<!DOCTYPE html>` | Tells the browser this document uses HTML5 (not older versions). |
| `<html lang="en">` | Root element that wraps the entire HTML page; `lang` sets the document language. |
| `<head>` | Container for metadata (invisible to users) like title, links, and meta tags. |
| `<meta charset="UTF-8">` | Declares the character encoding so special characters display correctly. |
| `<meta name="viewport">` | Makes the page responsive by controlling zoom and width on mobile devices. |
| `<title>` | Sets the text shown on the browser tab and in search engine results. |
| `<meta name="description">` | Provides a short page summary used by search engines as a snippet. |
| `<link rel="stylesheet">` | Links an external CSS file to apply styles to this HTML document. |
| `<body>` | Contains all visible page content that the user sees in the browser. |
| `<div>` | Generic block-level container used to group elements for layout and styling. |
| `<!-- comment -->` | HTML comment ignored by the browser, used for developer notes in code. |
| `<header>` | Semantic tag representing the top navigation/branding section of the page. |
| `<a>` | Anchor tag that creates a hyperlink; `href` sets the link destination. |
| `<nav>` | Semantic tag that groups the main navigation links of the page. |
| `<button>` | Creates a clickable button; can trigger JS actions or submit a form. |
| `<i>` | Inline element used here to host Lucide icon SVGs via the `data-lucide` attribute. |
| `<main>` | Semantic tag for the primary, unique content area of the page. |
| `<section>` | Semantic tag grouping thematically related content, typically with a heading. |
| `<h1>` | The most important page heading; only one per page is recommended for SEO. |
| `<h2>` | Second-level heading used for major section titles (e.g., "Active Ride Offers"). |
| `<h3>` | Third-level heading used for card/panel titles (e.g., stats card, modal header). |
| `<h4>` | Fourth-level heading used for student names inside ride cards and the chat panel. |
| `<h5>` | Fifth-level heading used for small item names in the hotspot destination list. |
| `<span>` | Inline generic container used to apply styles to a portion of inline text. |
| `<p>` | Defines a paragraph of text content. |
| `<label>` | Associates a text description with a form input for usability and accessibility. |
| `<select>` | Dropdown menu element containing `<option>` items for the user to choose. |
| `<option>` | Defines a single selectable item inside a `<select>` dropdown. |
| `<input>` | Creates an interactive field for user data entry — types used: `text`, `number`, `time`, `hidden`. |
| `<form>` | Wraps form inputs and manages submission; `id` links it to JavaScript handling. |
| `<small>` | Renders text in a smaller size, used here for hint/helper text below inputs. |
| `<footer>` | Semantic tag for the bottom section of the page, typically for copyright/credits. |
| `<script>` | Embeds or links JavaScript; `src` attribute loads an external JS file. |

---

## 🎨 CSS Properties

### Layout & Box Model

| Property | One-Line Explanation |
|---|---|
| `display` | Controls how an element is rendered — `flex`, `grid`, `block`, `none`, `inline-flex`. |
| `flex-direction` | Sets the axis of a flex container — `row` (horizontal) or `column` (vertical). |
| `flex` | Shorthand for grow/shrink/basis; `flex: 1` means the item fills available space. |
| `align-items` | Aligns flex/grid children along the cross-axis (e.g., `center`, `flex-start`). |
| `justify-content` | Aligns flex/grid children along the main-axis (e.g., `space-between`, `center`). |
| `align-self` | Overrides `align-items` for a single flex child independently. |
| `gap` | Sets uniform spacing between flex or grid children. |
| `grid-template-columns` | Defines the column structure of a CSS Grid layout. |
| `grid-template-rows` | Defines the row structure of a CSS Grid layout. |
| `margin` | Sets outer spacing around an element; `auto` centres elements horizontally. |
| `padding` | Sets inner spacing between the element's border and its content. |
| `width` | Sets the horizontal size of an element. |
| `height` | Sets the vertical size of an element. |
| `max-width` | Caps the maximum width an element can grow to. |
| `max-height` | Caps the maximum height an element can grow to. |
| `min-height` | Ensures an element never shrinks below a minimum height. |
| `box-sizing` | `border-box` includes padding and border in the declared width/height. |
| `overflow` | Controls what happens when content exceeds its container (`hidden`, `auto`, `scroll`). |
| `overflow-x` | Independently controls horizontal overflow — used here to prevent a side scrollbar. |
| `overflow-y` | Independently controls vertical overflow — used to enable scroll in the chat panel. |
| `position` | Sets positioning mode: `static`, `relative`, `absolute`, `fixed`, or `sticky`. |
| `top / bottom / left / right` | Offsets a positioned element from its reference edge. |
| `z-index` | Controls the stacking order of overlapping elements; higher numbers appear on top. |

---

### Typography

| Property | One-Line Explanation |
|---|---|
| `font-family` | Sets the typeface(s) to use; fallback fonts are listed after the primary one. |
| `font-size` | Sets the size of text using `rem`, `px`, or `em` units. |
| `font-weight` | Controls text boldness — `400` = normal, `700` = bold, `800` = extra-bold. |
| `line-height` | Sets vertical spacing between lines of text for readability. |
| `letter-spacing` | Adjusts horizontal space between individual characters. |
| `text-decoration` | Adds or removes underline, overline, or strikethrough on text. |
| `text-transform` | Changes text case — `uppercase`, `lowercase`, or `capitalize`. |
| `text-align` | Aligns text horizontally: `left`, `center`, or `right`. |
| `color` | Sets the foreground (text) colour of an element. |
| `opacity` | Sets element transparency from `0` (invisible) to `1` (fully opaque). |
| `-webkit-text-fill-color` | WebKit-specific property to fill text with a colour; used to make gradient text transparent. |

---

### Backgrounds & Visual Effects

| Property | One-Line Explanation |
|---|---|
| `background` | Shorthand for colour, image, gradient, repeat, and position in one declaration. |
| `background-color` | Sets a solid fill colour for the element's background area. |
| `background-image` | Sets one or more images or gradients as the background. |
| `background-attachment` | `fixed` pins the background to the viewport so it doesn't scroll with the page. |
| `background-clip` | Clips the background to a specific region — `text` clips it to the letter shapes. |
| `-webkit-background-clip` | Vendor-prefixed version of `background-clip` for older WebKit/Blink browsers. |
| `linear-gradient()` | CSS function creating a smooth colour transition along a straight line. |
| `radial-gradient()` | CSS function creating a circular/elliptical colour fade from a centre point. |
| `backdrop-filter` | Applies blur or effects to what is visible *behind* an element (frosted-glass effect). |
| `-webkit-backdrop-filter` | Vendor-prefixed version of `backdrop-filter` required by Safari. |
| `box-shadow` | Adds a drop shadow or inner glow to an element's box. |
| `border` | Shorthand for border width, style, and colour on all four sides at once. |
| `border-top / border-bottom / border-left` | Applies a border to one specific side of an element. |
| `border-radius` | Rounds the corners of an element's border box. |
| `border-color` | Sets only the colour of an element's border without changing width or style. |
| `outline` | Drawn outside the border box — setting `none` removes the default focus ring on inputs. |

---

### Transforms & Animations

| Property | One-Line Explanation |
|---|---|
| `transform` | Applies 2D/3D visual changes: `rotate()`, `scale()`, `translateX()`, `translateY()`. |
| `transition` | Smoothly animates a property change over a specified duration and easing curve. |

---

### Sizing & Appearance

| Property | One-Line Explanation |
|---|---|
| `cursor` | Changes the mouse cursor shape on hover — `pointer` shows the hand/click cursor. |
| `appearance` | `none` removes the browser's default native styling (e.g., the select dropdown arrow). |
| `pointer-events` | `none` makes an element completely unclickable and non-interactive. |
| `object-fit` | `cover` scales an `<img>` to fill its container while preserving aspect ratio. |

---

## 🔧 CSS Custom Properties (Variables — defined in `:root`)

| Variable | One-Line Explanation |
|---|---|
| `--bg-primary` | Deepest background colour (`#0b0f19`) — almost pure dark navy. |
| `--bg-secondary` | Mid-level card background (`#131b2e`). |
| `--bg-tertiary` | Slightly lighter surface used for hovered/active elements (`#1e2942`). |
| `--accent-gold` | Primary brand colour — the golden yellow (`#ffbe1a`) used on all CTAs and accents. |
| `--accent-gold-hover` | Darker shade of gold for hover/active button states (`#e0a30b`). |
| `--accent-gold-glow` | Semi-transparent gold (`rgba(255,190,26,0.2)`) for glows and focus rings. |
| `--text-primary` | Near-white text for primary readable content (`#f8fafc`). |
| `--text-secondary` | Muted grey for secondary labels and descriptions (`#94a3b8`). |
| `--text-muted` | Even more muted grey for hints and helper text (`#64748b`). |
| `--border-color` | Subtle white-tinted border (`rgba(255,255,255,0.08)`) used for card separators. |
| `--glass-bg` | Semi-transparent dark blue for glassmorphism panel backgrounds. |
| `--glass-border` | Nearly invisible white tint for glass panel borders. |
| `--color-success` | Emerald green (`#10b981`) for active/success status indicators. |
| `--color-success-bg` | Transparent emerald background for success badge fills. |
| `--color-warning` | Amber (`#f59e0b`) for warning-level status. |
| `--color-warning-bg` | Transparent amber background for warning badge fills. |
| `--color-error` | Red (`#ef4444`) for "Full" status and error badges. |
| `--color-error-bg` | Transparent red background for error badge fills. |
| `--font-main` | Primary font stack: `Plus Jakarta Sans` with system fallbacks. |
| `--border-radius-sm` | Small corner radius token — `8px`. |
| `--border-radius-md` | Medium corner radius token — `16px`. |
| `--border-radius-lg` | Large corner radius token — `24px`. |
| `--transition-smooth` | Reusable cubic-bezier transition for consistent micro-animations across the UI. |
| `--shadow-main` | Standard drop shadow (`0 8px 30px rgba(0,0,0,0.3)`) used on cards and modals. |
| `--shadow-glow` | Subtle golden glow shadow used on the logo icon and primary buttons. |

---

## 🧩 At-Rules & Pseudo-Selectors

| Rule / Selector | One-Line Explanation |
|---|---|
| `@import` | Loads an external resource (Google Font) before the rest of the stylesheet is parsed. |
| `@media (max-width: 992px)` | Applies styles only when the screen width is below 992px for responsive layout. |
| `:root` | Targets the top-level `<html>` element — the standard place to define CSS variables. |
| `*` | Universal selector matching every element; used here to reset default margins/padding. |
| `::-webkit-scrollbar` | Pseudo-element targeting the scrollbar widget in WebKit/Blink browsers. |
| `::-webkit-scrollbar-track` | Pseudo-element targeting the scrollbar background rail. |
| `::-webkit-scrollbar-thumb` | Pseudo-element targeting the draggable scrollbar handle. |
| `::before` | Pseudo-element that inserts generated content before an element's real content. |
| `:hover` | Pseudo-class that applies styles when the cursor is positioned over an element. |
| `:focus` | Pseudo-class that applies styles when an element receives keyboard or click focus. |
| `:last-child` | Pseudo-class targeting the last sibling element within its parent container. |
| `:first-child` | Pseudo-class targeting the first sibling element within its parent container. |
| `.active` | Utility class toggled by JavaScript to show/activate modals, chat panels, and toasts. |

---

*Generated for **Autoshare v1.0** — `index.html` (261 lines) · `style.css` (956 lines)*
