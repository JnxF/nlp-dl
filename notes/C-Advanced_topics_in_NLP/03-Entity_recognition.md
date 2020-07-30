# Entity recognition

What:
* Location, people, names.
* Varies among industries.
* Find them in the text and connect with Wikipedia.
* Useful: same concepts with different names.
* One to many relationship.

Example:
* Take the context around names.
* Example, _of_ before the name, a comma.
* Sometimes there is a title: _Mr_, _General_, _President_.

Differences with news and tweets:
* In news, person are politicians, celebrities. In tweets: actors, TV, ...
* Same with locations and organizations.

Issues:
* Capitalization: all uppercase, all lowercase, all letters upper initial.
* Unusual spelling, acronyms, abbreviations.

Feature representation:
* BIO: begin (B), inside (I), out (O). 
* SVM-U (uneven). E.g. SVM where one class has many points (very well defined the class) vs. very few.

Inference algorithm:

How to capture non-local dependencies:
* German verbs
* Inter-text references.

How to incorporate external knowledge / databases:
