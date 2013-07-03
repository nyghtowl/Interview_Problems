'''
Sample database structure

Twitter Feed

User
    id
    handle string
    name


Tweets
    id
    user_id
    comment string (140)
    datetimestamp

Mention
    id
    ref_handle_id
    tweet_id

Follow
    user_follower_id
    user_followed_id


select comment from tweets where user_id in (
  Select user_followed_id from follow where user_follower_id = 1
) order by datetimestamp desc limit 100;


select comment from tweets inner join follow 
  on tweets.user_id = follow.user_followed_id 
where follow.user_follower_id = 1
order by datetimestamp desc limit 100;


User A follows User B
User B follows User A
User A follows User C
C follows no one
'''