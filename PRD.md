# Product Requirements Document (PRD)
## Ṛta Intelligence & The Hour Glass — Strategic Digital Deliverables

**Author:** AKQA
**Date:** February 2026
**Status:** In Development
**Repository:** `superhotmaki/main`

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Deliverable 1: Ṛta Intelligence Landing Page](#2-deliverable-1-ṛta-intelligence-landing-page)
3. [Deliverable 2: The Hour Glass Strategic Document](#3-deliverable-2-the-hour-glass-strategic-document)
4. [Technical Architecture](#4-technical-architecture)
5. [Design System](#5-design-system)
6. [Interaction & Animation Specifications](#6-interaction--animation-specifications)
7. [Content Inventory](#7-content-inventory)
8. [Accessibility & Performance](#8-accessibility--performance)
9. [Development History & Iterations](#9-development-history--iterations)

---

## 1. Executive Summary

This project consists of **two self-contained, single-page HTML deliverables** designed to serve as premium digital presentations:

1. **Ṛta Intelligence (`index.html`)** — An immersive, interactive landing page presenting the Ṛta Intelligence Framework, a philosophical model for how natural, human, moral, temporal, and attention intelligences inform decision-making. Positioned as a brand/thought-leadership piece.

2. **The Hour Glass (`the-hour-glass.html`)** — A password-protected strategic pitch document from AKQA to The Hour Glass (a luxury watch retail group). It presents a market analysis, competitive audit, strategic opportunities, AKQA's capabilities, and a five-year financial projection with interactive data visualisation.

Both deliverables are **zero-dependency, single-file HTML** — no build tools, no frameworks, no external JavaScript libraries. All CSS, JS, and content are inline. They are designed for **private, confidential sharing** via direct URL.

---

## 2. Deliverable 1: Ṛta Intelligence Landing Page

### 2.1 Purpose & Concept

A visually rich, interactive page presenting the **Ṛta Intelligence Framework** — a philosophy rooted in the Vedic concept of "Ṛta" (cosmic order/natural law). The tagline is **"Right Time, Right Action."**

The page communicates a layered intelligence model where technology serves (never decides), and earth/reality is the final judge. It is a brand/thought-leadership piece, not a product page.

### 2.2 Sections (Top to Bottom)

| # | Section | Description |
|---|---------|-------------|
| 1 | **Hero** | Full-viewport. Animated particle canvas background with mouse-reactive stars. Title "Ṛta" with cyan accent on the Ṛ character. Subtitle: "Right Time, Right Action". Four stats displayed: 5 intelligences, ∞ feedback loops, 1 rule, 0 shortcuts. Animated scroll hint at bottom ("DESCEND" with bouncing arrow). |
| 2 | **Philosophy Quote** | Centered blockquote in amber/gold serif: *"Intelligence flows downward like water; wisdom rises back like roots."* |
| 3 | **Leaf Divider** | Custom SVG leaf-vein pattern divider used between all major sections. |
| 4 | **Five Intelligences — Orbital System** | Interactive orbital/planetary system. Five "planets" orbit a central "Ṛta" core at different speeds and radii. Each planet is clickable, revealing a detail panel with name, essence, and quote. |
| 5 | **The Stack — Waterfall** | Five descending layers (Insight → Strategy → Taste → Technology → Earth/Reality) presented as cards. Each has numbered header, title, subtitle, principles list, and a warning callout. Background canvas with waterfall particle effect. |
| 6 | **Two-Cell Architecture** | Toggle between "Human Cell" and "Agent Cell" views. Human Cell shows three roles: Steward, Systems Misfit, Culture Listener. Agent Cell shows five roles: Observation, Pattern, Documentation, Calendar, Scenario. Memory thread tagline below each. |
| 7 | **Feedback Loop** | Circular diagram with four nodes (Cosmos, Humans, Earth, Nature) orbiting an infinity symbol center. Tagline: *"Earth is the final judge — not the market, not the mind."* |
| 8 | **Footer** | "Return to Cosmos" link back to hero. Credits: "Ṛta Intelligence Framework" / "Technology serves. Earth judges. Wisdom takes time." |

### 2.3 Five Intelligences (Data)

| Intelligence | Emoji | Orbit Radius | Speed | Essence | Quote |
|-------------|-------|-------------|-------|---------|-------|
| Natural | 🌿 | 160px (innermost) | 25s | Land, seasons, soil, water, ecology, body, animals, materials | "Listening before extracting" |
| Human | 🤲 | 240px | 35s | Emotion, relationship, culture, craft, community | "How we live with one another" |
| Moral | ⚖️ | 320px | 45s | Restraint, responsibility, non-harm, right livelihood | "Just because we can doesn't mean we should" |
| Temporal | ⏳ | 400px | 55s | Patience, long arcs, intergenerational thinking, legacy | "Playing games worth finishing after we're gone" |
| Attention | ◉ | 480px (outermost) | 60s | What we notice, what we ignore, what we feed | "Attention becomes reality" |

### 2.4 The Stack Layers (Data)

| Layer | Title | Subtitle | Warning |
|-------|-------|----------|---------|
| 1 | Insight | Cosmic Rhythm — the pattern behind the pattern | "Insight hoarded becomes ideology. It must flow downward or it corrupts." |
| 2 | Strategy | Shaping insight into direction without forcing outcome | "Strategy without moral intelligence becomes manipulation." |
| 3 | Taste | The felt sense of what belongs — aesthetic discernment | "Taste without humility becomes gatekeeping. Stay porous." |
| 4 | Technology | The servant layer — powerful, never sovereign | "Technology placed above taste or strategy will optimize for the wrong summit." |
| 5 | Earth / Reality | The ground truth — where all intelligence is tested | "Ignoring earth's feedback is the oldest and most expensive mistake." |

### 2.5 Hero Stats

| Value | Label |
|-------|-------|
| 5 | intelligences — layered, not ranked |
| ∞ | feedback loops — earth always answers |
| 1 | rule — technology never decides |
| 0 | shortcuts — to wisdom |

---

## 3. Deliverable 2: The Hour Glass Strategic Document

### 3.1 Purpose & Concept

A confidential, password-gated strategic pitch from **AKQA** to **The Hour Glass** — Asia-Pacific's leading luxury watch retail group (founded 1979, 70+ boutiques, S$1.16B revenue FY2025).

The document argues that The Hour Glass has an exceptional physical retail philosophy but a significant digital gap compared to competitors. AKQA proposes a comprehensive digital transformation across experience design, connected commerce, and AI-powered clienteling.

### 3.2 Password Protection

- **Password:** `akqa2026`
- **Gate UI:** Full-screen black overlay with a single centered text input. Minimal — just the input and "AKQA" brand mark at bottom-left.
- **Behavior:** On correct password, gate fades out (600ms), main content fades in with upward slide. On incorrect password, input shakes (400ms) and clears.
- **Body is locked** (overflow: hidden) until password is entered.

### 3.3 Sections (Top to Bottom)

| # | Section | ID | Type | Description |
|---|---------|-----|------|-------------|
| I | Password Gate | `password-gate` | Dark/full-screen | Single password input, AKQA branding |
| II | Hero | `hero` | Dark | Full-viewport. Word-by-word reveal animation: "The Hour Glass". Animated horizontal rule. Subtitle: "A strategic perspective on what comes next." Footer: "AKQA — Confidential — February 2026" |
| III | Michael Tay Quote + Portrait | `quote` | Dark | Full-bleed portrait image of Michael Tay (Group Managing Director). Quote overlay centered on image: *"True luxury can only exist in authenticity."* Context line below: "The Hour Glass. Founded 1979. 70+ boutiques across Asia-Pacific." Portrait height: 80vh, min 500px. |
| IV | Market Signal | `market-signal` | Light | Four animated stat counters showing market data. Closing line: "Fewer watches. Higher prices. Every relationship compounds." |
| V | Position | `position` | Light | Two-column grid (Scale / Philosophy) documenting THG's current position. Includes pull-quote from Michael Tay. |
| VI | Competitive Frame | `competitive-frame` | Light | Three-page horizontal slider comparing THG against Cortina Watch, Watches of Switzerland, and Hodinkee. Uses live website screenshots via thum.io API. Arrow navigation, keyboard support, touch/swipe support. |
| VII | Tension | `tension` | Dark (full-bleed image bg) | Full-viewport statement: "The boutique ends at the door. The collector's journey does not." Ginza boutique background image with parallax. |
| VIII | Four Pressures | `pressures` | Light | Four numbered items describing strategic threats: digital vacuum, brand disintermediation, fragmented client intelligence, the discovery gap. Presented in 2x2 grid. |
| IX | Four Openings | `openings` | Light | Four numbered items describing strategic opportunities: collector platform, certified pre-owned, AI-augmented clienteling, cultural authority at scale. Presented in 2x2 grid. |
| X | What AKQA Brings | `akqa-brings` | Deep dark (#121212) | Three-column layout with video/image media for each capability. Plus a featured full-width case study ("The Generative Store"). |
| XI | Projected Outcomes | `outcomes` | Light | Six outcome metrics in a grid, plus an interactive SVG stacked area chart showing cumulative revenue impact over 5 years. Toggleable layers. |
| XII | Close | `close` | Dark | Statement: "In a market defined by scarcity, the relationship is the product." CTA: "We'd welcome the conversation." |
| XIII | Footer | — | Dark | "AKQA — Confidential — 2026" |

### 3.4 Market Signal Stats (Animated Counters)

| Value | Label |
|-------|-------|
| -1.7% | Swiss watch exports, FY2025 |
| -52% | U.S. exports, November 2025 |
| -40% | China, cumulative two-year decline |
| +4.9% | Secondary market price recovery |

### 3.5 Position — Scale & Philosophy

**Scale Column:**
- S$1.16B revenue (FY2025). H1 FY2026: +14% revenue, +23% profit.
- 70+ boutiques. Eight countries. Singapore to New Zealand.
- All four dominant brands: Rolex, Patek Philippe, Audemars Piguet, Richard Mille — 49% of Swiss watch export value.
- $90M Rolex Australia acquisition (June 2025).

**Philosophy Column:**
- Physical-first. Michael Tay's aspiration: "the Four Seasons of specialist luxury watch retail."
- Cultural programming: Malmaison concept salons, art commissions, IAMWATCH exhibitions.
- Connoisseurship over commerce — the boutique as cultural hub.

**Pull Quote:** *"It is more a hub for enthusiasts to gather than a store designed to ensure a commercially focused outcome."* — Michael Tay

### 3.6 Competitive Frame — Slider Details

**Three frames (pages), each containing a 4-column comparison grid:**

**Frame 1 — Home Page:**
| Brand | Screenshot URL | Commentary |
|-------|---------------|------------|
| The Hour Glass | thehourglass.com | Editorial narrative. Brand story above all else — no product grid, no pricing. |
| Cortina Watch | cortina.watch | Product-forward hero with brand carousel. Commerce intent from first scroll. |
| Watches of Switzerland | watchesofswitzerland.com | Full retail experience. Video, search, promotions — 22% of revenue generated digitally. |
| Hodinkee | hodinkee.com | Content-first. Editorial authority that converts readers into buyers. |

*Commentary:* "The Hour Glass leads with brand narrative. The rest lead with product and commerce. Two different philosophies — but only one leaves revenue on the table."

**Frame 2 — Product Page:**
| Brand | Screenshot URL | Commentary |
|-------|---------------|------------|
| The Hour Glass | thehourglass.com/rolex | Brand landing page, not product detail. No individual watches, no specifications, no price. |
| Cortina Watch | cortina.watch/brands | Full product grid with pricing and add-to-cart. Transactional from browse to basket. |
| Watches of Switzerland | watchesofswitzerland.com/Rolex | Rich product detail. Pricing, stock indicators, virtual consultation booking. |
| Hodinkee | hodinkee.com/shop | Curated shop. Editorial context wraps every product — reviews drive purchase decisions. |

*Commentary:* "Cortina and WoS show full product detail with pricing and purchase paths. Hodinkee bridges editorial and commerce. The Hour Glass presents watches as narrative — no price, no purchase path."

**Frame 3 — Cart & Purchase:**
| Brand | Screenshot URL | Commentary |
|-------|---------------|------------|
| The Hour Glass | N/A | No cart. No checkout. The digital experience ends at discovery. The transaction requires a physical visit. |
| Cortina Watch | cortina.watch/cart | Full checkout flow. Online exclusives drive conversion from discovery to delivery. |
| Watches of Switzerland | watchesofswitzerland.com/shopping-bag | Complete digital purchase path. Click-and-collect or home delivery. |
| Hodinkee | hodinkee.com/cart | Streamlined checkout. Content-to-commerce pipeline fully closes the loop. |

*Commentary:* "Three competitors offer a complete digital purchase path. The Hour Glass has none — the digital experience ends at discovery."

**Closing:** "Three design for the digital collector. One does not."

### 3.7 Four Pressures

| # | Title | Description |
|---|-------|-------------|
| I | The digital vacuum | Competitors deploy commerce, virtual consultation, online exclusives. THG presents an editorial brochure. The gap widens quarterly. |
| II | Brand disintermediation | Rolex launches its own CPO programme. Omega invests in DTC. The retailer's value demands redefinition through experience, community, and data. |
| III | Fragmented client intelligence | 70 boutiques, 8 countries, likely 70 disconnected client records. A collector who purchases in Singapore and services in Tokyo exists as two strangers. |
| IV | The discovery gap | Next-generation collectors form preferences on Instagram, Hodinkee, Reddit — long before entering a boutique. Physical-first is invisible in the phase that matters most. |

### 3.8 Four Openings

| # | Title | Description |
|---|-------|-------------|
| I | The collector platform | Members-only digital ecosystem connecting 70+ boutiques. Collection tracking, service history, priority allocations, provenance verification. |
| II | Certified Pre-Owned | Secondary market prices rose 4.9% in 2025. THG holds 45 years of transaction data. A curated CPO programme unlocks a new P&L line and new collector entry point. |
| III | AI-augmented clienteling | Intelligent client profiles across every boutique advisor. Purchase history, preference mapping, next-best-action. "Four Seasons aspiration — operationalised through technology." |
| IV | Cultural authority at scale | Leverage existing cultural programming (Malmaison, IAMWATCH, art commissions) via a dedicated content platform to capture the discovery phase. |

### 3.9 What AKQA Brings — Three Pillars + Featured Case Study

| # | Pillar | Description | Media Asset | Reference |
|---|--------|-------------|-------------|-----------|
| I | Experience Strategy and Design | Map end-to-end collector journey. Design digital layer around discovery, acquisition, ownership, advocacy. | Video: `videos.ctfassets.net/.../End-page-video.mp4` (Dior) | Dior — luxury experience design |
| II | Connected Commerce Platform | Unify 70+ boutiques into one relationship. Appointment booking, virtual consultations, allocation management, collection tracking. | Image: LV Collection Silhouette (Contentful CDN) | TAG Heuer Connected Modular 45 (linked to akqa.com/work/tag-heuer/) |
| III | AI and Data Intelligence | AI-powered clienteling. Unified client profiles, cross-market insights, next-best-action. | Image: LV Grid Static (Contentful CDN) | Blockchain provenance with Louis Vuitton and Loro Piana |

**Featured Case Study — The Generative Store:**
- Full-width video: `videos.ctfassets.net/.../Google-UX.mp4`
- Description: "Commerce rebuilt from first principles. Every store assembled in the moment of need — drawing from brand heritage, design systems, and real-time visitor context. Copy, imagery, and narrative adapt to each individual. Not a chatbot. A fully realised boutique experience at global scale. Built with Google Gemini."

### 3.10 Projected Outcomes — Five-Year Financial Model

| Metric | Projection | Incremental Value | Description |
|--------|-----------|-------------------|-------------|
| Digital-influenced revenue | +8–12% | ~S$93M–S$139M incremental over base | From near-zero digital share to meaningful omnichannel contribution |
| Client retention | +12–18% | ~S$35M–S$52M retained annually | Unified profiles, proactive outreach, cross-market continuity |
| Cross-sell conversion | +15–20% | ~S$23M–S$35M incremental | The right watch, the right client, the right moment |
| Content engagement | 2–3x | Organic reach compounding | Cultural authority driving discovery-stage acquisition |
| CPO revenue stream | New P&L | ~S$15M–S$25M by year 3 | 45 years of provenance data activated |
| Staff productivity | +10–15% | ~S$8M–S$12M efficiency gains | Intelligent tools free time for relationships |

**Year 5 Projected Total: S$318M** (cumulative across all layers)

### 3.11 Interactive Stacked Area Chart Data (S$ Millions by Year)

| Layer | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|-------|--------|--------|--------|--------|--------|
| Digital Revenue | 25 | 55 | 90 | 120 | 145 |
| Client Retention | 10 | 25 | 40 | 50 | 55 |
| Cross-sell | 8 | 18 | 30 | 38 | 42 |
| Content | 3 | 8 | 15 | 22 | 28 |
| CPO Stream | 0 | 5 | 15 | 22 | 28 |
| Productivity | 5 | 10 | 15 | 18 | 20 |

Chart is interactive: users can toggle individual layers on/off via buttons or by clicking outcome cards. Chart redraws dynamically. Greyscale palette (not coloured).

---

## 4. Technical Architecture

### 4.1 File Structure

```
/
├── index.html              # Ṛta Intelligence (1,787 lines)
├── the-hour-glass.html     # The Hour Glass Strategic Document (2,280 lines)
└── /images/
    └── michael-tay-portrait.jpg  # Referenced but stored externally
```

### 4.2 Zero-Dependency Architecture

Both files are **fully self-contained single-page HTML files** with:
- Inline `<style>` blocks (no external CSS)
- Inline `<script>` blocks (no external JS)
- No framework dependencies (no React, Vue, jQuery, etc.)
- No build tools required (no webpack, vite, etc.)
- Google Fonts loaded via CDN link tags (only external dependency)
- Media assets loaded from external CDNs (Contentful, thum.io)

### 4.3 External Asset Dependencies

**index.html:**
- Google Fonts: DM Sans, Instrument Serif

**the-hour-glass.html:**
- Google Fonts: Cormorant Garamond, Inter
- Portrait image: `/images/michael-tay-portrait.jpg`
- Competitor screenshots: `image.thum.io` (live screenshot API, 12 URLs)
- AKQA case study videos: `videos.ctfassets.net` (Contentful CDN, 2 videos)
- AKQA case study images: `images.ctfassets.net` (Contentful CDN, 2 images)

### 4.4 JavaScript Features

**index.html:**
- HTML5 Canvas particle system (hero) with device pixel ratio handling
- Mouse-reactive star field (150px radius, gravitational push effect)
- Waterfall canvas animation (stack section)
- Intersection Observer for scroll-reveal animations
- Orbital planet system with CSS animations + click-to-expand detail panels
- Animated stat counters with eased counting
- Cell toggle (Human/Agent) panel switching
- Smooth scroll with "Return to Cosmos" anchor

**the-hour-glass.html:**
- Password gate with Enter key handler and shake animation on error
- Word-by-word hero title reveal animation (staggered 150ms)
- Intersection Observer for scroll-reveal (`.reveal`, `.reveal-slow`, `.hr-reveal`, `.hr-reveal-full`)
- Animated stat counters (negative/positive values, decimals, prefixes/suffixes)
- Competitive frame slider (3 pages): arrow buttons, keyboard navigation (ArrowLeft/ArrowRight when in view), touch/swipe support (50px threshold)
- Interactive SVG stacked area chart with toggle buttons + clickable outcome cards
- Parallax controller (skipped on mobile <640px, skipped for reduced motion)
- Video playback control via Intersection Observer (play when 30% visible, pause otherwise)

---

## 5. Design System

### 5.1 Ṛta Intelligence — Design Tokens

**Color Palette:**
| Token | Value | Usage |
|-------|-------|-------|
| `--bg-deep` | `#060d06` | Page background |
| `--bg-primary` | `#0a1209` | Section backgrounds |
| `--bg-card` | `rgba(18, 32, 18, 0.7)` | Card backgrounds |
| `--bg-card-hover` | `rgba(28, 50, 28, 0.85)` | Card hover state |
| `--moss` | `#3a7233` | Primary green accent |
| `--moss-light` | `#5a9a50` | Light green |
| `--amber` | `#d4a55a` | Warm accent, quotes |
| `--amber-glow` | `#e8c547` | Glowing amber |
| `--gold` | `#c9952e` | Gold accent |
| `--cyan` | `#00e5c7` | Key accent (stats, hero Ṛ) |
| `--coral` | `#d4726a` | Warnings |
| `--text-primary` | `#e8e0d4` | Main body text |
| `--text-secondary` | `#a09888` | Secondary text |
| `--text-dim` | `#6a6258` | Dimmed text |

**Typography:**
| Role | Font | Weight | Size |
|------|------|--------|------|
| Display/Headings | Instrument Serif | 400 | clamp(2rem–8rem) |
| Body | DM Sans | 300–600 | 0.75rem–1rem |
| Section Labels | DM Sans | — | 0.75rem, uppercase, 0.25em tracking |

**Visual Textures:**
- SVG noise grain overlay (fixed, 3.5% opacity, fractalNoise)
- Topographic background pattern (SVG ellipse pattern, 4% opacity)
- Leaf-vein SVG dividers between sections

### 5.2 The Hour Glass — Design Tokens

**Color Palette:**
| Token | Value | Usage |
|-------|-------|-------|
| `--black` | `#000000` | Dark section backgrounds |
| `--dark` | `#121212` | Deep section backgrounds |
| `--dark-section` | `#222222` | Media placeholders |
| `--body-text` | `#414141` | Body text |
| `--muted` | `#BFBFBF` | Labels, secondary text |
| `--divider` | `#E5E5E5` | Horizontal rules |
| `--white` | `#FFFFFF` | Light backgrounds |
| `--off-white` | `#F5F5F5` | Hero text, light section text |

**Typography:**
| Role | Font | Weight | Size |
|------|------|--------|------|
| Hero headline | Cormorant Garamond | 400 | clamp(3rem, 8vw, 6rem) |
| Section headlines | Cormorant Garamond | 400 | clamp(2rem, 4vw, 3rem) |
| Pull quotes | Cormorant Garamond | 400 italic | clamp(1.5rem, 3vw, 2.25rem) |
| Body prose | Cormorant Garamond | 400 | 1.125rem |
| Labels/UI | Inter | 500 | 0.75rem, uppercase, 0.15em tracking |
| Meta text | Inter | 400 | 0.8125rem |

**Layout:**
- Content width: 900px (default), 1200px (wide)
- Section padding: 8rem vertical
- Content wrap padding: 0 2rem

---

## 6. Interaction & Animation Specifications

### 6.1 Shared Patterns

| Pattern | Specification |
|---------|--------------|
| Scroll reveal | Fade up (30–40px translate Y), 600–800ms, cubic-bezier easing. Triggered at 15% intersection, -50px root margin. |
| Stagger delays | 100ms increments (stagger-1 through stagger-6) |
| Reduced motion | All animations/transitions disabled via `prefers-reduced-motion: reduce` media query |

### 6.2 Ṛta Intelligence — Unique Interactions

| Interaction | Detail |
|-------------|--------|
| Hero particles | Canvas-based. Up to 300 particles. 5 colors (green, amber, blue, white, cyan). Drift, oscillate. Mouse repulsion effect within 150px radius. Parallax scroll fading. |
| Waterfall canvas | Background particles in the Stack section. Gentle downward drift simulating water. |
| Orbital system | CSS `@keyframes orbit` rotation. 5 concentric rings (160px–480px). Click a planet to show detail panel with smooth fade. |
| Cell toggle | Two-panel toggle with active state tracking. Human Cell (3 nodes) / Agent Cell (5 nodes). Slide transition. |
| Stat counters | Animated count-up on scroll into view. Eased cubic timing over 1500ms. |

### 6.3 The Hour Glass — Unique Interactions

| Interaction | Detail |
|-------------|--------|
| Password gate | Full-screen fixed overlay. Enter-key trigger. 600ms fade-out on success. 400ms shake animation on failure. |
| Hero word reveal | Each word in "The Hour Glass" wrapped in `.word-mask`. Staggered 150ms translateY(110% → 0) transitions. |
| Hero rule animation | Horizontal line width: 0 → 80px, 800ms, 800ms delay after word reveal. |
| Stat counters | Animated counting (supports negative values, decimals, +/- prefix). 1200ms duration. Ease-out cubic. |
| Competitive slider | 3-frame horizontal slider. `translateX(n * -100%)` transitions (500ms). Arrow buttons, keyboard (←/→ when section in view via IntersectionObserver), touch swipe (50px threshold). |
| Impact chart | SVG stacked area chart. 6 toggleable layers. Greyscale palette. Dot markers at data points. 0.4s fade-in animation per path. Total recalculates on toggle. |
| Parallax | `data-parallax` attribute on elements. Speed-based vertical offset relative to viewport center. Disabled on mobile (<640px) and reduced motion. |
| Video playback | Videos pause when out of view (30% threshold), play when scrolled into view. Uses IntersectionObserver. |
| Media placeholders | Animated gradient pulse (`placeholder-shift`, 4s loop) behind images/videos while loading. Labels shown until media loads. |

---

## 7. Content Inventory

### 7.1 Ṛta Intelligence — Key Copy

- **Hero tagline:** "Natural Intelligence"
- **Hero title:** "Ṛta"
- **Hero subtitle:** "Right Time, Right Action"
- **Philosophy quote:** "Intelligence flows downward like water; wisdom rises back like roots."
- **Footer:** "Technology serves. Earth judges. Wisdom takes time."

### 7.2 The Hour Glass — Key Copy

- **Hero title:** "The Hour Glass"
- **Hero subtitle:** "A strategic perspective on what comes next."
- **Michael Tay quote:** "True luxury can only exist in authenticity."
- **Market signal closing:** "Fewer watches. Higher prices. Every relationship compounds."
- **Position headline:** "Where you stand."
- **Competitive frame headline:** "What surrounds you."
- **Tension statement:** "The boutique ends at the door. The collector's journey does not."
- **Pressures headline:** "What presses inward."
- **Openings headline:** "What opens outward."
- **AKQA headline:** "Three spaces. One system."
- **Outcomes headline:** "Hypothetical impact. Five years."
- **Closing statement:** "In a market defined by scarcity, the relationship is the product."
- **CTA:** "We'd welcome the conversation."

### 7.3 Media Assets Required

| Asset | Type | Location | Used In |
|-------|------|----------|---------|
| Michael Tay portrait | JPEG | `/images/michael-tay-portrait.jpg` | Quote section hero |
| Ginza boutique | Background image | Referenced in CSS (tension section) | Tension section |
| Dior end-page video | MP4 | Contentful CDN | AKQA — Experience Strategy |
| LV Collection Silhouette | PNG/WebP | Contentful CDN | AKQA — Connected Commerce |
| LV Grid Static | PNG/WebP | Contentful CDN | AKQA — AI & Data |
| Google UX video | MP4 | Contentful CDN | AKQA — Generative Store |
| 12x competitor screenshots | Live capture | thum.io API | Competitive frame slider |

---

## 8. Accessibility & Performance

### 8.1 Accessibility

- **Reduced motion:** Both pages implement `@media (prefers-reduced-motion: reduce)` — all animations, transitions, and parallax are disabled.
- **Keyboard navigation:** Competitive slider supports arrow key navigation. Password gate supports Enter key.
- **ARIA labels:** Slider arrows have `aria-label` attributes.
- **Semantic HTML:** Proper use of `<section>`, `<h1>`–`<h4>`, `<blockquote>`, `<footer>`, `<button>`.
- **Loading strategy:** Hero images are `loading="eager"`, all other images are `loading="lazy"`.
- **Alt text:** Present on all `<img>` elements.

### 8.2 Performance

- **Single-file architecture:** Zero HTTP requests for CSS/JS (all inline).
- **Canvas optimisation:** Device pixel ratio capped at 2x. Particle count capped at 300.
- **Scroll optimisation:** `requestAnimationFrame` used for all scroll handlers. `{ passive: true }` on scroll/touch listeners.
- **Video management:** Videos auto-pause when out of view to reduce resource usage.
- **Image loading:** Lazy loading on below-fold images. thum.io screenshots load on demand.

### 8.3 Responsive Design

**Ṛta Intelligence breakpoints:**
- 768px: Reduce orbital system size, adjust cell node layout
- 480px: Further reduce orbit system, compact stats

**The Hour Glass breakpoints:**
- 900px: Stats grid → 2 columns, position grid → single column, frame grid → 2 columns
- 600px: Stats grid → 1 column, frame grid → 1 column, slider arrows → smaller

---

## 9. Development History & Iterations

### 9.1 Timeline of Changes (Chronological)

| Commit | Branch | Description |
|--------|--------|-------------|
| `07341eb` | master | Initial Ṛta Intelligence interactive visual page |
| `13f2503` | master | Add mouse-reactive stars, orbital system, and waterfall effect |
| `c09235a` | hour-glass-document | Add The Hour Glass strategic document — password-protected single-page HTML |
| `cf99a05` | fix-hero-overlap | Fix hero overlap, redesign competitive frame as slider, add interactive impact chart |
| `8335da3` | fix-hero-overlap | Update THG: rebrand footer, fix screenshots, link case studies, recalculate financials |
| `d86005a` | fix-hero-overlap | Add case study visuals and image load handlers for AKQA sections |
| `94b011d` | fix-hero-overlap | Add YouTube video bg to hero, Michael Tay image behind quote, remove top confidential line |
| `fe3b6ac` | fix-hero-overlap | Fix Michael Tay image crop and reduce bottom spacing |
| `ea6531d` | fix-hero-overlap | Overhaul competitive frame: screenshots, pagination, typography |
| `f8b1df5` | fix-hero-overlap | Add Ginza boutique background to tension section, update case studies |
| `04b4b48` | fix-hero-overlap | Fix Michael Tay hero: taller container, lower-third quote, tighter spacing |
| `cee8930` | full-bleed-portrait | Make Michael Tay portrait full-bleed at all viewport sizes |
| `6d2fbef` | full-bleed-portrait | Center quote and attribution over portrait image |
| `0c827e7` | full-bleed-portrait | Update AKQA case study media with real assets |
| `ba6861d` | full-bleed-portrait | Convert Pressures/Openings to 2x2 grid, fix AKQA media visibility |

### 9.2 Key Design Iterations

1. **Hero Evolution:** Started as simple text hero → added YouTube video background → switched to portrait-based hero with Michael Tay image → made portrait full-bleed with centered quote overlay.

2. **Competitive Frame:** Started as static cards → redesigned as horizontal slider with pagination → added live screenshots via thum.io → overhauled typography and pagination UI.

3. **AKQA Section:** Started with placeholder media → linked to actual AKQA case study assets from Contentful CDN (Dior video, LV images, Google UX video).

4. **Pressures/Openings:** Started as vertical numbered lists → converted to 2x2 grid layout for better visual density.

5. **Michael Tay Portrait:** Multiple iterations on cropping, container height, quote positioning — settled on full-bleed 80vh portrait with centered quote overlay.

### 9.3 Pull Requests

| PR # | Branch | Description | Status |
|------|--------|-------------|--------|
| #1 | `claude/hour-glass-document-Zcu4H` | Initial Hour Glass strategic document | Merged |
| #2 | `claude/fix-hero-overlap-z0WEV` | Hero overlap fix, slider redesign, interactive chart | Merged |
| #4 | `claude/full-bleed-portrait-image-XRHyg` | Full-bleed portrait, AKQA assets, grid layout | Merged |

---

## Appendix: Quick Reference for Rebriefing

### What to build (in the correct repo):

**File 1: `index.html` — Ṛta Intelligence**
- Self-contained single-page HTML
- Dark nature-themed aesthetic (deep greens, amber, cyan)
- Interactive canvas hero with mouse-reactive particles
- Orbital planet system (5 intelligences)
- Waterfall stack (5 layers: Insight → Earth)
- Two-cell architecture toggle (Human Cell / Agent Cell)
- Feedback loop diagram

**File 2: `the-hour-glass.html` — The Hour Glass Strategic Pitch**
- Self-contained single-page HTML, password-protected (`akqa2026`)
- Minimal luxury aesthetic (black, white, grey — Cormorant Garamond + Inter)
- Full-bleed Michael Tay portrait with quote overlay
- 4 animated market stats
- 2-column position grid (Scale / Philosophy)
- 3-page competitive slider with live screenshots (THG vs Cortina vs WoS vs Hodinkee)
- Full-viewport tension statement with Ginza boutique background
- 4 Pressures + 4 Openings (2x2 grids)
- AKQA capabilities (3 pillars + Generative Store featured case study)
- 6 projected outcome metrics + interactive SVG stacked area chart (S$318M 5-year total)
- Closing CTA

**Key technical constraints:**
- Zero external dependencies (no frameworks, no build tools)
- All CSS and JS inline in the HTML file
- Google Fonts via CDN only
- Media from Contentful CDN and thum.io
- Full reduced-motion support
- Responsive down to 480px
