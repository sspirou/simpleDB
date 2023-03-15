### Very simple in memory mock db table


#### Why?

I performed pretty miserably on my first live coding interview, so I redid it after the fact for some timed practice. The task was quite simple and didn't require any real problem solving: 
- Implement a very simple SQL-ish in-memory db that validates type of insertions and keeps strings < 20 chars and ints in range -1024 to 1023.
- allow table retreival and removal from db by table name
- allow row insertion
- allow conditional row retreival 
- support table printing

#### Explanation

A few hours after my terrible showing on the first live coding interview I ever did, I sat down and re-wrote the test case from memory (I think I included everything). During the interview, I spent the first 15-ish minutes refreshing myself on SQL commands only to realize the task didn't require any knowledge of SQL. Then, I implemented the logic in python3. I was very rough on my object-oriented use of python, so this was a slow process. I test 'compiled' my code as I wrote it (surpise, no errors!) only to find out that my code was littered with invalid syntax once I uncommented the test lines. In the moment and nervousness of the interview I had failed to think about how a scripting language would not throw compilation errors.. Really goes to show what nerves can do to mental performance. Anyhow, my final code made use of the JavaScript keyword `this` instead of python's `self` when accessing instance variables which meant that my code didn't run. Guessing round 3 with this company will be canceled 😆.

#### The redo

After venting about how I failed miserably on an interview I should have crushed and taking a long walk, I sat down and wrote the correct code in `db.py` in about 20 minutes. This README took way longer than the code itself! On to the next one, will certainly have better luck next time.
