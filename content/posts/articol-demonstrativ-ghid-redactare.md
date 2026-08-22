---
title: "Ghid de Redactare & Articol Model Fiecare Voce" # [OBLIGATORIU] Titlul principal al articolului afișat în antet și pe carduri
date: 2026-08-20 # [OBLIGATORIU] Data publicării articolului (format: AAAA-LL-ZZ, ex: 2026-08-20)
lastmod: 2026-08-20 # [OPȚIONAL] Data ultimei actualizări/revizuiri (format: AAAA-LL-ZZ)
draft: true # [OBLIGATORIU] Starea publicării: false = vizibil pe site, true = ciornă ascunsă
summary: "Ghidul tehnic complet și articolul model de referință care exemplifică toate câmpurile de date meta, formatările și shortcode-urile disponibile pe platforma Fiecare Voce." # [OBLIGATORIU] Rezumat scurt (1-2 fraze) afișat pe prima pagină, la căutare și în liste
description: "Ghid complet pentru redactarea și publicarea articolelor pe platforma independentă a tinerilor Fiecare Voce."
author: "Echipa Fiecare Voce" # [OBLIGATORIU] Numele autorului principal (ex: "Luca Georgescu" sau "Echipa Fiecare Voce")
authors: ["Luca Georgescu", "Iulia Geambazu"] # [OPȚIONAL] Lista tuturor autorilor/contribuitorilor din redacție
categories: ["Ghiduri", "Proiecte"] # [OBLIGATORIU] Categoriile articolului (ex: "Proiecte", "Educație", "Opinii", "Ghiduri")
tags: ["ghid", "redactare", "demo", "evenimente", "tehnologie", "jurnalism"] # [OPȚIONAL] Etichete/cuvinte cheie legate de subiect (pentru căutare și filtrare)
image: "/images/posts/demo-cover.jpg" # [OBLIGATORIU] Calea către imaginea de copertă (salvată în folderul static/images/...)
image_position: "center 40%" # [OPȚIONAL] Punctul de aliniere a coverului (ex: "center 30%", "center top", "center center")
image_fit: "cover" # [OPȚIONAL] Modul de încadrare al coperții: "cover" (umple tot cadrul) sau "contain" (încadrare completă)
photo_credit: "Unsplash / Foto Demo" # [OBLIGATORIU] Textul de credit foto afișat pe ecusonul galben al coperții (ex: "Foto: Arhiva Fiecare Voce")
featured: false # [OPȚIONAL] Articol Recomandat / Feature: true = prioritizează articolul pe prima pagină și în capul listei de articole cu un ecuson verde "★ RECOMANDAT", false = articol standard
---

<!-- SECTIUNE INTRODUCTIVA -->
Acest articol servește drept **Model de Referință (Proof-of-Concept)** și ghid tehnic complet pentru redactarea articolelor pe platforma *Fiecare Voce*. El ilustrează modul în care sunt structurate datele meta (frontmatter), stilurile neo-brutaliste de tipografie și toate shortcode-urile interactive disponibile.

---

<!-- SECTIUNEA 1: GHID FRONTMATTER -->
## 1. Structura Antetului (YAML Frontmatter)

Fiecare fișier Markdown din folderul `content/posts/` începe cu un antet YAML delimitat de `---`. Mai jos este structura completă comentată linie cu linie:

```yaml
---
title: "Ghid de Redactare & Articol Model Fiecare Voce" # [OBLIGATORIU] Titlul principal al articolului
date: 2026-08-20 # [OBLIGATORIU] Data publicării (AAAA-LL-ZZ)
lastmod: 2026-08-20 # [OPȚIONAL] Data ultimei revizuiri (AAAA-LL-ZZ)
draft: false # [OBLIGATORIU] false = vizibil pe site, true = ciornă
summary: "Rezumatul scurt (1-2 fraze) afișat în cardurile de pe prima pagină." # [OBLIGATORIU] Rezumat card
description: "Ghid complet pentru redactarea și publicarea articolelor pe platforma independentă a tinerilor Fiecare Voce."
author: "Echipa Fiecare Voce" # [OBLIGATORIU] Autor principal
authors: ["Luca Georgescu", "Iulia Geambazu"] # [OPȚIONAL] Lista autorilor
categories: ["Ghiduri", "Proiecte"] # [OBLIGATORIU] Categorii principale
tags: ["ghid", "redactare", "demo", "evenimente"] # [OPȚIONAL] Etichete pentru căutare
image: "/images/posts/demo-cover.jpg" # [OBLIGATORIU] Calea către imaginea de copertă
image_position: "center 40%" # [OPȚIONAL] Focalizare copertă ("center 30%", "center top")
image_fit: "cover" # [OPȚIONAL] Încadrare copertă ("cover" sau "contain")
photo_credit: "Unsplash / Foto Demo" # [OBLIGATORIU] Text ecuson galben credit foto
featured: true # [OPȚIONAL] true = articol recomandat (prioritizat automat ca Hero Card cu insignă "★ RECOMANDAT")
---
```

