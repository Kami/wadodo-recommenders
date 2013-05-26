# Simple Category Recommender

A recommender which finds matching activities based on the relative importance 
from categories which are parsed from user's likes.

## How it works

For the start we can assign each likes’ category a relative importance,
based on % of user’s likes of activities in a specific category (relative
to all liked activities).

Category | # of likes | Rel. importance
-------- | ---------- | ---------------
Health/beauty | 18 | 0.286
Athlete | 14 | 0.222
Sport | 13 | 0.206
Clubs | 10 | 0.159
Music | 8 | 0.127
*Total* | *63* | *1*

Relative importance tells us how valuable (how frequently liked) is a
specific category to the user.

The next step is to connect Facebook categories with Wadodo categories.
Facebook has many more categories than Wadodo and some are even irrelevant
for us (community, company ...). We need to associate each Facebook category
with related category on Wadodo.

Facebook | Wadodo
-------- | ------
Athlete | Sport
Sport | Sport
Recreation | Sport

Actual formula to calculate activity matching score is:

```
ACTIVITY’S MATCHING SCORE = SUM(RI(ACTIVITY_CATEGORY))
```

For each listed activity that has at least one category that matches user’s
liked categories we calculate a “matching score”.

We use the information about activity’s categories and a number which
represents user’s relative importance of specific category.

We connect each category with it’s belonging relative importance and sum up
the numbers. Activities with higher score are listed higher.

## Example

Category | # of likes | Rel. importance
-------- | ---------- | ---------------
Health/beauty | 18 | 0.286
Athlete | 14 | 0.222
Sport | 13 | 0.206
Clubs | 10 | 0.159
Music | 8 | 0.127
*Total* | *63* | *1*


An activity which is listed in all of the above categories will have a score
equal to 1 and will be listed as first.

An activity which is in categories: clubs, music and food will be scored as
follows:

```
ACTIVITY’S MATCHING SCORE = SUM(RI(ACTIVITY’S_CATEGORY))
```

```
Stratosphere Nightclub Matching Score = SUM (music + clubs + food)
Stratosphere Nightclub Matching Score = 0.127 + 0.159 + 0
Stratosphere Nightclub Matching Score = 0.286
```

As this activity is listed in two categories that are less important to the
user it is still listed almost on the same spot as one other activity which is
listed only in “health/beauty” (but is this single category more important
to user).

If we feel this  is good enough to go public, we can just show only the top X %
of results and allow users to manually apply some filters.
