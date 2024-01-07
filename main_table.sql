CREATE OR REPLACE TABLE `burnished-form-410209.zomato.tbl_analytics` AS(
select 
r.ID, Name, Veg, KnownFor, Dining, Full_Address, Area,
stat_ID, zomato_reviews, zomato_ratings, Delivery_Reviews, AverageCost
from 
`burnished-form-410209.zomato.stats` s join `burnished-form-410209.zomato.restaurant_dimension` r
on s.ID = r.ID)

