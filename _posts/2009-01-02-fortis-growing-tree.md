---
layout: project
title: Fortis growing tree
client: Fortis
teaser: When the theme of the conference of one of the largest banks in Belgium is "grow", only a custom-written tree will do.
images:
  - fortis1.jpg
  - fortis2.jpg
---
The 2007 conference for Fortis was a special one. That year, they merged private and merchant banking, and needed a way to tell their top employees. They held the conference under the Louvre in Paris, and we were invited to create a special celebratory multimedia spectacle.

The theme for their conference was "grow", something that matched our tastes perfectly. We wrote custom software showing off the best in generative design. We designed a custom, dynamic tree containing all of the faces of the Fortis employees that joined the  conference.

Generative growth
=================
We used a generative growth algorithm, called L-System or Lindenmayer system, for modeling the growth of the tree. This recursive system allows you to accurately model most types of trees and plants. A ruleset defines the form and shape of the tree, and a set of parameters modifies the look. We wrote 8 custom rulesets, each one resulting in a different tree. In our case, each segment of the tree is drawn as a face of an employee.

[Wikipedia -- L-system](http://en.wikipedia.org/wiki/Lindenmayer_system)

The ultimate deadline
=====================
We could create the tree generation software beforehand, but supplying the photos of all the employees required us to go to Paris. There, we worked with the photographers stationed in several hotels around the city to get the approximately 3000 photos that needed to be in the tree. These photos kept coming until the last minute, where we had only one chance to do it right. With all the photos loaded and the program well-tested, we pressed the spacebar on the presenting computer and off it went.

Big screen, big print
=====================
Once the presentation was over, the project was shown as a looping animation on a big screen in the lobby of the conference hall. This allowed attendees to examine the tree in further detail.

As a final touch, each of the employees received a poster of the tree with their photo in it. Since we could not print this in advance, we had to generate a PDF document on the scene, and let it print overnight. The result was a highly detailed print, where every employee could -- in true *Where's Wally* fashion -- look for their photo amongst the thousands of other "leaves".

For this project, both the end result, presented in different media, and the design process were engaging. We happily noticed that employees were curious about the mechanics behind the project, and we were happy to explain.
