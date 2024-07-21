# Cross Site Request Forgery

<!-- published_date: 21 Jul, 2024 -->
<!-- description: CSRF, XSRF -->
<!-- tags: security, hacking, csrf, xsrf -->

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. With a little help from social engineering (such as sending a link via email or chat), an attacker may trick the users of a web application into executing actions of the attacker’s choosing.

As represented in this diagram, a Cross Site Request Forgery attack is roughly composed of two parts:

1. Cross-Site: The user is logged into a website and is tricked into clicking a link in a different website that belongs to the attacker.
The link is crafted by the attacker in a way that it will submit a request to the website the user is logged in to. This represents the “cross-site” part of CSRF.

2. Request Forgery: The request sent to the user’s website is forged with values crafted by the attacker.
When the victim user opens the link in the same browser, a forged request is sent to the website with values set 
by the attacker along with all the cookies that the victim has associated with that website.

