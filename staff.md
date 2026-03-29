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

{% assign staff = site.staffers | where: 'role', 'Staff' %}
<div class="role">
  {% for staffer in staff %}
  {{ staffer }}
  {% endfor %}
</div>
