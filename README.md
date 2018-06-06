# ![9.9] twitter_block2mute ![8.8]
A tool for turning the Twitter users you have blocked into mutes. :seedling:

This script will take accounts you have [blocked](https://help.twitter.com/en/using-twitter/blocking-and-unblocking-accounts), unblock them and mute them. Users that you unblock will be able to view your profile and message you, while muted they will not appear in your feeds.

This script will need to be rerun periodically if you continue to use the block feature.
This script was written in June 2018.

--------

### Run with:
 *  `python3 twitter_block2mute.py`

--------


Functional notes:


    1. You will need a Twitter APP Key (apps.twitter.com) for the account you are executing these muting requests from.

    2. This script has been built to observe rate limits and to use Twitter's API respectfully.
       This script has been run for over X hours with no sign of interuption.
       Testing extreme cases uses: After running this script for X hours an estimated X users will have been ![9.9]unblocked and muted.

    3. This script can be interupted and when restarted it will work on unblocking & muting any remaining blocked users.

    4. Do not use any of the code I have written with harmful intent.

    5. By using this code you accept that every person has the right to choose their own gender identity.


Comments, critiques, need help? Contact me [![alt text][6.3]][3]  [![alt text][1.2]][1]

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->
[1.2]: https://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[1]: https://www.twitter.com/AGreenDCBike
[6.3]: http://i.imgur.com/9I6NRUm.png (github icon without padding)
[3]: https://github.com/antoinemcgrath

[8.8]: https://imgur.com/xIihGGC.png  (No Audio icon)
[9.9]: https://i.imgur.com/ShevBEa.png  (Blocked Twitter verified icon)
