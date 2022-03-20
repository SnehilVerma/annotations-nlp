# annotations-nlp

You are given a set of 120 rows of data ( tweets ) scraped from internet and you are expected to annotate each row with either **'sports'** or **'politics'** label. 
You can clone the repo, make changes to the **output_[user].xlsx** file, by adding a new column 'type' and adding the labels infront of each row.
Once done, you can push the file back to the repo.

IMPORTANT : Please make changes to the file with your name as the suffix. **Do not overwrite other user's file.**


 

## Example data with label = sports 
(1)
@ACNI2012 @TheToka920 Never knew having 1 or 2 followers had anything to do with reality...Malinga has never been s… https://t.co/SSmLS18O4k	**sports**

(2)
"MYCA Magical Moments:

September, 2011: Sham Chotoo of the Bowie Boys and Girls Club joins Maryland Youth Cricket a… https://t.co/zpbqXvK21S"	**sports**

(3)
"The current state of last year's @BBL finalists - 
@StarsBBL - P10 - W9 L1
@RenegadesBBL - P10 - W1 L9 

😲🙃😵😵😵 #Cricket #BBL09"	**sports**

## Example data with label = politics
(1)
"RT @allisonpearson: “We believe they have made an informed choice about their sexual behaviour.”
Gordon Brown’s government on the young gir…"	**politics**

(2)
"@johnlegend Your ignorance of real world politics is nauseating.

Warren is a fraud https://t.co/BPstZAksu0"	**politics**

(3)
"RT @ellymelly: A friend of mine has discovered 2020's pick-up line of choice (do NOT use it)!

"How's the climate in your local area? Is it…"	**politics**

## Points to keep in mind
While many of the text sequences would have keywords and context which you can use to decide whether it should be labeled as politics or sports, there would be sentences which might not be intuitive enought for you to judge. Take for instance, 

** "RT @ellymelly: A friend of mine has discovered 2020's pick-up line of choice (do NOT use it)!
"How's the climate in your local area? Is it…** 

The above text doesn't directly correspond to sports or politics but in the original dataset it's labeled as **politics**. A quick search on the google with the user handle 'ellymelly' depicted that this particular user always tweets on political issues and thus the label makes sense.
This being said, I don't expect this fine grained analysis from you, and just want you to label it as best as you can. Cheers and good luck 👍



