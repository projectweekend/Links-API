The RESTful API for what will become: http://links.projectweekend.net

## Development Environment

The development environment for this project is fully bootstrapped and portable with the help of: [Vagrant](http://www.vagrantup.com/), [Docker](https://www.docker.com/), and [Fig](http://orchardup.github.io/fig/index.html). If using Linux, all of the `Vagrant` stuff can be ignored since Docker runs natively.

* `vagrant up` - Start the VM. On first launch a lot of things need to be downloaded and installed so it could take a little while. Subsequent launches are much faster.
* `vagrant ssh` - Connect to the VM
* `vagrant halt` - Shut down the VM
* `vagrant destroy` - Delete the VM.
* `/vagrant` - The path on the VM where the project code is mounted. All `fig` commands mus be executed from this path.
* `fig up` - Start the web application and database containers. On first launch base containers will be downloaded from the Docker Registry so it could take a while. Subsequent launches are much faster.
* `fig build` - Rebuild the web application container. This needs to be done any time a new Python dependency is added to `requirements.txt`
* `fig run web python manage.py syncdb` - Run Django's `syncdb` command on a new database.
* `fig run web python manage.py migtrate` - Apply South database migrations
* `fig run web python manage.py test` - Run all project tests

-------------------------------------------------------------------------------

### Register a new user

**POST:** `/v1/maker/register`

**Body:**
~~~json
{
    "email": "test@test.com",
    "password": "adfadsf",
    "first_name": "Thomas",
    "last_name": "Jefferson"
}
~~~

**Response:** None

**Status Codes:**
* `201` - Registration was created
* `400` - Invalid request body


### Verify new user email address

**POST:** `/v1/maker/email/verification`

**Body:**
~~~json
{
    "token": "asdjfkal48a09d853qlkjadfl93&%3l2k"
}
~~~

**Response:** None

**Status Codes:**
* `200` - Verification was successful
* `400` - Invalid request body


### Request password reset for user

**POST:** `/v1/maker/password/reset`

**Body:**
~~~json
{
    "email": "test@test.com"
}
~~~

**Response:** None

**Status Codes:**
* `201` - Reset request was created
* `400` - Invalid request body


### Reset password for user

**POST:** `/v1/maker/password/reset/update`

**Body:**
~~~json
{
    "token": "alskdfj93lak4r&$@_23;lads",
    "new_password": "newPassword",
    "confirm_password": "newPassword"
}
~~~

**Status Codes:**
* `200` - Authentication was successful
* `400` - Invalid request body
* `412` - Invalid reset token


### Authenticate user

**POST:** `/v1/maker/authenticate`

**Body:**
~~~json
{
    "identifier": "test@test.com",
    "password": "adfadsf"
}
~~~

**Response:**
~~~json
{
    "token": "kja03984q0oaj34j*@$Fmjadfl"
}
~~~

**Status Codes:**
* `200` - Authentication was successful
* `400` - Invalid request body
* `401` - Invalid identifier/password


### Request email change for user

**POST:** `/v1/maker/email`

**Body:**
~~~json
{
    "new_email": "something@different.com"
}
~~~

**Response:** None

**Status Codes:**
* `201` - Request was created
* `400` - Invalid request body
* `409` - Email in use
