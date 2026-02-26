# Product Requirements Document (PRD)

**Project**: Premium Interactive Content Platform
**Date**: 2026-02-26
**Status**: Living Document

---

## 1. Overview

This platform delivers two premium, single-page interactive web experiences built with pure HTML5, CSS3, and vanilla JavaScript — no frameworks. Each application combines sophisticated visual storytelling with rich interactivity to create immersive, presentation-grade content.

### Applications

| Application | Purpose | Audience |
|---|---|---|
| **Rta — Right Time, Right Action** | Philosophical exploration of natural intelligence and decision-making frameworks | General / Educational |
| **The Hour Glass** | Confidential strategic analysis document for The Hour Glass luxury watch retailer | AKQA / Client stakeholders |

---

## 2. Product Goals

1. **Immersive storytelling** — Convey complex ideas through interactive visuals rather than static text.
2. **Zero-dependency performance** — Achieve rich interactivity without external JavaScript frameworks to minimise load time and maximise control.
3. **Accessibility-aware design** — Respect user preferences (reduced motion, responsive scaling) while maintaining visual impact.
4. **Presentation-grade polish** — Every interaction, animation, and transition should feel intentional and premium.

---

## 3. Application Details

### 3.1 Rta — Right Time, Right Action (`index.html`)

#### Purpose
An interactive educational experience exploring five layers of natural intelligence and how they inform decision-making.

#### Key Features

| Feature | Description |
|---|---|
| **Particle Canvas Hero** | Mouse-reactive star field where particles repel from the cursor within a 150px radius |
| **Five Intelligences Orbital System** | Interactive SVG orbital visualization with clickable planets (Natural, Human, Moral, Temporal, Attention) orbiting at different speeds |
| **The Stack — Cosmos to Earth** | Six descending layers (Insight, Strategy, Taste, Execution, Embedding, Rhythm) with corruption warnings at each level |
| **Waterfall Canvas** | Physics-based water droplets that flow downward with wobble, responding to mouse position |
| **Human / Agent Toggle** | Panel switcher showing two perspectives on how intelligence manifests |
| **Scroll Reveal Animations** | Elements animate into view as the user scrolls, with staggered timing |
| **Return to Cosmos** | Smooth-scroll back-to-top navigation |

#### Design System
- **Typography**: Instrument Serif (headings), DM Sans (body)
- **Palette**: Nature-inspired — moss greens, ambers, cyans, warm earth tones
- **Texture**: Grain overlays, topographic background patterns

---

### 3.2 The Hour Glass (`the-hour-glass.html`)

#### Purpose
A password-protected strategic presentation for The Hour Glass, a luxury watch retailer, analysing market position, competitive landscape, and projected business impact.

#### Key Features

| Feature | Description |
|---|---|
| **Password Gate** | Client-side authentication with error animations before granting access to the document |
| **Word-Reveal Hero** | Title animates character-by-character ("The" → "Hour" → "Glass") with an animated underline rule |
| **Market Signal Stats** | Animated counters displaying key market metrics (Swiss watch exports, U.S. exports, etc.) |
| **Position Section** | Two-column layout: company scale (S$1.16B revenue, 70+ boutiques) alongside philosophy (physical-first, connoisseurship over commerce) |
| **Competitive Frame Slider** | Touch/keyboard-navigable slider comparing The Hour Glass against Cortina Watch, Watches of Switzerland, and Hodinkee across multiple frames |
| **Interactive Impact Chart** | SVG stacked-area chart projecting S$ millions across 6 business layers over 5 years, with toggleable layers and real-time total recalculation |
| **Viewport-Aware Video** | Embedded videos auto-play/pause based on scroll visibility |
| **Parallax Effects** | Subtle scroll-based parallax on desktop, disabled on mobile for performance |

#### Design System
- **Typography**: Cormorant Garamond (headings), Inter (body)
- **Palette**: Luxury-minimal — black, white, dark gray, minimal accent colours
- **Aesthetic**: High-contrast editorial with strong content hierarchy

---

## 4. Technical Architecture

### Stack
- **HTML5** — Semantic markup, `<video>`, inline SVG
- **CSS3** — Custom properties, `clamp()` fluid typography, keyframe animations, flexbox/grid
- **Vanilla JavaScript** — Canvas API, IntersectionObserver, requestAnimationFrame, SVG DOM manipulation, touch/keyboard event handling

### Performance Considerations
- Particle counts scale with viewport size (1 particle per 2,500–3,500 px)
- Device pixel ratio handling for crisp canvas rendering
- Lazy loading for images
- IntersectionObserver for efficient scroll-triggered work (no polling)

### Accessibility
- `prefers-reduced-motion` detection disables animations when the user prefers reduced motion
- Fluid `clamp()`-based typography adapts from mobile to desktop without breakpoints
- Full keyboard navigation support for sliders and interactive elements
- Touch swipe gesture support on mobile

---

## 5. Non-Functional Requirements

| Requirement | Target |
|---|---|
| **External dependencies** | Zero runtime JS dependencies |
| **Browser support** | Modern evergreen browsers (Chrome, Safari, Firefox, Edge) |
| **Responsive** | Fluid layout from 320px to 2560px+ viewports |
| **Performance** | First Contentful Paint < 1.5s on broadband; smooth 60fps animations |
| **Motion safety** | All animations respect `prefers-reduced-motion: reduce` |

---

## 6. Content & Assets

### Fonts (Google Fonts CDN)
- Instrument Serif, DM Sans (Rta)
- Cormorant Garamond, Inter (The Hour Glass)

### Media
- Embedded video content in The Hour Glass (viewport-triggered playback)
- Inline SVG for charts, orbital systems, and decorative elements
- Canvas-rendered particle effects (stars, waterfall)

---

## 7. Future Considerations

- **CMS integration** — Extract content into a headless CMS for easier updates by non-technical stakeholders.
- **Analytics** — Add lightweight event tracking to measure engagement with interactive elements (chart toggles, slider navigation, orbital clicks).
- **Dark/Light mode** — Rta's earthy palette could adapt; The Hour Glass could offer a light variant.
- **i18n** — Multi-language support if the platform expands to non-English markets.
- **Component extraction** — Reusable modules (particle canvas, stat counters, scroll-reveal) could be extracted into a shared library for future projects.
