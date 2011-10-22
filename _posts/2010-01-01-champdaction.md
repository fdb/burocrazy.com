---
layout: project
title: Champ d'Action logo and website
client: Champ d'Action
teaser: Creating a new brand identity and website in one week, on-site, sounds crazy? It is.
images: 
  - champlogos.png
  - champsite.jpg
---
The rebranding of Champ d'Action, a contemporary music ensemble, happened during an intense workshop week, where we did both the logo design and website. Champ d'Action is known for its creative approaches to both process and end result, something that corresponds to our way of working. So they got a set of designers together, including Burocrazy, to design a new identity, their seasonal brochure, and a new website, all in a week's time.

The Champ d'Action logo
=======================
The Champ d'Action logo is made by NodeBox, our open-source 2D environment for graphic design with scripting. Since Champ d'Action means *field of action*, they wanted to carry over that dynamism in their logo. The logo is based on a custom sketching algorithm, that takes an underlying path (the form of the "clean" logo) and automatically redraws it using a sketch-like look. Instead of just letting the algorithm create one variant and declare that the logo, we run the script multiple times, resulting in an endless set of variations. The end result is not just a logo, it is a toolbox for constructing Champ d'Action logos. The identity is not fixed to one particular variant of the symbol: rather, we want to get as much variation on the logo out there as we can.

Custom content management system
================================
To manage the content for their website, and document all current and past projects, we created a custom content management system based on a wiki. This meant that editing the site became effortless, a process that, before, could only be handled by the webmaster.

Just as with any site, the logo is prominently displayed at the top. However, since we created a logo that has endless variations, we decided to integrate this into the website. Therefore, each page you view has a different variation on the logo. Even reloading the page shows a different logo. In addition, the longer you stay on the site, the more the logo decomposes, ultimately incorporating robots and strange heads. 

Projects: three of a kind
=========================
Just as with any other musical ensemble, Champ d'Action works on projects. These projects begin from vague ideas, and gradually form into concrete shape, finally to materialize as a finished production. Champ d'Action wanted to visualize this process of a project evolving from a rough sketch all the way to an archived project. Within our wiki, we built the idea of "state". 

Whenever a new project was started, its state would be set to "sketch". This would be reflected in the design where the page looked like a scrapbook of loose ends. As the state progressed, so did the design, getting more rigid and aligning with the overall feel of the rest of the project. This allowed visitors to quickly grasp the advancement of a project.

Custom content types
====================
We started to recognize patterns as the site matured. A project always had a calendar attached to it. Some pages contained information about CD's, including preview tracks. An internal database contained a list of contacts. We acted on these patterns to create a set of *content types*, classes of objects that held the same information. These could then be searched, filtered, ordered and arranged in a consistent format.

Instead of building a new content management system from scratch, we started out with Django as the foundation of our website. Django is an open-source web design framework, written in Python, that allows for ultimate flexibility and control, without sacrificing speed. It is described as the framework for "perfectionists with deadlines", something that appealed to us.

We mapped out our custom content types, attaching events to projects that could be arranged in a calendar. We extended the administration back-end by integrating a WYSIWYG editor and media framework, so website maintainers could easily adapt the pages to their liking.

The system has proven to be reliable and fast. It is easy to use, so everyone within the organization is able to modify the content they manage, and spruce up pages with images, links and YouTube videos. For a public musical ensemble, the website is a crucial communication tool. Our solution makes that succeed.