---

<!-- SECTIUNEA 2: ELEMENTE TIPOGRAFICE -->
## 2. Elemente de Tipografie & Stil

Platforma utilizează o tipografie **Neo-Brutalistă** cu contraste puternice și fonturi moderne.

### Exemple de Citate (Blockquotes):
> "Jurnalismul comunitar al elevilor nu este doar despre a raporta probleme, ci despre a oferi soluții reale și a construi o voce puternică în societate."
> — *Manifestul Fiecare Voce*

---

<!-- SECTIUNEA 3: GALERIE FOTO -->
## 3. Galerie Foto Dinamică (`{{</* gallery */>}}`)

Pentru articolele care conțin mai multe imagini de la evenimente, se folosește shortcode-ul intuitiv `{{</* gallery */>}}`. Acesta generează automat un slider orizontal compact, cu contor live, navigare prin touch/swipe și modul zoom pe tot ecranul (Lightbox Modal).

{{< gallery folder="images/evenimente/demo-gallery" title="Galerie Foto Eveniment — Atelierul de Jurnalism 2026" caption="Instantanee din cadrul atelierelor practice organizate cu elevii din redacție." />}}

```markdown
{{</* gallery folder="images/evenimente/nume-folder" title="Titlu Galerie" caption="Descriere opțională" */>}}
```

---

<!-- SECTIUNEA 4: EMBED INSTAGRAM -->
## 4. Integrare Postare Instagram (`{{</* instagram-embed */>}}`)

Se folosește pentru a încorpora o postare oficială de Instagram într-un cadru neo-brutalist cu buton direct către aplicație.

{{< instagram-embed url="https://www.instagram.com/p/DcOYWBpoxEm" caption="Urmărește activitatea redacției noastre pe Instagram @fiecarevoce!" />}}

```markdown
{{</* instagram-embed url="https://www.instagram.com/p/ID_POSTARE/" caption="Descriere opțională" */>}}
```

---

<!-- SECTIUNEA 5: NUMĂRĂTOARE INVERSĂ (COUNTDOWN) -->
## 5. Numărătoare Inversă Eveniment (`{{</* countdown */>}}`)

Generează un temporizator live pentru evenimente viitoare (Gale, conferințe, lansări), cu actualizare în timp real secundă cu secundă.

{{< countdown date="2026-12-31T23:59:59" title="Gala Anuală a Elevilor și Tinerilor Jurnaliști 2026" expired_message="EVENIMENTUL A ÎNCEPUT!" />}}

```markdown
{{</* countdown date="2026-12-31T23:59:59" title="Titlu Eveniment" expired_message="Mesaj la expirare" */>}}
```

---

---

<!-- SECTIUNEA 7: CASETA DE DESCARCARE (DOWNLOAD) -->
## 7. Descarcare Documente & Fișiere (`{{</* download */>}}`)

Afișează o casetă neo-brutalistă pentru descărcarea ghidurilor, regulamentelor sau fișierelor PDF/DOC/SVG.

{{< download url="/images/logo.svg" title="Pachetul Oficial de Identitate Vizuală Fiecare Voce" description="Ghidul oficial de brand, sigle în format vector SVG și elemente grafice de reprezentare." format="SVG" size="626 KB" />}}

```markdown
{{</* download url="/cale/fisier.pdf" title="Titlu Document" description="Descriere document" format="PDF" size="2.4 MB" */>}}
```

---

<!-- SECTIUNEA 8: EMBED CARD LINK (BOOKMARK) -->
## 8. Card de Link Extern / Bookmark (`{{</* embed-link */>}}`)

Generează o casetă de preview pentru linkuri externe sau resurse asociate (stil Notion/Medium Bookmark).

{{< embed-link url="https://www.instagram.com/fiecarevoce/" title="Pagina Oficială Instagram Fiecare Voce" description="Urmărește ultimele știri, interviuri și proiecte realizate de elevi din toată țara." site="INSTAGRAM" image="/images/posts/demo-cover.jpg" />}}

```markdown
{{</* embed-link url="https://link-extern.ro" title="Titlu Link" description="Descriere resursă" site="NUME SITE" image="/cale/imagine.jpg" */>}}
```

---

<!-- SECTIUNE CONCLUZIE -->
## 9. Concluzie

Acest articol model demonstrează că toate componentele vizuale, funcționale și meta ale platformei funcționează într-un ecosistem integrat, oferind o experiență de citire modernă, interactivă și accesibilă pe orice dispozitiv.
