# py_flashcards

I write all my notes for school in the Obsidian editor. So they're in Markdown. To study for my upcoming midterm, I wanted to turn these notes into flashcards. Unfortunately, all the "Anki" and spaced-repition are way too overkill for what I need.

I just want to turn my markdown notes into a set of flashcards I can just practice over and over.

I tried using Neuracache. Got my notes all nicely formatted and into the app before realizing I can't even shuffle my notes. So fuck it. I just wrote my own CLI text-only flashcard script in Python.

The file must contain any number of "cards" in the following format:

```
title (the question) #flashcard #other_tag
answer to the question on
any number of
lines.

---
```

Start the program like

```
python3 main.py example.md
```

#### Commands
- `go [tag]`: shuffles the deck and starts the flashcards. Tag is an optional parameter. If not specified, it plays all cards. If specified, it shows only cards with the matching tag.
- `return/enter key`: If last shown was a question, show the answer. If last shown was an answer, show the next question.
- `r`: redo the last card.


#### Notes
- any word starting with the `#` symbol in the title will be parsed as a tag.
- Make sure to include the `#flashcard` tag in each card or it won't be included.


