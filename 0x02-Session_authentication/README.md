# Project: 0x02. Session authentication

## Resources

- [REST API Authentication Mechanisms - Only the session auth part](https://www.youtube.com/watch?v=501dpx2IjGY)
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

## Learning Objectives

- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies

## Tasks

| Task                                     | File                                                                                                                         |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 0. Et moi et moi et moi!                 | [api/v1/app.py](./api/v1/app.py), [api/v1/views/users.py](./api/v1/views/users.py)                                           |
| 1. Empty session                         | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py), [api/v1/app.py](./api/v1/app.py)                               |
| 2. Create a session                      | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py)                                                                 |
| 3. User ID for Session ID                | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py)                                                                 |
| 4. Session cookie                        | [api/v1/auth/auth.py](./api/v1/auth/auth.py)                                                                                 |
| 5. Before request                        | [api/v1/app.py](./api/v1/app.py)                                                                                             |
| 6. Use Session ID for identifying a User | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py)                                                                 |
| 7. New view for Session Authentication   | [api/v1/views/session_auth.py](./api/v1/views/session_auth.py), [api/v1/views/**init**.py](./api/v1/views/**init**.py)       |
| 8. Logout                                | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py), [api/v1/views/session_auth.py](./api/v1/views/session_auth.py) |
