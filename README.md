# Hao Luo — Personal Academic Website

Personal academic website and research portfolio for **Hao Luo (骆浩)**, Ph.D. candidate in Mechanical Engineering at Tsinghua University.

**Live site:** [https://charlie-99-max.github.io](https://charlie-99-max.github.io)

## Research focus

- Living DNA data storage
- Engineered Living Memory Microspheroids (ELMMs)
- Regenerative Living Disk–Drive systems
- Microfluidics and biofabrication
- Automated scientific instruments

## Site structure

- `index.html` — homepage and research portfolio
- `publications.html` — complete peer-reviewed publication list
- `patents.html` — complete patent record with original Chinese titles
- `projects.html` — complete bilingual record of 14 research and engineering projects
- `media.html` — verified bilingual archive of 25 media, institutional news, and teaching-practice records
- `cv.html` — web CV with links to the complete records
- `assets/cv/Hao_Luo_CV_EN.pdf` — downloadable English academic CV
- `assets/cv/Hao_Luo_CV_CN.pdf` — downloadable user-provided Chinese academic CV
- `css/style.css` — responsive visual system
- `js/main.js` — navigation, language switch, and subtle reveal effects

The site uses plain HTML, CSS, and vanilla JavaScript, with no build step or external runtime dependencies.

## Updating content

Edit the HTML files directly. Replace research images in `assets/images/` while keeping filenames stable, or update the corresponding image paths in `index.html`. Regenerate the English CV with:

```bash
python3 scripts/generate_cv.py
```

## Research image credits

- ELMM and Living Disk–Drive research visuals: Hao Luo and co-authors, *Advanced Materials* (2025, 2026).
- Patient-specific lung cancer assembloid visual: Zhang et al., *Nature Communications* 15, 3382 (2024), licensed under CC BY 4.0.

© 2026 Hao Luo.
