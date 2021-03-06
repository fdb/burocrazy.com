---
layout: project
title: Trunk & Co Catalog
client: Samsonite / Creastore
teaser: A young and trendy catalog in five different languages? No problem with our custom solution.
images:
  - trunk1.jpg
  - trunk2.jpg
  - trunk3.jpg
  - trunk4.jpg
  - trunk5.jpg
---
When Creastore approached us to do a product catalog for Samsonite's youth brand, Trunk & Co, we were excited. They explained to us that they wanted to transform the traditionally uninspired product catalog into a gorgeous design item, to be valued greatly by stores retailing the brand. This meant we got virtually *carte blanche* on the design aspect.

Integrating the precise, informative purpose of the catalog with a design that was young and playful was a compelling challenge. The client desired a hands-on approach, which we delivered by involved him in all the aspects of the process, presenting design iterations every step of the way. The client was happy to to explore the design space with us, and had substantial impact on the design.

A fully automated solution
==========================
We knew we had to deal with rapidly changing requirements and many design iterations. Therefore, we chose to automate the process of generation the product pages by writing a custom solution in [NodeBox](http://nodebox.net/), an open-source tool for creating 2D designs using a scripting language, which we conceived. This allowed us to have swift turnarounds. Whenever a product's description or specification changed, we would press a button and an up-to-date version of the catalog was regenerated as a fully certified PDF, ready for printing.

The catalog needed to be developed in five different languages. Instead of laboriously design each version by hand, we created an XML description containing all product details together with internationalized information. In addition, we wrote a dictionary with domain-specific translations on backpacks, with translations for words like "straps", "sizes", "weight", etc. Whenever we needed to generate, say, a Spanish version of the catalog, we would change the language switch and NodeBox would generate a translated version of the catalog.
