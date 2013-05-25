Title: Migrating my site to github
Date: 2013-03-25 08:20
Tags: github, wordpress
Category: Ramblings
Slug: migrating-my-site-to-github
Author: Dan De Sousa
Summary: My considerations when migrating my site to github.
Status: draft

I recently left my secure job to pursue my dream of working for myself. In honor of new beginnings, I felt it appropriate that I migrate my website to github. As I plan to be a much more active member of the open source community, I decided to delve right in and move from wordpress to a github pages hosted site with a theme of my own design. I'll go over how I did this, the tools I used, the code I developed, etc. Convienently, these and the subsequent blog posts will server as test data for my theme / tool development.

## Why move away from something like Wordpress?

This is an interesting question because is presumes something, mainly that given an already setup Wordpress site is not currently meeting your needs. For me those needs were control, visibility, simplicity. 

I wanted control over how my site was generated. I wanted to understand everything that was going on under the hood. Unfortunately this meant learning, nay 'groking' PHP. While I admire and respect PHP as the "father" of server side web languages, I would feel much more comfortable having something depending only on python. Additionally, wordpress has dependencies like MySQL, which is yet another dependency I would rather not wish to have, given the low level of user interaction on my site.

So I decided to go with github pages, which lets me serve my content statically. I opted to go with pelican over jekyll. Again, opting for something written in python which I could assist with contributing right away, and because it provided a bit more flexibility in terms of templating and generation over jekyll and liquid. 

## What works and what doesn't

Right off the bat, I found that for just quickly getting setup, it pelican works great. It let's me choose the markup language I want, generate my page and commit to a separate branch in my github repo. However, I find myself wanting for page management and organization (something I plan to take a stab at in the near future). Additionally, while there is a fair amount of themes available for pelican, they aren't as numerous as jekyll or wordpress (of which there are literally thousands).

## Future work

I plan on doing the following in the near future:

  * Create my own theme
  * Create a set of util scripts to assist with pelican post / page management
