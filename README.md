# Wagtail Social

Social networking site built with Wagtail CMS

## Project scope

The initial project will aim to include the following features:

- user registration
- user profiles
- regions
- chapters
- chapter posts
- activity streams

### User registration

Users should be able to register for the site. To reduce the liklihood of SPAM registrations, we may create an invitation system that will be used by existing, trusted users.

### User profiles

Once users have registered, they should be able to fill out a basic user profile, with fields such as:

- full name (optional)
- biography (optional)
- photo (optional)
- interests (optional): keyword tags of user interests, perhaps from a pre-defined list

In addition to the above details, user profiles should show an activity feed for the recent activities of a given user within the networking site.

### Regions

Regions are used to group chapters. Regions should be non-overlapping.

### Chapters

Chapters are essentially groups that people can join and are representative of physical locations, such as a city.

Each chapter should have a dedicated page with the following:

- title and description
- chapter posts (e.g. news updates or events)
- members list
- "join" button

Chapters have stewards, who are users with special privileges. Chapter stewards can perform tasks for the chapter, such as:

- approving members
- adding posts
- managing chapter page details

### Activity streams

Activity streams highlight recent activities for chapters or individual users.

### Keywords (e.g. Interests)

Keyword tags should allow people to explore connections throughout the network and find related content. For example, clicking an interest tag on a user profile would show other users with similar interests.

## Further ideas

This section is intended to collect further ideas that might be out of scope for the initial project.

- membership directory: find members based on location, interests, or other criteria

## Thanks

Thank you to the following people and resources for guiding this project along.

- [LearningDjango](https://learndjango.com/books/)
- [simple is better than complex](https://simpleisbetterthancomplex.com/)
