# Stagger web resources

## Web App
### /app/
* Splash page
* Login
* Download App
### /app/login
* Login via email
* Login via Facebook
* Login via Google
* Create account
### /app/createAccount
* Create account with email
* Create account with Facebook
* Create account with Google
### /app/makeStagger
* Name stagger
* Dynamic list length
* Autocomplete addresses
* Select transport types
* Select start time
* Select duration
### /app/publish
* Create an event
* Share on social media
* Make public
### /app/myStaggers
* Checkerboard of staggers
* Favourite public staggers
### /app/stagger/{UID}
* Show stagger
* Share on social media
* Create event
* Save to favourites
### /app/recommendedStaggers
* Checkerboard of staggers
* Stagger ratings
* GeoLocation based recommendations
* Paid promotions


## Restful API
### /api/generateCrawl
* Take /app/makeStagger  form and return instructions

 
# To Do
## V0.1
* Create base site template
* Create /app/makeStagger form possibly using deform
* Create /api/generateCrawl
## V0.2
* Create database possibly MongoDB
* Create account management & login page template
* Add session cookies
* Create /app/myStaggers
## V0.3
* Create /app/recommendedStaggers
* Make mobile versions
* Implement google ads
## V0.4
* Push to AWS
* Create MongoDB
* Create Elastic load balancer 
## V1.0
* Add hare on social media
* Add create Facebook event
## V1.1 
* Create Android app
* Create iPhone app
## V1.2
* Create Windows Phone app
## V1.3
* Transition restful API to AWS serverless and API gateway
