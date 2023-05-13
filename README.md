# Network
The social network project is a web application designed to provide users with a platform for social interaction, content sharing, and connection with other users. It is built using a combination of Python, JavaScript, HTML, and CSS.

Key Features:

User Registration and Authentication: Users can create accounts and log in securely to access the social network's features.
New Post Creation: Signed-in users can write and submit text-based posts through a dedicated form or a "New Post" box on the main page.
All Posts Display: The "All Posts" page presents users with a chronological feed of all posts from all users, with the most recent posts appearing at the top. Each post includes the username, content, timestamp, and number of likes.
User Profile Pages: Clicking on a username leads to the corresponding user's profile page. This page showcases the user's posts in reverse chronological order and displays the number of followers and followings the user has.
Follow/Unfollow Functionality: On a user's profile page, signed-in users can choose to follow or unfollow that user, enabling them to see the followed user's posts on the "Following" page.
Following Page: The "Following" page displays posts exclusively from the users that the current user follows, providing a curated feed.
Pagination: To manage the display of a large number of posts, pagination is implemented. Each page shows a maximum of 10 posts, with navigation buttons for moving between pages.
Edit Post: Users can edit their own posts by clicking an "Edit" button. The post's content is replaced with a textarea, allowing users to modify the text. The edited post can be saved without reloading the entire page, thanks to JavaScript.
Like/Unlike Posts: Users can interact with posts by liking or unliking them. Clicking on a "like" button triggers an asynchronous request to update the like count on the server. The post's like count is then dynamically updated on the page using JavaScript.
Languages Used:

Python: The backend of the social network is built using Python. It handles user authentication, post creation, data storage, and retrieval.
JavaScript: JavaScript is used extensively to enhance the user experience and implement dynamic features such as editing posts, updating like counts, and providing seamless interactions without page reloads.
HTML: The structure and layout of the web pages are created using HTML, ensuring proper formatting and organization of the content.
CSS: CSS is utilized for styling and customizing the appearance of the web pages, ensuring an attractive and user-friendly interface.
