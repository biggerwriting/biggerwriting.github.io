---
date: '{{ .Date }}'
draft: false
title: '{{ replace .File.ContentBaseName "-" " " | title }}'
image: "{{ "/images/pic.jpg" | relURL }}"
alt_text: "{{ replace .Name "-" " " | title }} screenshot"
summary: "Summary of the {{replace .Name "-" " " | title }} project"
tech_used:
  - JavaScript
  - CSS
  - HTML
---

Description of the {{ replace .Name "-" " " | title}} project.
