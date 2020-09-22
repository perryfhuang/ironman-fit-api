# IRONMAN Fit API

The API for IRONMAN Fit is built with Django and PostgresQL. The two resources that the API works with is `Users` and `Workouts`, stored as tables in a SQL database, PostgresQL. Using Django and Django's REST Framework, I built the API routes for creating, reading, updating and deleting both of these resources. I've required user/token authentication for creating, updating and deleting `Workouts`. Indexing/gettings workouts and user profile information is an unauthenticated action, however, as I want to allow users to view the workout Feed and profiles of active users without having to sign up with an account. All in all, Django was great to use, with a lot more tools than Express. My favorite part of Django is having access to an admin portal where you can CRUD any of your resources without having to write the actual routes!! Some challenging and new concepts I found when using Django was learning how serializers work (model vs. regular serializers, when to use serializers, etc.) and overall just learning how to write class-based views in a completely new language!

## Important Links

- [Deployed API](https://ironman-api.herokuapp.com/)
- [IRONMAN Fit App](https://perryfhuang.github.io/ironman-fit-client/)
- [IRONMAN Fit App GitHub Repo](https://github.com/perryfhuang/ironman-fit-client)


## Planning Story

During planning, I wanted the app to support logging lifts, runs, bikes, and swims and rendering them to a feed. Currently, users are able to log lifts with up to 10 exercises including detailing weight, sets and reps for each exercise. For runs, biks and swims, users can log distance as well as total time. For all workouts, users can write a caption - bringing a social aspect to each workout. I also wanted to implement likes and comments on each workout, but I knew that for the sake of attaining MVP (minimum viable product) within the allotted project time, I would have to cut those features out for now. That said, this would be the first feature I implement for V2. See below for more features I plan to implement for the app. The app also supports viewing user profiles, and their personal workout activity as well as editing their own profile. Currently, the editable user profile fields are: name, city, state, country, bio, gender, height and weight, though the gender, height and weight fields aren't actually used and rendered anywhere in the app currently. Futher down the line, I could see some use for this information (tracking weight, using height for different metrics, etc.). In addition, indexing/gettings workouts and user profile information is an unauthenticated action, as I wanted to allow users to view the workout Feed and profiles of active users without having to sign up with an account. Posting, editing and deleting workouts, however, are acitons that require authentication.

## API End Points

| Verb   | URI Pattern          | Controller#Action       |  Token Required |
|:-------|:---------------------|:------------------------|-----------------|
| POST   | `/sign-up/`          | `users#sign-up`         |   `false`       |     
| POST   | `/sign-in/`          | `users#sign-in`         |   `false`       |
| PATCH  | `/change-pw/`        | `users#change-password` |   `true`        |
| DELETE | `/sign-out/`         | `users#sign-out`        |   `true`        |
| GET    | `/users/`            | `users#index`           |   `false`       |
| GET    | `/users/:id/`        | `users#show`            |   `false`       |
| PATCH  | `/user-profile/:id/` | `users#update`          |   `true`        |
| GET    | `/workouts/`         | `workouts#index`        |   `false`       |
| GET    | `/workouts/:id`      | `workouts#show`         |   `false`       |
| POST   | `/create-workout/`   | `workouts#create`       |   `true`        |
| PATCH  | `/workouts/`         | `workouts#index`        |   `true`        |
| DELETE | `/workouts/`         | `workouts#delete`       |   `true`        |


All data returned from the API is formatted as JSON.

### User Stories

- As a user, I want to sign up.
- As a user, I want to sign in.
- As a user, I want to be able to change password.
- As a user, I want to sign out.
- As a user, I want to ‘create’ a lift/run/swim/bike session by entering in distance and time for the run/bike/swim or information for the workout including exercise, weight, number of sets and reps, and caption (stretch: picture upload!)
- As a user, I want to be able to delete my past lifts/runs/swims/bikes.
- As a user, I want to be able to edit my past lifts/runs/swims/bikes.
- As a user, I want to be able to view all of my past lift/runs/swims/bikes.
- As a user, I want to be able to see friends’ activity on a feed.
- As a user, I want to view my profile, which shows my past activity.
- As a user, I want to be able to see friends' profiles and individual activity on their profile.
- As a user, I want to be able to edit my profile.

### Technologies Used

- Django
- Django REST Framework
- PostgresQL
- SQL
- Heroku
- Python
- pip
- Postman (to test API endpoints)

### Future Iterations

Below are features that will be implemented in future versions of the app, listed in order of priority:

- 'Users' page which lists all active users on the app [DONE]
- Likes and comments on `Workout` resource
- Picture uploads for profile pictures & with each `Workout` resource
- Following/'adding' friends -> adding relationships between `Users`
- Add more cutom emoticons for workout logs (ex. 'Perry Huang is feeling ...') 
  - Currently there is a `feeling` field in the `Workout` model, now I just have to tie that into the front-    end!!
- Integrate GPS tracking for live tracking of run/swim/bike distance

### Entity Relationship Diagram (ERD)
![ERD](https://i.imgur.com/DgU9UBE.jpg)
