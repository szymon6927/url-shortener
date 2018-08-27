# url-shortener-
[![CircleCI](https://circleci.com/gh/szymon6927/url-shortener/tree/master.svg?style=shield)](https://circleci.com/gh/szymon6927/url-shortener/tree/master)

http://kajakisekowski.pl/

Marketing application created for kayaking company [kajakisekowski.pl](https://kajakisekowski.pl/)

Application isn't available without authentication for obvious reasons. It's used internally in company

The main idea of ​​this app is to catch GA-client-id during redirection. Admin is giving a client phone number and URL which is going to be shortened. Shortener URL is sent to the client. It means when client click shortener link, he sees redirection screen but under the hood application give him a ga-client-id and after that app will redirect him to previously entered URL

App hosted at [heroku](https://www.heroku.com/) with CI supported by [CircleCI](https://circleci.com/)
