---
layout: page
title: Staff
description: A listing of all the course staff members.
---

# Staff 🧑‍🏫
{: .fs-7 .fw-400 }

## Instructor

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## Staff

{% assign tas = site.staffers | where: 'role', 'Teaching Assistant' %}
{% assign tutors = site.staffers | where: 'role', 'Tutor' %}
<div class="role">
  {% for staffer in tas %}
  {{ staffer }}
  {% endfor %}
  {% for staffer in tutors %}
  {{ staffer }}
  {% endfor %}
</div>
