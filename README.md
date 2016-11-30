# NaNoGenMo-2016

National Novel Generation Month 2016

I have always been fascinated with ciphers. As a software professional, I supposed I am meant to be good at them. But I am not, particularly. But I enjoy thinking about them; I retain a child-like wonder about them.

This, my entry in the National Novel Generation Month challenge by Darius Kazemi, uses a simple substitution cipher to encrypt twenty-six famous short stories, some of which are still under copyright. I suppose this is some kind of commentary on copyright--to publish them using a simple encryption scheme. But mostly I was interested to see how easy it might be to “read” a familiar story in an encrypted form.

For those unfamiliar with simple substitution ciphers, the idea is to replace each letter of the alphabet with a different, random, letter of the alphbet. If the “key” is a → b, b → c, c → d, d → e, e → f, etc, then the encryption of “The cat sat on the mat.” is “Uif dbu tbu po uif nbu.” For English, there are !26, or 148 septillion 362 sextillion 637 quintillion 348 quadrillion 470 trillion 135 billion 821 million 287 thousand 825 different possible keys (at least, if letters are  not allowed to encrypt themselves).

Despite this huge number, it is usually easy to break a simple substitution cipher based on letter frequencies and word patterns. Looking at the example above, noticing that “uif” appears twice is a hint that the original was “the.”

My original plan was to present several short stories, each with a different key. So, my first task was to look for stories that I loved that might be fun to encode. As I did so, though, I decided it would be even more fun to play with the kinds of encodings I used, perhaps even making it possible to read the story without laboriously deciphering it. In fact, this idea came to me when working with the Sherlock Holmes story, The Adventure of the Dancing Men, which is itself a story (spoiler alert!) about a substitution cipher. What if I used the code in Dancing Men to encode the story Dancing Men? What if I used the different heart symbols to encode the vowels of The Tell-Tale Heart by Poe, and use the emoji for cask for his Cask of Amontillado? Surely, Jackson’s The Lottery ought to use numbers for encoding. Only Flannery O’Connor’s story Revelation is hidden behind a full substitution cipher.

I hope you’ll enjoy this work. As always, I am grateful to Darius Kazemi for the very idea of National Novel Generation Month. Some simple cipher code can be found in my NaNoGenMo-2016 repository at GitHub (https://github.com/willf/NaNoGenMo-2016).
